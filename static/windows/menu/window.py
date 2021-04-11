# from flask import jsonify
# from db.db_session import create_session
# from db.__all_models import *
import config


@config.APP.route('/api/current_user')
def current_user():
    pass
    # db_sess = create_session()
    # user = db_sess.query(User).filter(
    #     User.get_id() == config.USER_ID).first()
    # return jsonify({
    #     'authorized': True if user else False,
    #     'nickname': user.nickname if user else '',
    # })

