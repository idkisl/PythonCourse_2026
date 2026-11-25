from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .db_sessions import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    grades = relationship('Grade', back_populates='student')
