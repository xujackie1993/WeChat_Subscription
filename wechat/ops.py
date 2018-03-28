#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from .common import text_str, img_str

def verify_server(signature, timestamp, nonce, echostr, token):
    try:
        list = [token, timestamp, nonce]
        list.sort()
        s = list[0] + list[1] + list[2]
        hashcode = hashlib.sha1(s.encode("utf-8")).hexdigest()
        print("hashcode: {}, signature: {}".format(hashcode, signature))
        if hashcode == signature:
            return echostr
        else:
            return ''
    except Exception as error:
        return error

def reply_muban(type):
    if type == "text":
        return text_str
    elif type == "image":
        return img_str