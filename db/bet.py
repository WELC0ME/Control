import sqlalchemy
import random
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from config import *


class Bet(SqlAlchemyBase):
    __tablename__ = 'bets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    sides = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Integer))
    created = sqlalchemy.Column(sqlalchemy.String)
    life_time = sqlalchemy.Column(sqlalchemy.String)
    result = sqlalchemy.Column(sqlalchemy.Integer)
    coefficient = sqlalchemy.Column(sqlalchemy.Integer)
    users = orm.relation("UsersToBets", back_populates='bet')

    def generate(self):
        self.created = TIME.now()
        self.life_time = TIME.random_time(
            '00:00:01:00:00', '00:00:05:00:00'
        )
        self.sides = [0, 0]

    def is_completed(self):
        return TIME.compare(self.created, self.life_time)

    def on_completed(self):
        roll = random.randint(0, self.sides[0] + self.sides[1])
        self.result = 1 if roll > self.sides[0] else 0
        if self.sides[self.result] != 0:
            self.coefficient = 1 + self.sides[
                (self.result % 2) + 1] / self.sides[self.result]
        else:
            self.coefficient = 1
        for association in self.users:
            association.user.on_bet_complete(self, association)

    def to_dict(self):
        return {
            'id': self.id,
            'sides': self.sides,
            'created': self.created,
            'life_time': self.life_time,
            'result': self.result,
            'coefficient': self.coefficient,
        }
