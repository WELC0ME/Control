from flask import jsonify
from window import WindowBase
import config


class WindowProductions(WindowBase):

    def __init__(self):
        super().__init__('productions')

    @staticmethod
    @config.APP.route('/api/productions')
    def productions():
        pass

    @staticmethod
    @config.APP.route('/api/promote_production')
    def promote():
        pass

    @staticmethod
    @config.APP.route('/api/start_production')
    def start_production():
        pass
