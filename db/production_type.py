import sqlalchemy
from .db_session import SqlAlchemyBase


class ProductionType(SqlAlchemyBase):
    # типы производства
    __tablename__ = 'production_types'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String)

    def apply_pattern(self, pattern):
        # добавление данных об объекте
        self.name = pattern['title']
