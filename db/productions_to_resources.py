import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class ProductionsToResources(SqlAlchemyBase):
    # модель для связи производств и ресурсов
    __tablename__ = 'productions_to_resources'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    production_id = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey('productions.id'))
    resource_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey('resources.id'))
    number = sqlalchemy.Column(sqlalchemy.Integer)
    direction = sqlalchemy.Column(sqlalchemy.Integer)

    production = orm.relation("Production")
    resource = orm.relation("Resource")
    # для связи с другими таблицами
