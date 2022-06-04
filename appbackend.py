import sqlite3


def create_table():
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookshelf (id INTEGER PRIMARY KEY, Book_title VARCHAR, Author TEXT, Year INT, Page INT)" )
    connect.commit()
    connect.close()

create_table()


def add(title, author, year, page):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("INSERT INTO bookshelf VALUES (NULL,?,?,?,?)", (title, author, year, page))
    connect.commit()
    connect.close()

def update(id, title, author, year, page):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("UPDATE bookshelf SET title=?, author=?, year=?, page=? WHERE id=?",(title, author, year, page, id))
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

def close():
    pass


def search(title, author, year, page):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM bookshelf WHERE title=? OR author=? OR year=? OR page=?", (title, author, year, page))
    row = cur.fetchall()
    connect.close()
    return row






























add('Cinderella', 'Shakespear', 1998, 5)







