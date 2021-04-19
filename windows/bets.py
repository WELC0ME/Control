from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config
import random


@config.APP.route('/api/bets', methods=['POST'])
def get_bets():
    _request = {
        'token': request.json.get('token', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
    db_sess = create_session()
    bets = db_sess.query(Bet).all()
    for bet in bets:
        if bet.is_complete():
            bet.on_complete()
            db_sess.delete(bet)
            db_sess.commit()
    bets = db_sess.query(Bet).all()
    while len(bets) < random.randint(15, 25):
        new_bet = Bet()
        new_bet.generate()
        db_sess.add(new_bet)
        db_sess.commit()
        bets = db_sess.query(Bet).all()
    bets = db_sess.query(Bet).all()
    return jsonify({
        'result': 'OK',
        'data': [bet.to_dict() for bet in bets],
    })


@config.APP.route('/api/do_bet', methods=['POST'])
def do_bet():
    _request = {
        'token': request.json.get('token', ''),
        'bet_id': request.json.get('bet_id', ''),
        'side': request.json.get('side', ''),
        'value': request.json.get('value', ''),
    }
    if not config.check_token(_request['token']):
        return jsonify({
            'error': 'incorrect token'
        })
    db_sess = create_session()
    bet = db_sess.query(Bet).get(_request['bet_id'])
    user = db_sess.query(User).get(config.USER_ID)
    return jsonify(user.do_bet(
        bet,
        _request['side'],
        _request['value']
    ))
