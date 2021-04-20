from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/rating', methods=["POST"])
def rating():
    # рейтинг пользователей
    _request = {
        'token': request.json.get('token', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
    db_sess = create_session()
    users = db_sess.query(User).all()
    users = sorted(users, key=lambda user: user.to_dict()['resources']['coin'],
                   reverse=True)
    return jsonify({
        'result': 'OK',
        'data': [user.to_dict() for user in users],
    })
    # возвращает результат
