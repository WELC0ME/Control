import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
import os

SqlAlchemyBase = dec.declarative_base()

__factory = None


def create_session() -> Session:
    global __factory

    if __factory:
        return __factory()

    engine = sa.create_engine('postgresql' + os.environ['DATABASE_URL'][8:],
                              echo=False)

    # for local debug
    # engine = sa.create_engine('sqlite:///test.db?check_same_thread=False',
    #                           echo=False)

    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)

    return __factory()
