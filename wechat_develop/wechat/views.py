# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import ops

def index(request):
    return HttpResponse("hello world")

def weixin(request):
    signature = request.GET.get("signature","")
    timestamp = request.GET.get("timestamp", "")
    nonce = request.GET.get("nonce", "")
    echostr = request.GET.get("echostr", "")
    token = "hello2018"
    print(signature, timestamp, nonce, echostr)
    ret = ops.verify_server(signature, timestamp, nonce, echostr, token)
    return  HttpResponse(ret, content_type='application/json; charset=utf-8')

# Create your views here.
