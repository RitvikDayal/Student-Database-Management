from tkinter import *
import tkinter.messagebox
import veiw_client_directory as veiwBook
import Add_client as addn


def addNewClient():
    addn.addClient()
    root.destroy()

def veiwDirectory():
    root.destroy()
    veiwBook.showAll()

def iExit():
    iExit = tkinter.messagebox.askyesno("Client Directory","Confirm if you want to exit.")
    if iExit > 0:
        root.destroy()
        return

root = Tk()
root.title('Client Directory')
root.config(bg='grey')
root.resizable(width=False, height=False)
root.geometry('400x500+500+0')

#========================================================================================================================

'''-------------------------TITLE_LABEL-------------------------------------------------------'''
fr1 = Frame(root, bg='grey', height=150)
fr1.pack()

titleLabel = Label(fr1, text='Client Directory', font=('arial',28,'bold'),
                   bg='grey', bd=8, fg='black')
titleLabel.grid(columnspan=4)

invi_fr1 = Frame(root, bg='grey', height=60)
invi_fr1.pack()
'''----------------------VEIW_CLIENT_DIRECTORY------------------------------------------------'''

fr2 = Frame(root, bg='grey', height=50)
fr2.pack()
veiwBook_btn = Button(fr2, text='Veiw Clients Directory',
                      font=('arial',14,'bold'), bd=10,
                      fg='black', bg='white', command=veiwDirectory)
veiwBook_btn.grid(columnspan=4)


invi_fr2 = Frame(root, bg='grey', height=40)
invi_fr2.pack()
'''--------------------------SEARCH_CLIENT----------------------------------------------------'''

fr3 = Frame(root, bg='grey', height=50)
fr3.pack()
searchBook_btn = Button(fr3, text='Search Clients',
                      font=('arial',14,'bold'), bd=10,
                      fg='black', bg='white')
searchBook_btn.grid(columnspan=4)

invi_fr3 = Frame(root, bg='grey', height=40)
invi_fr3.pack()
'''----------------------ADD_NEW_CLIENT_BUTTON------------------------------------------------'''

fr4 = Frame(root, bg='grey', height=50)
fr4.pack()
newContact_btn = Button(fr4, text='Add new client',
                      font=('arial',14,'bold'), bd=10,
                      fg='black', bg='white', command=addNewClient)
newContact_btn.grid(columnspan=4)

invi_fr4 = Frame(root, bg='grey', height=40)
invi_fr4.pack()
'''--------------------------EXIT_BUTTON------------------------------------------------------'''

fr5 = Frame(root, bg='grey', height=50)
fr5.pack()
exit_btn = Button(fr5, text='Exit',
                      font=('arial',14,'bold'), bd=10,
                      fg='black', bg='white', command=iExit)
exit_btn.grid(columnspan=4)
'''-------------------------------------------------------------------------------------------'''
#========================================================================================================================
root.mainloop()
