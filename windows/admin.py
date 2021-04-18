from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/admin/create_resources', methods=["POST"])
def create_resources():
    _request = {
        'token': request.json.get('token', ''),
    }
    if not config.check_token(_request['token']):
        print('incorrect token')
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
