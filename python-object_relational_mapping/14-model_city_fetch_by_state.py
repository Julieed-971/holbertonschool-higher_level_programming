#!/usr/bin/python3
"""Print all City objects from database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(
        State, State.id == City.state_id).order_by(asc(City.id)).all()

    for city, state in cities:
        print("{} ({}) {}".format(state.name, city.id, city.name))

    session.close()
