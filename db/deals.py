import sqlalchemy
from .db_session import SqlAlchemyBase


class Deal(SqlAlchemyBase):
    __tablename__ = 'deals'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    author = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey('users.id'),
                               nullable=True)

    input_resource = sqlalchemy.Column(sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey('resources.id'),
                                       nullable=True)

    input_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    output_resource = sqlalchemy.Column(sqlalchemy.Integer,
                                        sqlalchemy.ForeignKey('resources.id'),
                                        nullable=True)

    output_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
