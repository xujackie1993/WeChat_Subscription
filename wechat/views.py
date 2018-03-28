# -*- coding: utf-8 -*-
import json
import logging
from utils.api import APIResult, api_wrap
from flask import Blueprint, jsonify, abort, make_response, request
from time import time
import xml.etree.ElementTree as et
from . import ops

weixin_api = Blueprint("weixin", __name__)

@weixin_api.route('/', methods=['GET', "POST"])
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
        print("============")
        print(xmldata)
        xml_rec = et.fromstring(xmldata)
        ToUserName = xml_rec.find('ToUserName').text
        fromUser = xml_rec.find('FromUserName').text
        MsgType = xml_rec.find('MsgType').text
        Content = xml_rec.find('Content').text
        MsgId = xml_rec.find('MsgId').text
        return ops.reply_muban(MsgType) % (fromUser, ToUserName, int(time()), Content)


# Create your views here.
