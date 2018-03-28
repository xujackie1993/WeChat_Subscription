#-*- encoding=utf-8 -*-
'''
Provide cache access mechanism.
'''
import functools
import re

KEY_CHARS = r'[^a-zA-Z0-9_-]'


def to_cache_key(cache_key):
    '''
    Filter off non-supported chacraters for memcached key
    string.
    '''
    if type(cache_key) is not str:
        cache_key = cache_key.encode('utf-8', 'ignore')
    return re.sub(KEY_CHARS, '', cache_key)


class Cached(object):
    '''
    A decorator to wrap the return value of function
    in the cache.

    parameters for init
    -------------------
    clients: list of cache clients,
        The clients used for cache access.

    parameters
    ----------
    key: string or callable,
        The cache key, if it is callable, the parameters
        is of the form "*sub, **kw", which is the parameters
        of the wrapped function.
    timeout: integer,
        How long the key is to be timeout in cache.
    log_to: function, default None,
        Accept function like log(msg), if provided, hit/miss
        log will be logged via the function.
 
    parameters when calling
    -----------------------
    __force_refill: boolean,
        Default False, whether to refill the cache.

    example
    -------
    cached = Cached(clients)

    @cached(key=lambda *sub, **kw: 'user_%s' % kw['user_id'],
            timeout=60):
    def user_profile(user_id=None):
        # Get user profile info
        return profile
    '''
    def __init__(self, *clients):
        self._clients = clients

    def _fill(self, depth, key, value, timeout):
        timeout_factor = len(self._clients) - depth
        for client in self._clients[depth::-1]:
            reduced_timeout = timeout / timeout_factor\
                              if timeout else timeout
            timeout_factor += 1
            client.set(key, value, reduced_timeout)

    def _get(self, key, timeout, func, __force_refill, log_to, *sub, **kw):
        if __force_refill:
            ret = None
        else:
            for i, client in enumerate(self._clients):
                ret = client.get(key)
                if ret is not None:
                    if i > 0:
                        self._fill(i - 1, key, ret, timeout)
                    break
        if ret is None:
            log_to("Key %s miss." % key)
            ret = func(*sub, **kw)
            self._fill(len(self._clients) - 1, key, ret, timeout)
        else:
            log_to("Key %s hit." % key)
        return ret

    def __call__(self, key, timeout=0, log_to=None):
        log_to = log_to if log_to else lambda x: None
        def entangle(func):
            @functools.wraps(func)
            def wrapper(*sub, **kwargs):
                __force_refill = kwargs.pop('__force_refill', False)
                __log_to = kwargs.pop('__log_to', None) or log_to
                cache_key = key(*sub, **kwargs) if callable(key) else key
                cache_key = to_cache_key(cache_key)
                cache_timeout = timeout(*sub, **kwargs) if callable(timeout) else timeout
                ret = self._get(cache_key, cache_timeout,
                                func, __force_refill, __log_to,
                                *sub, **kwargs)
                return ret
            return wrapper
        return entangle
