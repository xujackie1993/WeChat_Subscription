#!/usr/bin/env python
# -*- coding: utf-8 -*-

#文本、图片、语言、视频、小视频、地理位置和链接，
# 所对应的MsgType分别为[text,image,voice,video,shortvideo,location,link]
text_str = "<xml>" \
           "<ToUserName><![CDATA[%s]]></ToUserName>" \
           "<FromUserName><![CDATA[%s]]></FromUserName>" \
           "<CreateTime>%s</CreateTime>" \
           "<MsgType><![CDATA[text]]>" \
           "</MsgType><Content><![CDATA[%s]]></Content>" \
           "</xml>"

img_str = "<xml>" \
          "<ToUserName><![CDATA[%s]]></ToUserName>" \
          "<FromUserName><![CDATA[%s]]></FromUserName>" \
          "<CreateTime>%s</CreateTime>" \
          "<MsgType><![CDATA[image]]></MsgType>" \
          "<Image><MediaId><![CDATA[%s]]></MediaId></Image>" \
          "</xml>"
