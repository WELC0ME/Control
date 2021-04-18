import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import config


class Deal(SqlAlchemyBase):
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
        return {
            'author': self.user,
            'input_resource': self.input_resource.name,
            'input_number': self.input_number,
            'output_resource': self.output_resource.name,
            'output_number': self.output_number,
            'active': self.user_id != config.USER_ID,
        }

    def create(self, options, user):
        if options['input'] == options['output']:
            return {
                'result': 'same resources'
            }
        self.input_resource = options['input']
        self.output_resource = options['output']
        self.input_number = options['input_number']
        self.output_number = options['output_number']
        self.user_id = user.id
