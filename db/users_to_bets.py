import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class UsersToBets(SqlAlchemyBase):
    __tablename__ = 'users_to_bets'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'))
    bet_id = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey('bets.id'))
    side = sqlalchemy.Column(sqlalchemy.Integer)
    value = sqlalchemy.Column(sqlalchemy.Integer)

    user = orm.relation("User")
    bet = orm.relation("Bet")
