import sqlalchemy
from .db_session import SqlAlchemyBase


class Deal(SqlAlchemyBase):
    __tablename__ = 'deals'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    author = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey('users.id'))

    input_resource = sqlalchemy.Column(sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey('resources.id'))

    input_number = sqlalchemy.Column(sqlalchemy.Integer)

    output_resource = sqlalchemy.Column(sqlalchemy.Integer,
                                        sqlalchemy.ForeignKey('resources.id'))

    output_number = sqlalchemy.Column(sqlalchemy.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'input_resource': self.input_resource,
            'input_number': self.input_number,
            'output_resource': self.output_resource,
            'output_number': self.output_number
        }
