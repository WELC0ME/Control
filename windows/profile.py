from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/profile', methods=["POST"])
def profile():
    _request = {
        'token': request.json.get('token', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'result': 'incorrect token'
        })
    db_sess = create_session()
    user = db_sess.query(User).get(config.USER_ID)
    return jsonify({
        'result': 'OK',
        'user': user.to_dict() if user else {'authorized': False}
    })
    # авторизация пользователя


@config.APP.route('/api/logout', methods=["POST"])
def logout():
    _request = {
        'token': request.json.get('token', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'result': 'incorrect token'
        })
    config.USER_ID = -1
    return jsonify({
        'result': 'OK'
    })
