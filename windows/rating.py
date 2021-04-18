from flask import jsonify
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/rating')
def rating():
    db_sess = create_session()
    users = db_sess.query(User).order_by(
        User.to_dict()['resources']['coins']).all()
    return jsonify({
        'rating': [user.to_dict() for user in users],
    })
