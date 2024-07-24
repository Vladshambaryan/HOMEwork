import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'))

cursor = db.cursor()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
destination_path = os.path.join(homework_path, "homework", "hw_data", "data.csv")


with open(destination_path, "r", newline="") as data_file:
    reader = csv.reader(data_file)
    next(reader)

    for row in reader:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

        query = """
        SELECT students.name, students.second_name, `groups`.title, books.title, subjets.title, lessons.title, marks.value
        FROM students
        JOIN `groups` ON students.group_id = `groups`.id
        JOIN books ON students.id = books.taken_by_student_id
        JOIN marks ON students.id = marks.student_id
        JOIN lessons ON marks.lesson_id = lessons.id
        JOIN subjets ON lessons.subject_id = subjets.id
        WHERE students.name = %s
        AND students.second_name = %s
        AND `groups`.title = %s
        AND books.title = %s
        AND subjets.title = %s
        AND lessons.title = %s
        AND marks.value = %s
        """
        values = (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)
        data = cursor.execute(query, values)

        data_result = cursor.fetchall()

        if not data_result:
            print(f"Not found in DB: {row}")


db.close()