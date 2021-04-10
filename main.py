import os
from flask import Flask
from importlib import import_module
import config
from config import *

if __name__ == '__main__':
    config.APP = Flask(__name__, static_folder=WINDOWS_PATH)
    for window in os.listdir(WINDOWS_PATH):
        import_module('.'.join([WINDOWS_PATH[:-1], window, 'window']))
    # config.APP.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    config.APP.run()
