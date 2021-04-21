import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from config import *
import config
from .__all_models import ProductionsToResources
from .__all_models import ProductionsToUsers


class Production(SqlAlchemyBase):
    # класс роизводства
    __tablename__ = 'productions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    type_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('production_types.id'))
    type = orm.relation('ProductionType')

    resources = orm.relation('ProductionsToResources',
                             back_populates='production')
    users = orm.relation('ProductionsToUsers',
                         back_populates='production')
    # связь с другими таблицами

    working_time = sqlalchemy.Column(sqlalchemy.Integer)
    created = sqlalchemy.Column(sqlalchemy.Integer)
    life_time = sqlalchemy.Column(sqlalchemy.Integer)

    action_price = sqlalchemy.Column(sqlalchemy.Integer)
    action_shift = sqlalchemy.Column(sqlalchemy.Integer)

    def to_dict(self):
        # приводит к виду словаря все нобходимые данные об объекте
        return {
            'type': self.type.name,
            'input_resources': [[i.resource.name, i.number]
                                for i in self.resources if i.direction == 0],
            'output_resources': [[i.resource.name, i.number]
                                 for i in self.resources if i.direction == 1],
            'time': TIME.view(
                int(self.life_time) - TIME.get(int(self.created))),
            'working_time':  TIME.view(int(self.working_time)),
            'action_price': self.action_price,
            'action_shift':  TIME.view(int(self.action_shift)),
            'active': config.USER_ID not in [i.user.id for i in self.users]
        }

    def promote(self, side):
        # добавление времени жизни
        self.life_time += int(side) * self.action_shift

    def apply_pattern(self, data):
        # добавление данных
        self.type_id = data['type']
        for resource in data['input']:
            # добавление ресурсов
            self.resources.append(ProductionsToResources(
                production_id=self.id,
                resource_id=resource[0],
                number=resource[1],
                direction=0,
            ))
        for resource in data['output']:
            # добавление ресурсов
            self.resources.append(ProductionsToResources(
                production_id=self.id,
                resource_id=resource[0],
                number=resource[1],
                direction=1,
            ))
        self.working_time = TIME.random(*data['working_time'])
        self.created = TIME.now()
        self.life_time = TIME.random(*data['life_time'])
        self.action_price = data['interaction_price']
        self.action_shift = TIME.random(*data['interaction_time_shift'])

    def is_outdated(self):
        # проверяет сломалось ли производство
        return TIME.get(int(self.created)) > int(self.life_time)

    def on_complete(self):
        # дает ресурсы пользователя
        new_users = []
        for association in self.users:
            if TIME.get(association.time) > self.working_time:
                association.user.on_production_complete([
                    [i.resource.id, i.number]
                    for i in self.resources if i.direction == 1
                ])
            else:
                new_users.append(association)
        self.users = new_users[:]
        print(self.users)

    def start(self, user):
        # Начать производство
        self.users.append(ProductionsToUsers(
            production_id=self.id,
            user_id=user.id,
            time=TIME.now()
        ))
