# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def weixin(request):
    signature = request.GET.get("signature","")
    return  HttpResponse(signature,content_type='application/json; charset=utf-8')

# Create your views here.
