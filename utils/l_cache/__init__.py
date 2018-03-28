#-*- encoding=utf-8 -*-
'''
Provide cache access idioms and patterns.
'''
from .cached import Cached
from .tinycache import TinyCache
from .lock import DummyLock, lock_maker

__all__ = ['Cached', 'TinyCache', 'DummyLock', 'lock_maker']
