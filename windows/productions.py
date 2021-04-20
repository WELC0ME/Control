from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/productions', methods=['POST'])
def get_productions():
    # получение ппроизводств
    _request = {
        'token': request.json.get('token', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'result': 'incorrect token'
        })
    db_sess = create_session()

    productions = db_sess.query(Production).all()
    for production in productions:
        if production.is_outdated():
            db_sess.delete(production)
            db_sess.commit()
        production.on_complete()
        db_sess.merge(production)
        db_sess.commit()

    patterns = eval(open('static/core/productions.txt',
                         'r', encoding='utf8').read())
    users = len(db_sess.query(User).all())
    for pattern in patterns:
        productions = db_sess.query(Production).filter(
            Production.type_id == pattern['type']).all()
        count = len(productions) if productions else 0
        while count * pattern['count'] < users:
            new_production = Production()
            new_production.apply_pattern(pattern)
            db_sess.add(new_production)
            db_sess.commit()
            productions = db_sess.query(Production).filter(
                Production.type_id == pattern['type']).all()
            count = len(productions) if productions else 0
    productions = db_sess.query(Production).all()
    return {
        'result': 'OK',
        'data': [production.to_dict() for production in productions]
    }


@config.APP.route('/api/promote_production', methods=['POST'])
def promote_production():
    _request = {
        'token': request.json.get('token', ''),
        'production_id': request.json.get('production_id', ''),
        'param': request.json.get('param', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'result': 'incorrect token'
        })
    db_sess = create_session()
    production = db_sess.query(Production).get(_request['production_id'])
    user = db_sess.query(User).get(config.USER_ID)
    res = user.promote(production)
    if res:
        return jsonify(res)
    production.promote(_request['param'])
    db_sess.merge(user)
    db_sess.commit()
    db_sess.merge(production)
    db_sess.commit()
    return jsonify({
        'result': 'OK'
    })


@config.APP.route('/api/start_production', methods=['POST'])
def start_production():
    # начать производство
    _request = {
        'token': request.json.get('token', ''),
        'production_id': request.json.get('production_id', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'result': 'incorrect token'
        })
    db_sess = create_session()
    production = db_sess.query(Production).get(_request['production_id'])
    user = db_sess.query(User).get(config.USER_ID)
    res = user.start(production)
    if res:
        return jsonify(res)
    production.start(user)
    db_sess.merge(user)
    db_sess.commit()
    db_sess.merge(production)
    db_sess.commit()
    return jsonify({
        'result': 'OK'
    })
