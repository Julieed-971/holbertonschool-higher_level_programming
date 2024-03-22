#!/usr/bin/python3
"""
Update State object with the name 'New Mexico'
by ID from the database hbtn_0e_6_usa
as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    delete_states = delete(State).where(State.name.like('%a%'))
    session.execute(delete_states)
    session.commit()

    session.close()
