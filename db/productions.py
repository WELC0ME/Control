import sqlalchemy
from .db_session import SqlAlchemyBase


class Production(SqlAlchemyBase):
    __tablename__ = 'productions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    type = sqlalchemy.Column(sqlalchemy.Integer,
                             sqlalchemy.ForeignKey('production_types.id'),
                             nullable=True)
    input_resources = sqlalchemy.Column(sqlalchemy.Integer,
                                        sqlalchemy.ForeignKey(
                                            'resource_list.id'), nullable=True)
    output_resources = sqlalchemy.Column(sqlalchemy.Integer,
                                         sqlalchemy.ForeignKey(
                                             'resource_list.id'),
                                         nullable=True)

    working_time = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    workload = sqlalchemy.Column(
        sqlalchemy.ARRAY((sqlalchemy.Integer, sqlalchemy.String)))

    created = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    life_time = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    action_price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    action_shift = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'input_resources': self.input_resources,
            'output_resources': self.output_resources,
            'created': self.created,
            'life_time': self.life_time,
            'action_price': self.action_price,
            'action_shift': self.action_shift,
            'workload': self.workload
        }

    def promote(self):  # добавление жизни
        pass

    def apply_pattern(self, data):
        self.type = data['type']
        self.input_resources = data['input']
        self.name = data['title']
        self.action_price = data['interaction_price']
        self.action_shift = data['interaction_time_shift']

    def is_outdated(self):
        pass

    def is_completed(self, user):
        pass

    def on_completed(self, user):
        pass
