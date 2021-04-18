import sqlalchemy
import random
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from config import *


class Bet(SqlAlchemyBase):
    __tablename__ = 'bets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    side_01 = sqlalchemy.Column(sqlalchemy.Integer)
    side_02 = sqlalchemy.Column(sqlalchemy.Integer)
    created = sqlalchemy.Column(sqlalchemy.Integer)
    life_time = sqlalchemy.Column(sqlalchemy.Integer)
    coefficient = sqlalchemy.Column(sqlalchemy.Integer)
    users = orm.relation("UsersToBets", back_populates='bet')

    def generate(self):
        self.created = TIME.now()
        self.life_time = TIME.random(86400, 432000)
        self.coefficient = round(random.random(), 2)
        self.side_01 = 0
        self.side_02 = 0

    def is_complete(self):
        return TIME.get(int(self.created)) > int(self.life_time)

    def on_complete(self):
        roll = random.randint(0, self.side_01 + self.side_02)
        if roll >= self.side_01:
            result = 0
        else:
            result = 1
        for association in self.users:
            association.user.on_bet_complete(result, self.coefficient,
                                             association)

    def to_dict(self):
        return {
            'side_01': self.side_01,
            'side_02': self.side_02,
            'coefficient': self.coefficient,
            'time': TIME.view(
                int(self.life_time) - TIME.get(int(self.created))),
        }
