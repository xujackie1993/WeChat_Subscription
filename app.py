#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask

app = flask.Flask("flask-test")
from wechat.views import weixin_api

app.register_blueprint(weixin_api, url_prefix="/weixin")
# app.register_blueprint(auth, url_prefix="/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
