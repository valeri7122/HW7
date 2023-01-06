from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    date_of = Column(DateTime, default=datetime.now())


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"))
    grades = relationship("Grade", cascade="all, delete", backref="student")


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_number = Column(Integer, nullable=False, unique=True)
    students = relationship("Student", cascade="all, delete", backref="group")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(50), nullable=False)
    subjects = relationship("Subject", cascade="all, delete", backref="teacher")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(50), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"))
    grades = relationship("Grade", cascade="all, delete", backref="subject")
