#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import hashlib
import logging
from .common import text_str, img_str

logger = logging.getLogger(__name__)

def verify_server(signature, timestamp, nonce, echostr, token):
    try:
        list = [token, timestamp, nonce]
        list.sort()
        s = list[0] + list[1] + list[2]
        hashcode = hashlib.sha1(s.encode("utf-8")).hexdigest()
        logger.info("hashcode: {}, signature: {}".format(hashcode, signature))
        if hashcode == signature:
            return echostr
        else:
            return ''
    except Exception as error:
        return error

def reply_msg(type, fromuser, tousername, content):
    if type == "text":
        return text_str % (fromuser, tousername, int(time.time()), content)
    elif type == "image":
        return img_str % (fromuser, tousername, int(time.time()), content)