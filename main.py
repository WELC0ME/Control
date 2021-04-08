from flask import Flask
import os
from config import *
from api import *

config.APP = Flask(__name__)


@config.APP.route('/')
def menu():
    return show_template('menu')


@config.APP.route('/rating')
def rating():
    return show_template('rating')


@config.APP.route('/productions')
def productions():
    return show_template('productions')


@config.APP.route('/stock_exchange')
def stock_exchange():
    return show_template('stock_exchange')


@config.APP.route('/sign_in')
def sign_in():
    return show_template('sign_in')


@config.APP.route('/sign_up')
def sign_up():
    return show_template('sign_up')


if __name__ == '__main__':
    config.APP.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
