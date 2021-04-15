import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Recource(SqlAlchemyBase):
    __tablename__ = 'resources'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)


