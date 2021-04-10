from flask import jsonify
from window import WindowBase
import config


class WindowSignIn(WindowBase):

    def __init__(self):
        super().__init__('sign_in')

    @staticmethod
    @config.APP.route('/api/sign_in')
    def sign_in():
        pass
