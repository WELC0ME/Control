from flask import jsonify, url_for
from window import WindowBase
# from db.db_session import create_session
# from db.__all_models import *
import config


class WindowMenu(WindowBase):

    def __init__(self):
        super().__init__('menu')

    @staticmethod
    @config.APP.route('/api/authorized')
    def authorized():
        db_sess = create_session()
        user = db_sess.query(User).filter(
            User.get_id() == config.USER_ID).first()
        return jsonify({
            'authorized': True if user else False,
            'user_name': user.name if user else '',
        })


WindowMenu()
