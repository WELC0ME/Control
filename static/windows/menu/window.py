from flask import jsonify
# from db.db_session import create_session
# from db.__all_models import *
import config


@config.APP.route('/api/current_user')
def current_user():
    db_sess = create_session()
    user = db_sess.query(User).get(config.USER_ID)
    return jsonify({
        'user': user.to_dict() if user else {'authorized': False}
    })

