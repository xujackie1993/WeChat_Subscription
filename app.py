#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask
import conf
import traceback

app = flask.Flask("flask-test")

from wechat.views import weixin_api

@app.errorhandler(Exception)
def handle_error(e):
    logger = logging.getLogger("error")
    logger.exception(e)
    if getattr(conf, 'DEBUG', False):
        resp = traceback.format_exception(type(e), e, e.__traceback__)
        print(resp)
    else:
        resp = "Things can go wrong will go wrong,"\
               + "so are servers."
    return flask.Response(response=resp, status=500)

app.register_blueprint(weixin_api, url_prefix="/weixin")
# app.register_blueprint(auth, url_prefix="/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
