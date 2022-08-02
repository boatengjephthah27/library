from tkinter import *
import appbackend



# creating functions
def show():
    t_lbox.delete(0, END)
    for row in appbackend.print_it():
        t_lbox.insert(END, row)
        
def search_for():
    t_lbox.delete(0, END)
    for row in appbackend.search(title.get(), author.get(), year.get(), page.get()):
        t_lbox.insert(0,END)
        
  












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
t_entry = Entry(app, borderwidth=3, textvariable=t)
t_entry.grid(row=0,column=1, sticky=NSEW)

y = StringVar()
y_entry = Entry(app, borderwidth=3, textvariable=y)
y_entry.grid(row=1,column=1, sticky=NSEW)

a = StringVar()
a_entry = Entry(app, borderwidth=3, textvariable=a)
a_entry.grid(row=0,column=3, sticky=NSEW)

p = StringVar()
p_entry = Entry(app, borderwidth=3, textvariable=p)
p_entry.grid(row=1,column=3, sticky=NSEW)

# creating a listbox
t_lbox = Listbox(app, width=28)
t_lbox.grid(padx=3, pady=5, row=2, column=0, columnspan=2, rowspan=6, sticky=NSEW)

# creating a scrollbar
svbar = Scrollbar(app)
svbar.grid(row=2, column=2, rowspan=6, sticky=NSEW)
# shbar = Scrollbar(app, orient=HORIZONTAL)
# shbar.grid(row=8, column=0, columnspan=3, sticky=NSEW)

# configuring the listbox and scrollbar
t_lbox.configure(yscrollcommand=svbar.set)
# t_lbox.configure(xscrollommand=shbar.set)
svbar.configure(command=t_lbox.yview)
# shbar.configure(command=t_lbox.xview)


# creating buttons
viewb = Button(app, text='View', width=15, command=show,).grid(row=2,column=3, sticky=NSEW)
searchb = Button(app, text='Search Entry', width=15, command=search_for,).grid(row=3,column=3, sticky=NSEW)
addb = Button(app, text='Add Entry', width=15).grid(row=4,column=3, sticky=NSEW)
updateb = Button(app, text='Update', width=15).grid(row=5,column=3, sticky=NSEW)
deleteb = Button(app, text='Delete', width=15).grid(row=6,column=3, sticky=NSEW)
closeb = Button(app, text='Close', width=15).grid(row=7,column=3, sticky=NSEW)




app.mainloop()









