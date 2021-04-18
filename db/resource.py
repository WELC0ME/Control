import sqlalchemy
from .db_session import SqlAlchemyBase


class Resource(SqlAlchemyBase):
    # класс ресурсов
    __tablename__ = 'resources'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)

    name = sqlalchemy.Column(sqlalchemy.String)

    def apply_pattern(self, data):
        # добавление данных об объекте
        self.id = data['id']
        self.name = data['name']
