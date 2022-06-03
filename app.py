import sqlite3

conn = sqlite3.connect("bookstore.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS bookshelf (book TEXT, quantity INT, price REAL)" )
conn.commit()
conn.close()


def add(book, quantity, price):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO bookshelf VALUES (?,?,?)", (book, quantity, price))
    conn.commit()
    conn.close()

m = input("book name: --  ")
n = int(input("book quantity: --  "))
v = float(input("book price: --  "))

add(m,n,v)

# def ()











