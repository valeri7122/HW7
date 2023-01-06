from seeds import session
from models import Grade, Student, Group, Teacher, Subject
from sqlalchemy import func, desc


def select_1():
    return (
        session.query(
            Student.student_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2():
    return (
        session.query(
            Student.student_name,
            Subject.subject_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student, Subject)
        .group_by(Student.id, Subject.id)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )


def select_3():
    return (
        session.query(
            Subject.subject_name,
            Group.group_number,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student, Subject, Group)
        .group_by(Subject.id, Group.id)
        .all()
    )


def select_4():
    return (
        session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))
        .select_from(Grade)
        .all()
    )


def select_5():
    return (
        session.query(Teacher.teacher_name, Subject.subject_name)
        .select_from(Teacher)
        .join(Subject, isouter=True)
        .filter(Teacher.teacher_name == "Tony Wise")
        .all()
    )


def select_6():
    return (
        session.query(Student.student_name, Group.group_number)
        .select_from(Student)
        .join(Group)
        .filter(Group.group_number == 2)
        .order_by(Student.student_name)
        .all()
    )


def select_7():
    return (
        session.query(
            Grade.date_of,
            Student.student_name,
            Group.group_number,
            Subject.subject_name,
            Grade.grade,
        )
        .select_from(Grade)
        .join(Student, Group, Subject)
        .filter(Subject.subject_name == "History", Group.group_number == 3)
        .order_by(Student.student_name)
        .all()
    )


def select_8():
    return (
        session.query(
            Teacher.teacher_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .join(Subject)
        .group_by(Teacher.teacher_name)
        .order_by(Teacher.teacher_name)
        .all()
    )


def select_9():
    return (
        session.query(Student.student_name, Subject.subject_name)
        .select_from(Grade)
        .join(Subject, Student)
        .filter(Student.student_name == "Jason Lee")
        .group_by(Subject.subject_name)
        .order_by(Subject.subject_name)
        .all()
    )


def select_10():
    return (
        session.query(Student.student_name, Teacher.teacher_name, Subject.subject_name)
        .select_from(Grade)
        .join(Student, Subject)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(
            Student.student_name == "John Stout", Teacher.teacher_name == "Gene Wallace"
        )
        .group_by(Subject.subject_name)
        .order_by(Student.student_name)
        .all()
    )


if __name__ == "__main__":

    print(select_10())
