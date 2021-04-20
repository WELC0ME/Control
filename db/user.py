import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from .__all_models import UsersToBets
from config import *


class User(SqlAlchemyBase):
    # класс пользователя
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)

    resources = orm.relation('UsersToResources', back_populates='user')
    bets = orm.relation("UsersToBets", back_populates='user')
    # связь с другими таблицами
    last_energy = sqlalchemy.Column(sqlalchemy.Integer)

    def get_energy(self):
        for i in self.resources:
            if i.resource.name == 'energy':
                add = (TIME.now() - int(self.last_energy)) // 3600
                i.number = int(i.number) + add
                self.last_energy = int(self.last_energy) + add * 3600
                break

    def check_password(self, password):
        # проверка пароля
        # пароль хранится в хэшированном виде
        return check_password_hash(self.password, password)

    def start(self, production):
        # начать производство
        print(self.to_dict())
        print(production.to_dict())
        for i in production.resources:
            if i.direction == 0:
                for k in self.resources:
                    if k.resource_id == i.resource_id:
                        if k.number < i.number:
                            return {
                                'result': 'not enough resources'
                            }
        for i in production.resources:
            if i.direction == 0:
                for k in self.resources:
                    if k.resource_id == i.resource_id:
                        k.number -= i.number

    def promote(self, production):
        # метод вычитает у пользователя деньги
        for i in self.resources:
            if i.resource.name == 'coin':
                if int(i.number) < int(production.action_price):
                    return {
                        'result': 'not enough money',
                    }
                else:
                    i.number = int(i.number) - int(production.action_price)
                    break

    def do_bet(self, bet, side, value):
        # сделать ставку
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
        ))  # добавление сделки
        return {
            'result': 'OK',
        }  # если ставка прошла успешно

    def on_bet_complete(self, result, coefficient, association):
        if result == association.side:
            for i in self.resources:
                if i.resource.name == 'coin':
                    i.number += int(association.value) * coefficient
                    break

    def on_production_complete(self, profit):
        for element in profit:
            for i in self.resources:
                if i.resource.id == element[0]:
                    i.number += element[1]

    def to_dict(self):
        # приводит к виду словаря
        return {
            'authorized': True,
            'nickname': self.nickname,
            'resources': {i.resource.name: i.number for i in self.resources
            },
        }

    def apply_pattern(self, pattern):
        # добавление данных о пользователе, данные передаются в функции
        self.nickname = pattern['nickname']
        self.password = generate_password_hash(pattern['password'])
        self.last_energy = int(TIME.now())

    def create_deal(self, deal):
        # начать сделку
        for i in self.resources:
            if i.resource.id == deal.input_resource.id:
                if int(i.number) < int(deal.input_number):
                    return {
                         'result': 'not enough resources'
                    }
                i.number = int(i.number) - int(deal.input_number)
                break

    def get_deal(self, deal):
        for i in self.resources:
            if i.resource.id == deal.output_resource.id:
                i.number += deal.output_number
                break

    def send_deal(self, deal):
        # отправить сделку
        for i in self.resources:
            if i.resource.id == deal.output_resource.id:
                if int(i.number) < int(deal.output_number):
                    return {
                         'result': 'not enough resources'
                    }
                i.number = int(i.number) - int(deal.output_number)
                break
        for i in self.resources:
            if i.resource.id == deal.input_resource.id:
                i.number = int(i.number) + int(deal.input_number)
                break
