import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class ProductionsToUsers(SqlAlchemyBase):
    # модель для связи пользователей и производств
    __tablename__ = 'productions_to_users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    production_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('productions.id'))
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'))
    time = sqlalchemy.Column(sqlalchemy.Integer)

    production = orm.relation("Production")
    user = orm.relation("User")
    # для связи с другими таблицами
