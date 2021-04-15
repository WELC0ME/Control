import sqlalchemy
from .db_session import SqlAlchemyBase


class ResourceList(SqlAlchemyBase):
    __tablename__ = 'resource_list'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    resource_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("resources.id"))

    number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
