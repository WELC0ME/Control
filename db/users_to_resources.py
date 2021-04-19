import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class UsersToResources(SqlAlchemyBase):
    # модель для связи пользователей и ресурсов
    __tablename__ = 'users_to_resources'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'))
    resource_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey('resources.id'))
    number = sqlalchemy.Column(sqlalchemy.Integer)

    user = orm.relation("User")
    resource = orm.relation("Resource")

    def create(self, user, resource_pattern):
        # создание
        self.user_id = user.id
        self.resource_id = resource_pattern['id']
        self.number = 0
