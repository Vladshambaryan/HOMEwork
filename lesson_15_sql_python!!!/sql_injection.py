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
# cursor.execute('SELECT * FROM students')
# data = cursor.fetchall()  # верни все результаты
# print(data)
# for student in data:
#     print(student['second_name'])


cursor.execute('SELECT * FROM students WHERE id = 1477')
data2 = cursor.fetchone() # верни 1 результат
print(data2)

# f"SELECT * FROM users WHERE user = '{user}' and password = '{passw}'"
query = "SELECT * FROM students WHERE name ={0} and second_name ={1}"
cursor.execute(query.format(input('name'), input('second_name')))
print(cursor.fetchall())



db.close()