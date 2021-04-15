import sqlalchemy
from .db_session import SqlAlchemyBase


class Production(SqlAlchemyBase):
    __tablename__ = 'productions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

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

    working_time = sqlalchemy.Column(sqlalchemy.Time, nullable=True)

    created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    life_time = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)

    action_price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    action_shift = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
