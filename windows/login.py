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
        print('incorrect token')
        return jsonify({
            'error': 'incorrect token'
        })
    db_sess = create_session()
    user = db_sess.query(User).filter(
        User.nickname == _request['nickname']).first()
    if not user:
        print('unknown nickname')
        return jsonify({
            'result': 'unknown nickname'
        })
    if not user.check_password(_request['password']):
        print('incorrect password')
        return jsonify({
            'result': 'incorrect password'
        })
    config.USER_ID = user.id
    print('OK')
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
        print('incorrect token')
        return jsonify({
            'error': 'incorrect token'
        })
    if len(_request['nickname']) < 4:
        print('nickname too short')
        return jsonify({
            'result': 'nickname too short'
        })
    if len(_request['password']) < 4:
        print('password too short')
        return jsonify({
            'result': 'password too short'
        })

    db_sess = create_session()
    user = db_sess.query(User).filter(
        User.nickname == _request['nickname']).first()
    if user:
        print('user with same nickname is already exist')
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
    return jsonify({
        'result': 'OK',
        'user': user.to_dict(),
    })
