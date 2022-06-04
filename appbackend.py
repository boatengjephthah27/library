import sqlite3


def create_table():
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookshelf (id INTEGER PRIMARY KEY, Book_title VARCHAR, Author TEXT, Year INT, Page INT)" )
    connect.commit()
    connect.close()


create_table()


def add(book, quantity, price):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("INSERT INTO bookshelf VALUES (NULL,?,?,?,?)".format(book, quantity, price))
    connect.commit()
    connect.close()


def update(quantity, price, item):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("UPDATE bookshelf SET quantity = {}, price = {} WHERE book = {}".format(quantity, price, item))
    connect.commit()
    connect.close()


def delete(book):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("DELETE FROM bookshelf WHERE book = ?", (book,))
    connect.commit()
    connect.close()

def print_it():
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM bookshelf")
    row = cur.fetchall()
    connect.close()
    return row
