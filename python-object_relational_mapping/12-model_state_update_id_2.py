#!/usr/bin/python3
"""
Update State object with the name 'New Mexico'
by ID from the database hbtn_0e_6_usa
as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    update_state = update(State).where(State.id == 2).values(name='New Mexico')
    session.execute(update_state)
    session.commit()

    session.close()
