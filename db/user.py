import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from .__all_models import UsersToBets


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)

    resources = orm.relation('UsersToResources', back_populates='user')
    bets = orm.relation("UsersToBets", back_populates='user')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def start_production(self, production):
        pass

    def promote(self, productions):
        self.resources[productions] -= 1

    def do_bet(self, bet, side, value):
        for i in self.resources:
            if i.resource.name == 'coin':
                if int(i.number) < int(value):
                    return {
                        'result': 'not enough money',
                    }
                else:
                    i.number = int(i.number) - int(value)
                    break
        self.bets.append(UsersToBets(
            user_id=self.id,
            bet_id=bet.id,
            side=side,
            value=int(value)
        ))
        return {
            'result': 'OK',
        }

    def on_bet_complete(self, result, coefficient, association):
        if result == association.side:
            for i in self.resources:
                if i.resource.name == 'coin':
                    i.number += int(association.value) * coefficient
                    break

    def to_dict(self):
        return {
            'authorized': True,
            'nickname': self.nickname,
            'resources': {
                i.resource.name: i.number for i in self.resources
            },
        }

    def apply_pattern(self, pattern):
        self.nickname = pattern['nickname']
        self.password = generate_password_hash(pattern['password'])
