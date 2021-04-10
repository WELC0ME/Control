from flask import jsonify
from window import WindowBase
import config


class WindowProfile(WindowBase):

    def __init__(self):
        super().__init__('profile')

    @staticmethod
    @config.APP.route('/api/user')
    def user():
        pass
