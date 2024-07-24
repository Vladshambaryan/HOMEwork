import mysql.connector as mysql

# Подключение к базе данных
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# Создание курсора для выполнения SQL-запросов
cursor = db.cursor(dictionary=True)

# Создание студента (student)
cursor.execute("""
INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)
""", ('Vlad', 'Shambaryan', None))
# Получение идентификатора нового студента
student_id = cursor.lastrowid
print(f"Student id: {student_id}")

# Создание группы (group) и добавление студента в эту группу
group_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = ('QA', '2025-04-01', '2025-07-01')
cursor.execute(group_query, values)
# Получение идентификатора новой группы
group_id = cursor.lastrowid
print(f"Group id: {group_id}")

# Обновление записи студента, присваивая ему новую группу
query = "UPDATE students SET group_id = %s WHERE id = %s"
values = (group_id, student_id)
cursor.execute(query, values)

# Создание нескольких книг (books) и указание, что студент взял их
books_query = "insert into books (title, taken_by_student_id) values (%s, %s)"
cursor.executemany(
    books_query, [
        ('Python', student_id),
        ('Pytest', student_id),
        ('XPATH', student_id)
    ]
)

# Создание нескольких учебных предметов (subjects)
cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ['JavaScript'])
# Получение идентификатора нового предмета
subject_1_id = cursor.lastrowid
print(f"Subject 1 id: {subject_1_id}")

cursor.execute("INSERT INTO subjets (title) VALUES (%s)", ['Postman'])
# Получение идентификатора второго предмета
subject_2_id = cursor.lastrowid
print(f"Subject 2 id: {subject_2_id}")

# Создание по два занятия (lessons) для каждого предмета
cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('JavaScript', subject_1_id))
# Получение идентификатора первого занятия
lesson_1_id = cursor.lastrowid
print(f"JavaScript id: {lesson_1_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('Functions', subject_1_id))
# Получение идентификатора второго занятия
lesson_2_id = cursor.lastrowid
print(f"Functions id: {lesson_2_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('Postman', subject_2_id))
# Получение идентификатора третьего занятия
lesson_3_id = cursor.lastrowid
print(f"Postman id: {lesson_3_id}")

cursor.execute("INSERT INTO lessons (title, subject_id) values (%s, %s)", ('Autotests in Postman', subject_2_id))
# Получение идентификатора четвертого занятия
lesson_4_id = cursor.lastrowid
print(f"Autotests in Postman id: {lesson_4_id}")

# Поставить студенту оценки (marks) для всех созданных занятий
query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    query_marks, [
        ('10', lesson_1_id, student_id),
        ('8', lesson_2_id, student_id),
        ('9', lesson_3_id, student_id),
        ('10', lesson_4_id, student_id)
    ]
)

# Сохранить изменения в базе данных
db.commit()

# Вывести все оценки студента
print(':' * 50, 'Все оценки студента', ':' * 50)
student_grades = """
SELECT students.id, students.name, students.second_name, marks.lesson_id, marks.value
FROM students
JOIN marks ON students.id = marks.student_id
WHERE students.id = %s
"""
cursor.execute(student_grades, (student_id,))
# Печать всех оценок студента
for student_grade in cursor.fetchall():
    print(f"Student grades: {student_grade}")

# Вывести все книги, которые находятся у студента
print(':' * 50, 'Все книги, которые находятся у студента', ':' * 30)
student_books = """
SELECT students.id, students.name, students.second_name, books.title
FROM students
RIGHT JOIN books on students.id = books.taken_by_student_id
WHERE students.id = %s;
"""
cursor.execute(student_books, (student_id,))
# Печать всех книг, которые взял студент
for student_book in cursor.fetchall():
    print(f"Student books: {student_book}")

# Вывести всю информацию о студенте
print(':' * 50, 'Вся информация о студенте', ':' * 45)
student_info = """
SELECT students.id, students.name, students.second_name, `groups`.start_date,
`groups`.end_date, lessons.title, subjets.title, lessons.subject_id, marks.lesson_id,
marks.value, books.title
FROM students
join `groups` on students.group_id = `groups`.id
join marks on students.id = marks.student_id
join lessons on marks.lesson_id = lessons.id
join subjets on lessons.subject_id = subjets.id
join books on students.id = books.taken_by_student_id
WHERE students.id = %s;
"""
cursor.execute(student_info, (student_id,))
# Печать всей информации о студенте
for student_all in cursor.fetchall():
    print(f"Student all: {student_all}")

# Закрытие соединения с базой данных
db.close()
