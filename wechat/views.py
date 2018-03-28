# -*- coding: utf-8 -*-
import json
import logging
from utils.api import APIResult, api_wrap
from flask import Blueprint, jsonify, abort, make_response, request
from . import ops


@weixin_api.route('/', methods=['GET'])
def weixin():
    signature = request.args.get("signature","")
    timestamp = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    echostr = request.args.get("echostr", "")
    token = "hello2018"
    print(signature, timestamp, nonce, echostr)
    ret = ops.verify_server(signature, timestamp, nonce, echostr, token)
    return  ret

# Create your views here.
