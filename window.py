import config
from config import *


def make_request(name):
    @config.APP.route('/' + name)
    def wrapped():
        template = open(WINDOWS_PATH + name + '/template.html',
                        'r', encoding='utf8').read()
        return template.replace('__PATH__', 'windows/' + name)
    return wrapped


class WindowBase:

    def __init__(self, name):
        make_request(name)
