#!/usr/bin/env python
# coding: utf-8

# # Project 1

# ## Library Book Management System

# In[1]:


from sqlite3 import *
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkmessagebox


# In[2]:


def Database():
    global conn,cursor
    conn=connect('LBMS.db')
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS lbms(book_title TEXT, author_name TEXT, year INTEGER, isbn INTEGER)")


# In[3]:


def display_records():
    present.delete(*present.get_children())
    Database()
    cursor.execute("SELECT * FROM lbms ")
    fetch = cursor.fetchall()
    for data in fetch:
        present.insert('',"end",values=(data[0],data[1],data[2],data[3]))
    conn.close()
    txt_result.config(text="These are the books available in the records", fg='red')


# In[4]:


def add():
    
    Database()
    
    if book_title.get(1.0,"end-1c")!="" and author_name.get(1.0,"end-1c")!="" and year.get(1.0,"end-1c")!="" and isbn.get(1.0,"end-1c")!="" :
        cursor.execute("INSERT INTO lbms VALUES(?,?,?,?)",(book_title.get(1.0,"end-1c").title(),author_name.get(1.0,"end-1c").title(), int(year.get(1.0,"end-1c")),int(isbn.get(1.0,"end-1c"))))
        conn.commit()
        delete()
        conn.close()
        txt_result.config(text="Book Details Inserted!",fg = 'green')
    else:
        txt_result.config(text='Please enter all the values to add the book', fg='red')
        delete()


# In[5]:


def search():
    
    present.delete(*present.get_children())
    Database()
    if str(book_title.get(1.0,"end-1c"))!="":
        name="'"+str(book_title.get(1.0,"end-1c").title())+"'"
        temp="SELECT * FROM lbms WHERE book_title ="+name
        cursor.execute(temp)
        fetch = cursor.fetchall()
        for data in fetch:
            present.insert('','end',values=(data[0],data[1],data[2],data[3]))
        txt_result.config(text="These are the books available in the records",fg='green')
        
    elif str(author_name.get(1.0,"end-1c"))!="":
        name="'"+str(author_name.get(1.0,"end-1c").title())+"'"
        temp ="SELECT * FROM lbms WHERE author_name ="+name
        cursor.execute(temp)
        fetch = cursor.fetchall()
        for data in fetch:
            present.insert('','end',values=(data[0],data[1],data[2],data[3]))
        txt_result.config(text="These are the books available in the records",fg='green')
        
    elif str(year.get(1.0,"end-1c"))!="":
        temp = "SELECT * FROM lbms WHERE year ="+str(year.get(1.0,"end-1c"))
        cursor.execute(temp)
        fetch = cursor.fetchall()
        for data in fetch:
            present.insert("","end",values=(data[0],data[1],data[2],data[3]))
        txt_result.config(text="These are the books available in the records",fg='green')
        
    elif str(isbn.get(1.0,"end-1c"))!="":
        temp = "SELECT * FROM lbms WHERE isbn ="+str(isbn.get(1.0,"end-1c"))
        cursor.execute(temp)
        fetch = cursor.fetchall()
        for data in fetch:
            present.insert("","end",values=(data[0],data[1],data[2],data[3]))
        txt_result.config(text="These are the books available in the records",fg='green')
        
    else:
        txt_result.config(text="Please enter atleast one entity to search!", fg='red')
    delete()
    conn.close()
    


# In[6]:


def issue_book():
    Database()
    selected_item=present.selection()
    if len(selected_item)>0:
        present.delete(selected_item)
        txt_result.config(text="The selected book is issued",fg='green')
        
    else:
        txt_result.config(text="Please select a book from the records available!",fg='red')
    delete()
    conn.close()


# In[7]:


def delete_book():
    Database()
    if book_title.get(1.0,"end-1c")== "" and author_name.get(1.0,"end-1c")=="" and year.get(1.0,"end-1c")=="" and isbn.get(1.0,"end-1c")== "":
        txt_result.config(text="Please enter all entries!", fg="red")
        delete()
        
    else:
        book='"'+str(book_title.get(1.0,"end-1c"))+'"'
        author='"'+str(author_name.get(1.0,"end-1c"))+'"'
        y = str(year.get(1.0,"end-1c"))
        i = str(isbn.get(1.0,"end-1c"))
        temp = "DELETE FROM lbms WHERE book_title = "+book+" and author_name = "+author+" and year = "+y+" and isbn = " +i
        cursor.execute(temp)
        conn.commit()
        txt_result.config(text="Book deleted successfully",fg='green')
        delete()
    conn.close()


