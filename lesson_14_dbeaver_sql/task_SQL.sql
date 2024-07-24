-- Создайте студента (student)
insert into students (name, second_name, group_id) VALUES ('Vladimir', 'Shambaryan', 1)
SELECT * FROM students WHERE second_name = 'Shambaryan' and name = 'Vladimir'
DELETE FROM students WHERE id = 1473


-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
insert into books (title, taken_by_student_id) values ('Python', '1474'), ('Pytest', '1474'), ('XPATH', '1474')
SELECT * FROM books WHERE taken_by_student_id = 1474
DELETE FROM books WHERE id = 1474



-- Создайте группу (group) и определите своего студента туда
insert into `groups` (title, start_date, end_date) values ('QA testers', '2024-04-01', '2024-07-01')
SELECT * FROM `groups` WHERE id = 1480
DELETE FROM `groups` WHERE id = 1479


-- Обновление записи студента, присваивая ему новую группу
update students
-- Устанавливаем значение group_id для студента
set group_id = (
    -- Подзапрос для получения id группы с названием 'QA testers' и соответствующими датами начала и окончания
    select id from `groups`
    where title = 'QA testers' and start_date = '2024-04-01' and end_date = '2024-07-01'
)
-- Условие обновления: обновляем только запись студента с id '1474'
where id = '1474'




-- Создайте несколько учебных предметов (subjects)
insert into subjets (title) values ('JavaScript'), ('Postman')
SELECT * FROM subjets WHERE id = 1919
DELETE FROM subjets WHERE id = 1917




-- Создайте по два занятия для каждого предмета (lessons)
insert into lessons (title, subject_id) values ('JavaScript', '1918'),('Functions', '1918')
insert into lessons (title, subject_id) values ('Postman', '1919'), ('Autotests in Postman', '1919')
SELECT * FROM lessons WHERE subject_id = 1918
DELETE FROM lessons WHERE subject_id = 1913



-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
insert into marks (value, lesson_id, student_id) values ('9', '4330', '1474'), ('8', '4331', '1474')
insert into marks (value, lesson_id, student_id) values ('9.5', '4332', '1474'), ('10', '4333', '1474')
SELECT * FROM marks WHERE lesson_id = 4331
DELETE FROM marks  WHERE lesson_id = 4329


-- Все оценки студента
-- Выбираем имя, фамилию студента, значение оценки и ID занятия
select students.name, students.second_name, marks.value, marks.lesson_id
from students
-- Соединяем таблицу marks с таблицей students по полю student_id
left join marks on students.id = marks.student_id
-- Фильтруем результаты, чтобы выбрать записи только для студента с именем "Vladimir" и фамилией "Shambaryan"
where name = 'Vladimir'
and second_name = 'Shambaryan'


-- Все книги, которые находятся у студента
-- Выбираем имя, фамилию студента и название книги
select students.name, students.second_name, books.title
from students
-- Соединяем таблицу books с таблицей students по полю taken_by_student_id
left join books on students.id = books.taken_by_student_id
-- Фильтруем результаты, чтобы выбрать записи только для студента с именем "Vladimir" и фамилией "Shambaryan"
where students.name = 'Vladimir'
and students.second_name = 'Shambaryan'


-- Для вашего студента выведит всё
-- Выбираем имя и фамилию студента, название группы, даты начала и окончания группы, название предмета,
-- название урока, ID предмета, оценку студента, ID урока и название книги
select students.name, students.second_name, `groups`.title, `groups`.start_date, `groups`.end_date,
       subjets.title, lessons.title, lessons.subject_id, marks.value, marks.lesson_id, books.title
from students
-- Соединяем таблицу `groups` с таблицей students по полю group_id
left join `groups` on students.group_id = `groups`.id
-- Соединяем таблицу marks с таблицей students по полю student_id
left join marks on students.id = marks.student_id
-- Соединяем таблицу lessons с таблицей marks по полю lesson_id
left join lessons on marks.lesson_id = lessons.id
-- Соединяем таблицу subjets с таблицей lessons по полю subject_id
left join subjets on lessons.subject_id = subjets.id
-- Соединяем таблицу books с таблицей students по полю taken_by_student_id
left join books on students.id = books.taken_by_student_id
-- Фильтруем результаты, чтобы выбрать записи только для студента с ID
where student_id = '1474'



