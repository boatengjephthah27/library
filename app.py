from tkinter import *
import sqlite3



def create_table():
    connect = sqlite3.connect("bookstore.db")
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookshelf (book TEXT, quantity INT, price REAL)" )
    connect.commit()
    connect.close()


def add(book, quantity, price):
    connect = sqlite3.connect("bookstore.db")
    cur = connect.cursor()
    cur.execute("INSERT INTO bookshelf VALUES ('{}','{}','{}')".format(book, quantity, price))
    connect.commit()
    connect.close()


def update(quantity, price, item):
    connect = sqlite3.connect("bookstore.db")
    cur = connect.cursor()
    cur.execute("UPDATE bookshelf SET quantity = {}, price = {} WHERE book = {}".format(quantity, price, item))
    connect.commit()
    connect.close()


def delete(book):
    connect = sqlite3.connect("bookstore.db")
    cur = connect.cursor()
    cur.execute("DELETE FROM bookshelf WHERE book = ?", (book,))
    connect.commit()
    connect.close()

def print_it():
    connect = sqlite3.connect("bookstore.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM bookshelf")
    row = cur.fetchall()
    connect.close()
    return row






# Creating the frontend interface
app = Tk()
# app.geometry('500x500')
app.title('My Library')

# creating labels
title_label = Label(app, text='Title').grid(row=0,column=0, sticky=NSEW)
year_label = Label(app, text='Year').grid(row=1, column=0, sticky=NSEW)
author_label = Label(app, text='Author').grid(row=0, column=2, sticky=NSEW)
page_label = Label(app, text='Page At').grid(row=1, column=2, sticky=NSEW)

# creating entry widgets
t = StringVar()
t_entry = Entry(app, borderwidth=3, textvariable=t).grid(row=0,column=1, sticky=NSEW)
y = StringVar()
y_entry = Entry(app, borderwidth=3, textvariable=y).grid(row=1,column=1, sticky=NSEW)
a = StringVar()
a_entry = Entry(app, borderwidth=3, textvariable=a).grid(row=0,column=3, sticky=NSEW)
p = StringVar()
p_entry = Entry(app, borderwidth=3, textvariable=p).grid(row=1,column=3, sticky=NSEW)


# creating a listbox
t_lbox = Listbox(app, width=28).grid(padx=3, pady=5, row=2, column=0, columnspan=2, rowspan=6, sticky=NSEW)

# creating a scrollbar
svbar = Scrollbar(app, orient=VERTICAL).grid(row=2, column=2, rowspan=6, sticky=NSEW)
shbar = Scrollbar(app, orient=HORIZONTAL).grid(row=8, column=0, columnspan=3, sticky=NSEW)

# configuring the listbox and scrollbar
t_lbox.config(yscrollcommand=svbar.set, xscrollommand=shbar.set)
svbar.config(command=t_lbox.yview)
shbar.config(command=t_lbox.xview)

# creating buttons
viewb = Button(app, text='View', width=15).grid(row=2,column=3, sticky=NSEW)
searchb = Button(app, text='Search Entry', width=15).grid(row=3,column=3, sticky=NSEW)
addb = Button(app, text='Add Entry', width=15).grid(row=4,column=3, sticky=NSEW)
updateb = Button(app, text='Update', width=15).grid(row=5,column=3, sticky=NSEW)
deleteb = Button(app, text='Delete', width=15).grid(row=6,column=3, sticky=NSEW)
closeb = Button(app, text='Close', width=15).grid(row=7,column=3, sticky=NSEW)






app.mainloop()