# In[8]:



def delete():
 book_title.delete("1.0","end")
 author_name.delete("1.0","end")
 year.delete("1.0","end")
 isbn.delete("1.0","end")
     
 
def Exit():
 result = tkmessagebox.askquestion('Do you wanna exit the application?(Y/N)', icon='warning')
 if result == 'yes':
     win.destroy()
     exit()


# In[9]:


# Th GUI interface using the tkinter application


# In[ ]:



#-----------------------------------------------------------------------------------------------------
#Frame
#-----------------------------------------------------------------------------------------------------
win = Tk()
win.title("Library Management System")
win.geometry("900x400")
Top = Frame(win,width=900,height=50,bd=8,relief='raise',bg='red')
Top.pack(side=TOP)
Left = Frame(win,width=300,height=500,bd=8,relief='raise',bg='blue')
Left.pack(side=LEFT)
Right = Frame(win,width=800,height=500,bd=8,relief='raise',bg='yellow')
Right.pack(side=RIGHT)

Forms = Frame(Left,width=300,height=500,bd=8,relief='raise',bg='grey')
Forms.pack(side=TOP)

BUTTONS= Frame(Left,width=300,height=450,bd=8,relief='raise',bg='black')
BUTTONS.pack(side=BOTTOM)

txt_title = Label(Top, text= 'Library Book Management System',width = 1000,bg='black',fg='white',font='arial')
txt_title.pack(side=TOP)



book_title = Text(Forms,height=2,width=40)
book_title.grid(row=0,column=1)
author_name = Text(Forms,height=2,width=40)
author_name.grid(row=1,column=1)
year = Text(Forms,height=2,width=40)
year.grid(row=2,column=1)
isbn = Text(Forms,height=2,width=40)
isbn.grid(row=3,column=1)



#-----------------------------------------------------------------------------------------------------
#Labels
#-----------------------------------------------------------------------------------------------------


title_label = Label(Forms,text = "Book title:",font=('arial',14),bg='grey')
title_label.grid(row=0,stick='e')


author_label = Label(Forms, text = "Author:",font=('arial',14),bg='grey')
author_label.grid(row=1,stick='e')


year_label = Label(Forms, text = "Year:",font=('arial',14),bg='grey')
year_label.grid(row=2,stick='e')


isbn_label = Label(Forms, text = "ISBN:",font=('arial',14),bg='grey')
isbn_label.grid(row=3,stick='e')


txt_result = Label(Right)
txt_result.pack(side=BOTTOM)

#-----------------------------------------------------------------------------------------------------
#Buttons
#-----------------------------------------------------------------------------------------------------

display_btn = Button (BUTTONS, text='Display',command=display_records)
display_btn.pack(side=LEFT)

search_btn = Button(BUTTONS,text='Search',command=search)
search_btn.pack(side=LEFT)

add_btn = Button(BUTTONS,text='Add',command=add)
add_btn.pack(side=LEFT)

issue_btn = Button(BUTTONS,text='Issue', command=issue_book)
issue_btn.pack(side=LEFT)

delete_btn=Button(BUTTONS,text='Delete',command=delete_book)
delete_btn.pack(side=LEFT)

exit_btn = Button(BUTTONS,text='Exit',command=Exit)
exit_btn.pack(side=LEFT)

#-----------------------------------------------------------------------------------------------------
#Listbox
#-----------------------------------------------------------------------------------------------------
present = ttk.Treeview(Right)

scrollbary=Scrollbar(Right,orient=VERTICAL)
scrollbarx=Scrollbar(Right,orient=HORIZONTAL)

scrollbary.config(command=present.yview)
scrollbary.pack(side=RIGHT, fill=Y)

scrollbarx.config(command=present.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

present['columns']=("Book Title", "Author Name", "Publish Year", "ISBN No")
present.column('#0', stretch=NO,width=0)
present.column('Book Title',anchor=CENTER, width=125)
present.column('Author Name',anchor=CENTER, width=125)
present.column('Publish Year',anchor=CENTER, width=80)
present.column('ISBN No',anchor=CENTER, width=50)

present.heading('#0', text='',anchor=CENTER)
present.heading("Book Title", text = "Book Title", anchor=CENTER)
present.heading("Author Name", text = "Author Name", anchor=CENTER)
present.heading("Publish Year", text = "Publish Year", anchor=CENTER)
present.heading("ISBN No", text = "ISBN No", anchor=CENTER) 



present.pack()


win.mainloop()


# In[ ]:





# In[ ]:




