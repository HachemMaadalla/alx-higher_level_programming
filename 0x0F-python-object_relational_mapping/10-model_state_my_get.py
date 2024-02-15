#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
"""
    Module that performs MySQL query through MySQLAlchemy.
"""
if __name__ == "__main__":
    for c in sys.argv[4]:
        if c == ';':
            exit()

    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                            sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3])

    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if state is not None:
        print(state.id)
    else:
        print('Not found')

    session.close()
