# coding:utf-8

import os
from flask import Flask

def create_app(test_config=None):
     # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    @app.route('/')
    def index():
        return "Y a quelqu'un ?"
    return app
