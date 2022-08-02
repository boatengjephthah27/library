import sqlite3


def create_table():
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookshelf (id INTEGER PRIMARY KEY, Book_title VARCHAR, Author TEXT, Year INT, Page INT)" )
    connect.commit()
    connect.close()

create_table()


def add(Book_title, Author, Year, Page):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("INSERT INTO bookshelf VALUES (NULL,?,?,?,?)", (Book_title, Author, Year, Page))
    connect.commit()
    connect.close()

def update(id, Book_title, Author, Year, Page):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("UPDATE bookshelf SET Book_title=?, Author=?, Year=?, Page=? WHERE id=?",(Book_title, Author, Year, Page, id))
    connect.commit()
    connect.close()

def delete(Book_Title):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("DELETE FROM bookshelf WHERE Book_Title = ?", (Book_Title,))
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


def search(Book_title="", Author="", Year="", Page=""):
    connect = sqlite3.connect("library.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM bookshelf WHERE Book_title=? OR Author=? OR Year=? OR Page=?", (Book_title, Author, Year, Page))
    row = cur.fetchall()
    connect.close()
    return row


# add("Power of the Mind", "Pastor Chris Oyakilome", 2014, 5)
# add("Rich Dad Poor Dad", "Robert Kiyosaki", 2011, 12)
# add("The Rich Man in Babylon", "clement", 2018, 7)
# add("Sleeping Beauty", "Shakespear", 2015, 15)
# add("Snow White", "Shakespear", 2020, 32)

# print(search(Page="15"))

































