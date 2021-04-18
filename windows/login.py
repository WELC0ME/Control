from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/sign_in', methods=["POST"])
def sign_in():
    _request = {
        'token': request.json.get('token', ''),
        'nickname': request.json.get('nickname', ''),
        'password': request.json.get('password', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
    db_sess = create_session()
    user = db_sess.query(User).filter(
        User.nickname == _request['nickname']).first()
    if not user:
        return jsonify({
            'result': 'unknown nickname'
        })
    if not user.check_password(_request['password']):
        return jsonify({
            'result': 'incorrect password'
        })
    config.USER_ID = user.id
    user.get_energy()
    return jsonify({
        'result': 'OK',
        'user': user.to_dict(),
    })


@config.APP.route('/api/sign_up', methods=["POST"])
def sign_up():
    _request = {
        'token': request.json.get('token', ''),
        'nickname': request.json.get('nickname', ''),
        'password': request.json.get('password', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
    if len(_request['nickname']) < 4:
        return jsonify({
            'result': 'nickname too short'
        })
    if len(_request['password']) < 4:
        return jsonify({
            'result': 'password too short'
        })

    db_sess = create_session()
    user = db_sess.query(User).filter(
        User.nickname == _request['nickname']).first()
    if user:
        return jsonify({
            'result': 'user with same nickname is already exist'
        })
    user = User()
    user.apply_pattern(_request)
    db_sess.add(user)
    db_sess.commit()
    resource_patterns = eval(open('static/core/resources.txt',
                                  'r', encoding='utf8').read())
    for pattern in resource_patterns:
        users_to_resources = UsersToResources()
        users_to_resources.create(user, pattern)
        db_sess.add(users_to_resources)
        db_sess.commit()
    config.USER_ID = user.id
    user.get_energy()
    return jsonify({
        'result': 'OK',
        'user': user.to_dict(),
    })
