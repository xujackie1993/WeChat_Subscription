#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from functools import wraps

def time_it(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        print("This Func: {} cost {}".format(func.__name__), time.time()-st)
        return res
    return wrapper


