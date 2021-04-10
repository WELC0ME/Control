from flask import jsonify
from window import WindowBase
import config


class WindowSignUp(WindowBase):

    def __init__(self):
        super().__init__('sign_up')

    @staticmethod
    @config.APP.route('/api/sign_up')
    def sign_up():
        pass
