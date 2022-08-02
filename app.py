from tkinter import *
import appbackend



# creating functions

def selected_rows(event):
    global selected_row
    index = t_lbox.curselection()[0]
    selected_row = t_lbox.get(index)
    t_entry.delete(0, END)
    t_entry.insert(END, selected_row[1])
    a_entry.delete(0, END)
    a_entry.insert(END, selected_row[2])
    y_entry.delete(0, END)
    y_entry.insert(END, selected_row[3])
    p_entry.delete(0, END)
    p_entry.insert(END, selected_row[4])
    # print(selected_row[0])

def show():
    t_lbox.delete(0, END)
    for row in appbackend.print_it():
        t_lbox.insert(END, row)
        
def search_for():
    t_lbox.delete(0, END)
    for row in appbackend.search(t.get(), a.get(), y.get(), p.get()):
        t_lbox.insert(END, row)
        
def add_up():
    appbackend.add(t.get(), a.get(), y.get(), p.get())
    t_lbox.delete(0, END)
    t_lbox.insert(END, "Book added!")

def update_():
    appbackend.update(selected_row[0], t.get(), a.get(), y.get(), p.get())
    t_entry.delete(0, END)
    a_entry.delete(0, END)
    y_entry.delete(0, END)
    p_entry.delete(0, END)
    t_lbox.delete(0, END)
    t_lbox.insert(END, "Book Updated!")
    
def delete_():
    appbackend.delete(selected_row[0])
    t_lbox.delete(0,END)
    t_lbox.insert(END, "Selected Book deleted!")

def close_():
    app.quit()



# Creating the frontend interface
app = Tk()
app.title('My Library')

# app.geometry('500x500')

# screen_width = app.winfo_screenwidth()
# screen_height = app.winfo_screenheight()
# window_height = 750
# window_width = 750
# width_center = int(screen_width/2 - window_width/2)
# height_center = int(screen_height/2 - window_height/2)
# window_position = app.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
# app.resizable(False, False)

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

# configuring the listbox and scrollbar
t_lbox.configure(yscrollcommand=svbar.set)
svbar.configure(command=t_lbox.yview)
t_lbox.bind('<<ListboxSelect>>', selected_rows)



# creating buttons
viewb = Button(app, text='View', width=15, command=show,).grid(row=2,column=3, sticky=NSEW)
searchb = Button(app, text='Search Entry', width=15, command=search_for,).grid(row=3,column=3, sticky=NSEW)
addb = Button(app, text='Add Entry', width=15, command=add_up).grid(row=4,column=3, sticky=NSEW)
updateb = Button(app, text='Update', width=15, command=update_).grid(row=5,column=3, sticky=NSEW)
deleteb = Button(app, text='Delete', width=15, command=delete_).grid(row=6,column=3, sticky=NSEW)
closeb = Button(app, text='Close', width=15, command=close_).grid(row=7,column=3, sticky=NSEW)




app.mainloop()









