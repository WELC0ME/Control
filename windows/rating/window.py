from flask import jsonify
from window import WindowBase
import config


class WindowRating(WindowBase):

    def __init__(self):
        super().__init__('rating')

    @staticmethod
    @config.APP.route('/api/rating')
    def rating():
        pass
