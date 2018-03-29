# -*- coding: utf-8 -*-
import json
import logging
from utils.api import APIResult, api_wrap
from flask import Blueprint, request
import xml.etree.ElementTree as et
from . import ops

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
        print(signature, timestamp, nonce, echostr)
        ret = ops.verify_server(signature, timestamp, nonce, echostr, token)
        return  ret
    if request.method == "POST":
        xmldata = request.stream.read()
        xml_rec = et.fromstring(xmldata)
        ToUserName = xml_rec.find('ToUserName').text
        fromUser = xml_rec.find('FromUserName').text
        MsgType = xml_rec.find('MsgType').text
        Content = xml_rec.find('Content').text
        logger.info("POST ToUserName: %s, fromUser: %s, MsgType: %s, Content: %s" %
                    (ToUserName, fromUser, MsgType, Content))

        return ops.reply_msg(MsgType, fromUser, ToUserName, Content)


# Create your views here.
