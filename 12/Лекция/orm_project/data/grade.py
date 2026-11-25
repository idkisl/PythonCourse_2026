from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .db_sessions import Base


class Grade(Base):
    __tablename__ = 'grade'
    __table_args__ = (CheckConstraint('mark BETWEEN 1 AND 10'),)

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    mark = Column(Integer, nullable=False)

    student = relationship('Student', back_populates='grades')
