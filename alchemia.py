import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print(sqlalchemy.__version__)

engine = create_engine('sqlite:///college.db', echo=True)
# engine = create_engine('mysql:///user:pass@localhost/college', echo=True)
# print(engine.driver)

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)


# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_student = Student(name='Ania', lastname='Kowalska')
session.add(new_student)

session.commit()

students = session.query(Student).all()
for s in students:
    print(f"ID: {s.id}, name: {s.name}, lastname: {s.lastname}")

