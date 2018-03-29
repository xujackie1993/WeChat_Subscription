#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import mongoengine

DEBUG = True
MONGO={
    "test_data": {
        "name": "test_data",
        "host": "39.107.109.85",
        "port": 27017,
        'username': 'admin123',
        'password': '123',
        "authentication_source": "admin"
    }
}

AWS_PARAMS = {
    "aws_access_key_id": "AKIAJ6COJJRHOQYMNG4A",
    "aws_secret_access_key": "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",
    "region_name": "ap-northeast-1"
}

TEST_S3_BUCKET = "test_bucket"

TULING = {
    "apiKey": "4493f61135154c61a83fa0fb9ed69736",
    "userId": "4223abc71320c28d"
}

if globals().get('DEBUG'):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())


for alias, attrs in MONGO.items():
    mongoengine.register_connection(alias, **attrs)