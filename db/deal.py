import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import config


class Deal(SqlAlchemyBase):
    # класс сделок
    __tablename__ = 'deals'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'))

    input_resource_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('resources.id'))

    input_number = sqlalchemy.Column(sqlalchemy.Integer)

    output_resource_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('resources.id'))

    output_number = sqlalchemy.Column(sqlalchemy.Integer)

    user = orm.relation('User')
    input_resource = orm.relation('Resource',
                                  foreign_keys=[input_resource_id])
    output_resource = orm.relation('Resource',
                                   foreign_keys=[output_resource_id])

    def to_dict(self):
        # приводит к виду словаря
        return {
            'author': self.user.nickname,
            'input_resource': self.input_resource.name,
            'input_number': self.input_number,
            'output_resource': self.output_resource.name,
            'output_number': self.output_number,
            'active': self.user_id != config.USER_ID,
        }

    def create(self, options, user, resources):
        # создать сделку, на вход - необходимые ресурсы и пользователь
        if options['input'] == options['output']:
            return {
                'result': 'same resources'
            }
        for resource in resources:
            if resource.name == options['input'].lower().replace(' ', '_'):
                self.input_resource_id = resource.id
                self.input_resource = resource
            if resource.name == options['output'].lower().replace(' ', '_'):
                self.output_resource_id = resource.id
                self.output_resource = resource
        try:
            self.input_number = int(options['input_number'])
            self.output_number = int(options['output_number'])
            if self.input_number <= 0 or self.output_number <= 0:
                return {
                    'result': 'incorrect number'
                }
        except ValueError:
            return {
                'result': 'not a number'
            }

        self.user_id = user.id
