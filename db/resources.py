import sqlalchemy
from .db_session import SqlAlchemyBase


class Resource(SqlAlchemyBase):
    __tablename__ = 'resources'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def apply_pattern(self, data):
        self.name = data['name']