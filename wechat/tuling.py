#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import conf

def get_turing_response(msg=""):
    url = "http://www.tuling123.com/openapi/api"
    response = requests.post(url=url, json={"key": conf.TULING.get("apikey"), "info": msg, "userid": 12345678})
    return json.loads(response.text)['text'] if response.status_code == 200 else ""

# 简单做下。后面慢慢来
def get_response_by_keyword(keyword):
    if '团建' in keyword:
        result = {"type": "image", "content": "3s9Dh5rYdP9QruoJ_M6tIYDnxLLdsQNCMxkY0L2FMi6HhMlNPlkA1-50xaE_imL7"}
    elif 'music' in keyword or '音乐' in keyword:
        musicurl='http://owhbcjbqh.bkt.clouddn.com/stillyoung.jpg'
        result = {"type": "music", "content": {"title": "80000", "description":"有个男歌手姓巴，他的女朋友姓万，于是这首歌叫80000", "url": musicurl, "hqurl": musicurl}}
    elif '关于' in keyword:
        items = [{"title": "关于我", "description":"喜欢瞎搞一些脚本", "picurl":"http://owhbcjbqh.bkt.clouddn.com/stillyoung.jpg", "url":"https://github.com/xujackie1993"},
                 {"title": "我的博客", "description":"收集到的，瞎写的一些博客", "picurl":"http://avatar.csdn.net/0/8/F/1_marksinoberg.jpg", "url":"http://blog.csdn.net/marksinoberg"},
                 {"title": "薛定谔的��", "description": "副标题有点奇怪，不知道要怎么设置比较好","picurl": "https://www.baidu.com/img/bd_logo1.png","url": "http://www.baidu.com"}
                 ]
        result = {"type": "news", "content": items}
    else:
        result = {"type": "text", "content": "可以自由进行拓展"}
    return result