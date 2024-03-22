#!/usr/bin/python3
"""List all State object from database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_with_a = session.query(State).filter(
        State.name.like('%a')).order_by(asc(State.id)).all()

    for state in state_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
