import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from .__all_models import UsersToBets


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    resources = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey('resource_list.id'),
                                  nullable=True)

    notifications = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    bets = orm.relation("UsersToBets", back_populates='user')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def do_bet(self, bet, side, value):
        if self.resources['coins'] < value:
            return {
                'error': 'not money'
            }
        self.resources['coins'] -= value
        self.bets.append(UsersToBets(
            user_id=self.id,
            bet_id=bet.id,
            side=side,
            value=value
        ))

    def on_bet_complete(self, bet, association):
        if bet.result == association.side:
            self.resources['coins'] += association.value * bet.coefficient
