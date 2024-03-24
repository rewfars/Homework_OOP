
import sqlite3

conn = sqlite3.connect('Database.db')
cursor = conn.cursor()


create_table_countries = '''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);
'''

conn.execute(create_table_countries)
conn.commit()


def additions_countries():
    insert_countries = '''
    INSERT INTO countries (title)
    VALUES (?);
    '''
    countries = [
        ('Россия',),
        ('Франция',),
        ('Япония',)
    ]
    cursor.executemany(insert_countries, countries)
    conn.commit()

#additions_countries()

create_table_cities = '''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area TEXT DEFAULT '0',
    country_id INTEGER REFERENCES countries(id)
);
'''

conn.execute(create_table_cities)
conn.commit()

def additions_cities():
    insert_cities = '''
    INSERT INTO cities (title, area, country_id)
    VALUES (?, ?, ?);
    '''
    cities = [
        ('Москва', '2511 км²', 1),
        ('Париж', '105,4 км²', 2),
        ('Токио', '2194 км²', 3),
        ('Сочи', '176,8 км²', 1),
        ('Кале', '33,5 км²', 2),
        ('Осака', '223 км²', 3),
        ('Владивосток', '331,2 км²', 1)
    ]
    cursor.executemany(insert_cities, cities)
    conn.commit()

#additions_cities()

create_table_employees = '''
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER INTEGER REFERENCES cities(id)
    );
    '''
conn.execute(create_table_employees)
conn.commit()

def additions_emploees():
    insert_employees = '''
    INSERT INTO employees (first_name, last_name, city_id)
    VALUES (?, ?, ?);
    '''
    employees = [
    ("Андрей", "Смирнов", 2),
    ("Джонни", "Синс", 2),
    ("Джон", "Уик", 1),
    ("Уил", "Смит", 7),
    ("Владимир", "Путин", 7),
    ("Анджелина", "Джоли", 3),
    ("Алекс", "Адамс", 1),
    ("Джеки", "Чан", 4),
    ("Лео", "Месси", 6),
    ("Садыр", "Жапаров", 3),
    ("Бред", "Питт", 5),
    ("Конор", "Макгрегор", 1),
    ("Наруто", "Узумаки", 7),
    ("Какаши", "Хатаке", 4)
]

    cursor.executemany(insert_employees, employees)
    conn.commit()

#additions_emploees()


def list_cities():
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]} - {city[1]}")

def employees_in_city(city_id):
    join_f = '''
    SELECT e.first_name, e.last_name, c.title AS city_name, c.area, co.title AS country_name
    FROM employees e
    JOIN cities c ON e.city_id = c.id
    JOIN countries co ON c.country_id = co.id
    WHERE c.id = ?
    '''
    cursor.execute(join_f, (city_id,))
    employees = cursor.fetchall()
    for employee in employees:
        print(f"ИМЯ: {employee[0]}, ФАМИЛИЯ: {employee[1]}, ГОРОД: {employee[2]}, ПЛОЩАДЬ: {employee[3]}, СТРАНА: {employee[4]}")


while 1:
    print("Введите id города что бы посмотреть список сотрудников")
    print("Из перечня городов ниже:")
    list_cities()

    input_id = int(input("Введите id города (для выхода из программы введите 0 ): "))

    if input_id == 0:
        break

    employees_in_city(input_id)

conn.close()