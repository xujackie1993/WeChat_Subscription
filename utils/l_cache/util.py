#-*- encoding=utf-8 -*-
'''
Basic utilites for cache.
'''
import hashlib


def freeze(o):
    if isinstance(o, dict):
        return tuple(sorted([(k, freeze(v)) for k, v in o.items()],
                              key=lambda x: x[0]))
    elif isinstance(o, list):
        return tuple([freeze(v) for v in o])
    elif isinstance(o, tuple):
        return tuple([freeze(v) for v in o])
    elif isinstance(o, set):
        return tuple([freeze(v) for v in sorted(o)])
    return o


def to_hash(*sub, **kw):
    content = str(freeze([sub, kw])).encode('utf-8', 'ignore')
    return hashlib.md5(content).hexdigest()


class Auto(object):
    '''
    A class for generating cache key automatically.
    parameters
    ----------
    prefix: string, the prefix of the key.
    '''
    def __init__(self, prefix=""):
        self.prefix = prefix

    def __call__(self, *sub, **kw):
        return '%s%s' % (self.prefix, to_hash(*sub, **kw))
