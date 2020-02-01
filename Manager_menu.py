# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:38:04 2019

@author: Cyber Lord
"""
from tkinter import *
import tkinter.messagebox
import Add_Student as adds

bg_color = '#312d3d'


'''----------Functions--------------------'''
def addNewStudents():
    root.destroy()
    adds.addStudent()

def veiwDirectory():
    root.destroy()
    veiwBook.showAll()

def iExit():
    iExit = tkinter.messagebox.askyesno("Student Database Manager","Confirm if you want to exit.")
    if iExit > 0:
        root.destroy()
        return

'''-------------------------------Window Configuration----------------------------------------'''
root = Tk()
root.title('Student Database Manager')
root.iconbitmap(r'sdm_icon.ico')
root.config(bg=bg_color)
root.resizable(width=False, height=False)
root.geometry('400x500+500+0')

#========================================================================================================================

'''-------------------------TITLE_LABEL-------------------------------------------------------'''
fr1 = Frame(root, bg=bg_color, height=150)
fr1.pack()

titleLabel = Label(fr1, text='Student Database\nManager', font=('arial',22,'bold'),
                   bg=bg_color, bd=8, fg='#f8ffba')  #f8ffba:- title color, yellowish
titleLabel.grid(columnspan=4)

invi_fr1 = Frame(root, bg=bg_color, height=40)
invi_fr1.pack()
'''----------------------VEIW_Student_Database_Manager------------------------------------------------'''

fr2 = Frame(root, bg=bg_color, height=50)
fr2.pack()
veiwBook_btn = Button(fr2, text='Veiw Student Database',
                      font=('arial',14,'bold'), bd=10,
                      fg='black', bg='white', command=veiwDirectory)
veiwBook_btn.grid(columnspan=4)


invi_fr2 = Frame(root, bg=bg_color, height=40)
invi_fr2.pack()
'''--------------------------SEARCH_Students----------------------------------------------------'''

fr3 = Frame(root, bg=bg_color, height=50)
fr3.pack()
searchBook_btn = Button(fr3, text='Search Students',
                      font=('arial',14,'bold'), bd=10,
                      fg='black', bg='white')
searchBook_btn.grid(columnspan=4)

invi_fr3 = Frame(root, bg=bg_color, height=40)
invi_fr3.pack()
'''----------------------ADD_NEW_Students_BUTTON------------------------------------------------'''

fr4 = Frame(root, bg=bg_color, height=50)
fr4.pack()
newContact_btn = Button(fr4, text='Add new Students',
                      font=('arial',14,'bold'), bd=10,
                      fg='black', bg='white', command=addNewStudents)
newContact_btn.grid(columnspan=4)

invi_fr4 = Frame(root, bg=bg_color, height=40)
invi_fr4.pack()
'''--------------------------EXIT_BUTTON------------------------------------------------------'''

fr5 = Frame(root, bg=bg_color, height=50)
fr5.pack()
exit_btn = Button(fr5, text='Exit',
                      font=('arial',14,'bold'), bd=10,
                      fg='black', bg='white', command=iExit)
exit_btn.grid(columnspan=4)
'''-------------------------------------------------------------------------------------------'''
#========================================================================================================================
root.mainloop()



