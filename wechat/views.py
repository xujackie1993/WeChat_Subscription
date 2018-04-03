# -*- coding: utf-8 -*-
import json
import logging
from utils.api import APIResult, api_wrap
from flask import Blueprint, request, make_response
from . import ops
from .dispatcher import *

logger = logging.getLogger(__name__)

weixin_api = Blueprint("weixin", __name__)

@weixin_api.route('/trans', methods=['GET', "POST"])
def weixin():
    if request.method == "GET":
        signature = request.args.get("signature","")
        timestamp = request.args.get("timestamp", "")
        nonce = request.args.get("nonce", "")
        echostr = request.args.get("echostr", "")
        token = "hello2018"
        logger.info("signature: %s, timestamp: %s, nonce: %s, echostr: %s",
                    signature, timestamp, nonce, echostr)
        ret = ops.verify_server(signature, timestamp, nonce, echostr, token)
        return  ret
    if request.method == "POST":
        xmldata = request.stream.read()
        dispatcher = MsgDispatcher(xmldata)
        data = dispatcher.dispatch()
        logger.info("response data: %s", data)
        response = make_response(data)
        response.content_type = "application/xml"
        return response