import os
from flask import Flask
from importlib import import_module
import config
from config import *

config.APP = Flask(__name__)


@config.APP.route('/<name>')
def handler(name):
    base_template = open('static/base.html', 'r', encoding='utf8').read()
    base_app = open('static/app.js', 'r', encoding='utf8').read()
    current_template = open(WINDOWS_PATH + name + '/template.html',
                            'r', encoding='utf8').read()
    current_app = open(WINDOWS_PATH + name + '/app.js',
                       'r', encoding='utf8').read()
    base_app = base_app.replace('__METHODS__', current_app)
    base_template = base_template.replace('__TEMPLATE__', current_template)
    base_template = base_template.replace('__SCRIPT__', base_app)
    return base_template


if __name__ == '__main__':
    for window in os.listdir(WINDOWS_PATH):
        import_module('.'.join([
            WINDOWS_PATH[:-1].replace('/', '.'), window, 'window'
        ]))
    # config.APP.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    config.APP.run()
