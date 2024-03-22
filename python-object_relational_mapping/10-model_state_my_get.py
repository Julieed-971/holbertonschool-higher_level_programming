#!/usr/bin/python3
"""
Print State objectwith the name passed
as argument from the database hbtn_0e_6_usa
"""
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

    states_found = session.query(State).filter(State.name == sys.argv[4]).all()

    if states_found:
        for state in states_found:
            print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
