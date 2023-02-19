from tkinter import *
import backend


def get_selected_row(event): #this function gets the highted row in the listbox and displays it
    try:
        
        global selected_row
        index=books_info.curselection()[0]#gets the index of the selected row
        
        selected_row=books_info.get(index)#stores the row as a list in the varaible
    
    
        e1.delete(0,END)#this section makes sure the entry box is empty before inserting
        e1.insert(END,selected_row[1])
    
        e2.delete(0,END)
        e2.insert(END,selected_row[2])
    
        e3.delete(0,END)
        e3.insert(END,selected_row[3])
    
        e4.delete(0,END)
        e4.insert(END,selected_row[4])
    
    except IndexError:
        pass
    
    

def view_command():
    books_info.delete(0,END)
    for i in backend.view():
        books_info.insert(END,i)

def search_command():
    books_info.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        books_info.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    books_info.delete(0,END)
    books_info.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    backend.delete(selected_row[0])

def update_command():
    backend.update(selected_row[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    








window=Tk()
window.title("Bookstore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

books_info=Listbox(window,height=6,width=35)
books_info.grid(row=2,column=0,rowspan=6,columnspan=2)

books_info.bind('<<ListboxSelect>>',get_selected_row)#executes the get_selected_row when thye row is highted

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
books_info.configure(yscrollcommand=sb1.set)
sb1.configure(command=books_info.yview)

sb2=Scrollbar(window,orient='horizontal')
sb2.grid(row=7,column=0,columnspan=2)
books_info.configure(xscrollcommand=sb2.set)
sb2.configure(command=books_info.xview)


b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="close",width=12,command=window.destroy)
b6.grid(row=7,column=3)



















window.mainloop()