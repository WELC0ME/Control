from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/productions')
def get_productions():
    db_sess = create_session()

    productions = db_sess.query(Production).all()
    users = db_sess.query(User).all()
    for production in productions:
        if production.is_outdated():
            db_sess.delete(production)
            db_sess.commit()
        for user in users:
            if production.is_completed(user):
                production.on_complete(user)
                db_sess.merge(production)
                db_sess.commit()

    patterns = eval(open('static/core/productions.txt',
                         'r', encoding='utf8').read())
    users = len(db_sess.query(User).all()) // 1000 + 1
    for pattern in patterns:
        productions = db_sess.query(Production).get(pattern['type'])
        adj = (users - len(productions) / pattern['count']) / pattern['count']
        for _ in range(int(adj)):
            new_production = Production()
            new_production.apply_pattern(pattern)
            db_sess.add(new_production)
            db_sess.commit()
    productions = db_sess.query(Production).all()
    return {
        'productions': [production.to_dict() for production in productions]
    }


@config.APP.route('/api/promote_production')
def promote_production():
    db_sess = create_session()
    production = db_sess.query(Production).get(request.json['production_id'])
    user = db_sess.query(User).get(config.USER_ID)
    user.promote(production, request.json['value'])
    production.promote(request.json['value'])
    return jsonify({
        'result': 'OK'
    })


@config.APP.route('/api/start_production')
def start_production():
    db_sess = create_session()
    production = db_sess.query(Production).get(request.json['production_id'])
    user = db_sess.query(User).get(config.USER_ID)
    user.start_production(production)
    return jsonify({
        'result': 'OK'
    })