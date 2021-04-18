from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/stock_exchange', methods=['POST'])
def stock_exchange():
    _request = {
        'token': request.json.get('token', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
    db_sess = create_session()
    deals = db_sess.query(Deal).all()

    return {
        'result': 'OK',
        'data': [deal.to_dict() for deal in deals]
    }


@config.APP.route('/api/create', methods=['POST'])
def create():
    _request = {
        'token': request.json.get('token', ''),
        'input': request.json.get('input', ''),
        'output': request.json.get('output', ''),
        'input_number': request.json.get('input_number', ''),
        'output_number': request.json.get('output_number', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
    db_sess = create_session()
    user = db_sess.query(User).get(config.USER_ID)
    new_deal = Deal()

    res = new_deal.create(_request, user)
    if res:
        return jsonify(res)
    res = user.create_deal(new_deal)
    if res:
        return jsonify(res)

    db_sess.add(new_deal)
    db_sess.commit()
    return jsonify({
        'result': 'OK'
    })


@config.APP.route('/api/accept', methods=['POST'])
def accept():
    _request = {
        'token': request.json.get('token', ''),
        'deal_id': request.json.get('deal_id', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
    db_sess = create_session()
    deal = db_sess.query(Deal).get(_request['deal_id'])

    user = db_sess.query(User).get(config.USER_ID)
    author = db_sess.query(User).get(deal.user.id)

    res = user.send_deal(deal)
    if res:
        return jsonify(res)

    author.get_deal(deal)

    db_sess.delete(deal)
    db_sess.commit()
    return jsonify({
        'result': 'OK'
    })
