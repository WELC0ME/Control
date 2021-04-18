from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/admin/init', methods=["POST"])
def init():
    _request = {
        'token': request.json.get('token', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
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

    types = db_sess.query(ProductionType).all()
    names = [i.name for i in types]
    patterns = eval(open('static/core/productions.txt',
                         'r', encoding='utf8').read())
    for pattern in patterns:
        if pattern['name'] not in names:
            new_type = ProductionType()
            new_type.apply_pattern(pattern)
            db_sess.add(new_type)
            db_sess.commit()

    return jsonify({
        'result': 'OK'
    })
