#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import hashlib
import logging

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