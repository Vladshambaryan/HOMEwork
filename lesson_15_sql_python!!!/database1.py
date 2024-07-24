import mysql.connector as mysql
#  ctrl+alt+l починит
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor(dictionary=True)

cursor.execute('SELECT * FROM students WHERE id = 1477')
data2 = cursor.fetchone() # верни 1 результат
print(data2)

cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Vlad', 'Sham', 1)")  # создаем
student_id = cursor.lastrowid
cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchone())

insert_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        ('vlad1', 'sh1', '1'),
        ('vlad2', 'sh2', '2')
        ]
)
db.commit()

db.close()
