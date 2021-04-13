from flask import jsonify, request
# from db.db_session import create_session
# from db.__all_models import *
import config


@config.APP.route('/api/productions')
def get_productions():
    db_sess = create_session()
    resources = db_sess.query(Resource).all()
    names = [i.name for i in resources]
    patterns = eval(open('static/core/resources.txt',
                         'r', encoding='utf8').read())
    for pattern in patterns:
        if pattern['name'] not in names:
            new_resource = Resource()
            new_resource.apply_pattern(pattern)
            db_sess.add(new_resource)
            db_sess.commit()

    names = [i['name'] for i in patterns]
    for resource in resources:
        if resource['name'] not in names:
            db_sess.delete(resource)
            db_sess.commit()

    productions = db_sess.query(Production).all()
    users = db_sess.query(Users).all()
    for production in productions:
        if production.is_outdated():
            db_sess.delete(production)
        elif production.is_completed():
            production.on_complete(users)
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
    production.start_production(user)
    return jsonify({
        'result': 'OK'
    })
