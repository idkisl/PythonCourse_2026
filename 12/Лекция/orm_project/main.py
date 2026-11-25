from sqlalchemy import select
from data.db_sessions import Base, engine, Session
from data.student import Student
from data.grade import Grade

# Создаём таблицы, если они ещё не существуют.
Base.metadata.create_all(engine)
session = Session()

# 1. Добавление студента и оценки
student = Student(name='Иван', surname='Иванов')
student.grades.append(Grade(mark=8))
session.add(student)
session.commit()
student_id = student.id

# 2. Получение всех студентов
students = session.scalars(select(Student)).all()
for person in students:
    print(person.id, person.name, person.surname)

# 3. Поиск по первичному ключу
student = session.get(Student, student_id)
print(student.name)

# 4. Фильтрация
students = session.scalars(
    select(Student).where(Student.surname == 'Иванов')
).all()
for person in students:
    print(person.name)

# 5. Изменение записи
student.name = 'Александр'
session.commit()

# 6. Получение связанных оценок
for grade in student.grades:
    print(grade.mark)

# 7. Удаление оценки (пример; раскомментируйте при необходимости)
# session.delete(student.grades[0])
# session.commit()

# 8. Удаление студента (сначала удаляем его оценки)
# for grade in student.grades:
#     session.delete(grade)
# session.flush()
# session.delete(student)
# session.commit()

session.close()
