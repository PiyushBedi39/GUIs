"""
Program that stores Book Information
"""
from tkinter import *

from backend import Database

database=Database("books.db")

class Window(Tk):

    
    
    def __init__(self,window):
        
        self.window=window
        self.window.wm_title("Book Store")
        #self.window.minsize(500,400)
        
        l1=Label(window,text="Title")
        l1.grid(row=0,column=0,ipadx=15,ipady=10)

        l2=Label(window,text="Author")
        l2.grid(row=0,column=2,ipadx=15,ipady=10)

        l3=Label(window,text="Year")
        l3.grid(row=1,column=0,ipadx=15,ipady=10)

        l4=Label(window,text="ISBN")
        l4.grid(row=1,column=2,ipadx=15,ipady=10)

        self.title_value=StringVar()
        self.e1=Entry(window,textvariable=self.title_value)
        self.e1.grid(row=0,column=1)

        self.author_value=StringVar()
        self.e2=Entry(window,textvariable=self.author_value)
        self.e2.grid(row=0,column=3)

        self.year_value=StringVar()
        self.e3=Entry(window,textvariable=self.year_value)
        self.e3.grid(row=1,column=1)

        self.isbn_value=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_value)
        self.e4.grid(row=1,column=3)

        self.lbox=Listbox(window,height=6, width=40)
        self.lbox.grid(row=2,column=0,rowspan=8,columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.lbox.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.lbox.yview)

        self.lbox.bind('<<ListboxSelect>>',self.get_Selected_row)

        b1=Button(window,text="View All",width=15,command=self.view_command)
        b1.grid(row=2,column=3, ipadx=5)

        b2=Button(window,text="Search Entry",width=15,command=self.search_command)
        b2.grid(row=3,column=3, ipadx=5)

        b3=Button(window,text="Add Entry",width=15,command=self.insert_command)
        b3.grid(row=4,column=3, ipadx=5)

        b4=Button(window,text="Update",width=15,command=self.update_command)
        b4.grid(row=5,column=3, ipadx=5)

        b5=Button(window,text="Delete",width=15,command=self.delete_command)
        b5.grid(row=6,column=3, ipadx=5)

        b6=Button(window,text="Close",width=15,command=window.destroy)
        b6.grid(row=7,column=3, ipadx=5)
        
        
        
    def get_Selected_row(self,event):
        try:
            #global selected_tuple
            index=self.lbox.curselection()[0]    #[0] to get index,without [0], it returns a tuple
            self.selected_tuple=self.lbox.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.lbox.delete(0,END)
        for row in database.view():
            self.lbox.insert(END,row)

    def search_command(self):
        self.lbox.delete(0,END)
        for row in database.search(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()):
            self.lbox.insert(END,row)

    def update_command(self):
        try:
            database.update(self.selected_tuple[0], self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
            self.lbox.delete(0,END)
            self.lbox.insert(END, (self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()))
        except:
            self.lbox.delete(0,END)
            self.lbox.insert(END,"Please select a row to update")

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def insert_command(self):
        database.insert(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.lbox.delete(0,END)
        self.lbox.insert(END,(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()))


window=Tk()
Window(window)
window.mainloop() 
