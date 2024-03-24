import sqlite3


def create_connection(name_db):
    conn = None
    try:
        conn = sqlite3.connect(name_db)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def additions_product(conn, products):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(conn, products):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_price(conn, products):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_products(conn):
    sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        products = cursor.fetchall()
        for product in products:
            print(product)
    except sqlite3.Error as e:
        print(e)


def all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        all_products = cursor.fetchall()
        for product in all_products:
            print(product)
    except sqlite3.Error as e:
        print(e)


def search_products(conn, title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + title + '%',))
        search_products = cursor.fetchall()
        for product in search_products:
            print(product)
    except sqlite3.Error as e:
        print(e)


connection = create_connection('hw.db')
sql_create_products_table = '''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price NUMERIC(10, 2) DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print('Successfully')

    create_table(connection, sql_create_products_table)

    additions_product(connection, ("жидкое мыло с запахом яблоко", 123.99, 10))
    additions_product(connection, ("мыло детское", 90.50, 20))
    additions_product(connection, ("шампунь для волос", 285.49, 15))
    additions_product(connection, ("зубная паста с мятой", 80.99, 30))
    additions_product(connection, ("гель для душа с алоэ вера", 140.99, 4))
    additions_product(connection, ("хозяйственное Мыло", 100.49, 12))
    additions_product(connection, ("очищающий лосьон для лица", 210.99, 18))
    additions_product(connection, ("крем для рук", 99.99, 22))
    additions_product(connection, ("кондиционер для волос", 250.49, 17))
    additions_product(connection, ("дезодорант в стике", 7.49, 28))
    additions_product(connection, ("мыло для бритья", 78.99, 14))
    additions_product(connection, ("шампунь для окрашенных волос", 13.99, 10))
    additions_product(connection, ("мыло для чувствительной кожи", 120.99, 16))
    additions_product(connection, ("крем для лица с SPF 30", 29.99, 8))
    additions_product(connection, ("губная помада", 50.49, 40))

    update_quantity(connection, (16, 14))
    update_price(connection, (75.83, 10))
    delete_products(connection, 11)

    select_products(connection)
    search_products(connection, 'мыло')
    all_products(connection)

    connection.close()