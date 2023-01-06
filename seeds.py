from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from models import Grade, Student, Group, Teacher, Subject
from datetime import datetime
import faker
from random import randint

engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    NUMBER_TEACHERS = randint(3, 5)
    NUMBER_GROUPS = 3
    NUMBER_ESTIMATES = 20
    subjects_list = [
        "History",
        "Maths",
        "Biology",
        "Geography",
        "Physics",
        "Philosophy",
    ]
    fake_data = faker.Faker()

    def get_data() -> tuple():
        fake_teachers = []
        for _ in range(NUMBER_TEACHERS):
            fake_teachers.append(fake_data.name())
        teachers = []
        for teacher in fake_teachers:
            teachers.append((teacher,))

        subjects = []
        for sub in subjects_list:
            subjects.append((sub, randint(1, NUMBER_TEACHERS)))

        grades = []
        for std in range(1, 31):
            days = []
            subj = {}
            for _ in range(0, randint(1, NUMBER_ESTIMATES)):
                day = randint(1, 31)
                days.append(day)
                days.sort()
            for d in days:
                subj.update({d: randint(1, 6)})
            for key, value in subj.items():
                est_date = datetime(2022, 12, key).date()
                grades.append((std, value, randint(1, 10), est_date))

        return teachers, subjects, grades

    def insert_data_to_db(teachers, subjects, grades) -> None:
        for g in range(1, 4):
            group = Group(group_number=g)
            for _ in range(1, 11):
                Student(student_name=fake_data.name(), group=group)
            session.add(group)

        for i in teachers:
            teacher = Teacher(teacher_name=i[0])
            session.add(teacher)

        for i in subjects:
            subject = Subject(subject_name=i[0], teacher_id=i[1])
            session.add(subject)

        for i in grades:
            grade = Grade(student_id=i[0], subject_id=i[1], grade=i[2], date_of=i[3])
            session.add(grade)

        session.commit()

    insert_data_to_db(*get_data())
