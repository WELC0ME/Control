from flask import jsonify, request
from db.db_session import create_session
from db.__all_models import *
import config


@config.APP.route('/api/bets')
def bets():
    db_sess = create_session()
    bets = db_sess.query(Bet).all()
    return jsonify({
        'bets': [bet.to_dict() for bet in bets],
    })


@config.APP.route('/api/do_bet')
def do_bet():
    db_sess = create_session()
    bet = db_sess.query(Bet).get(request.json['bet_id'])
    user = db_sess.query(User).get(config.USER_ID)
    return jsonify(user.do_bet(
        bet,
        request.json['side'],
        request.json['value']
    ))
