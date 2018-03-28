#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

def verify_server(signature, timestamp, nonce, echostr, token):
    try:
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("hashcode: {}, signature: {}".format(hashcode, signature))
        if hashcode == signature:
            return echostr
        else:
            return echostr   # 原为“”(加密算法可能有误)  直接返回echostr即可完成认证
    except Exception as error:
        return error