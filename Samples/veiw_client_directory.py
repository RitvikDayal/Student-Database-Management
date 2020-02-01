from tkinter import *
import pandas as pd

def showAll():

    name = 'Ritvik Dayal'
    add = '2/480,\nBudhhiviahr Colony\nAvasvikas Colony\nMoradabad'
    phn = 98374880059
    email = 'Ritvikr98@gmail.com'
    description = 'Future Data Scientist\nMIT B\'tech Student\nComputer Science Engineer '

    root1 = Tk()
    root1.title('Address Book')
    root1.config(bg='black')
    root1.geometry('1200x700+60+0')

    fr1 = Frame(root1)
    fr1.pack()
    titleLabel = Label(fr1, text='Contacts', font=('arial',30,'bold'),
                       bg='black', bd=8, fg='white')
    titleLabel.grid(columnspan=4)


    invi_fr1=Frame(root1, height=50, bg='black').pack()



    fr2 = Frame(root1, bg='black')
    fr2.pack()

    nameLabel = Label(fr2, text='Name: ', font=('arial',16,'bold'),
                      bg='black', fg='white', bd=8)
    nameLabel.grid(columnspan=2, sticky='W', padx=5, pady=5)

    name = Label(fr2, text=name,font=('arial', 14, 'italic'), width=30, 
                   bd=4)
    name.grid(row=0,column=2,columnspan=2, sticky='W', padx=5, pady=5)


    invi_fr2=Frame(fr2, width=250, bg='black')
    invi_fr2.grid(row=0, column=7)

    canvas = Canvas(fr2, width = 200, height = 200)      
    canvas.grid(row=0,column=8, sticky='S')     
    img = PhotoImage(file="pic.png")      
    canvas.create_image(100,100,image=img)  

    invi_fr3=Frame(root1, height=50, bg='black').pack()



    fr3 = Frame(root1, bg='black')
    fr3.pack()

    addLabel = Label(fr3, text='Address: ', font=('arial',16,'bold'),
                      bg='black', fg='white', bd=8)
    addLabel.grid(columnspan=2, sticky='NW', padx=5, pady=5)

    address = Label(fr3, text=add, font=('arial', 14, 'italic'),
                   width=30, height=5, bd=4)
    address.grid(row=0,column=3,columnspan=4,sticky='NW')

    invi_fr2=Frame(fr3, width=420, bg='black')
    invi_fr2.grid(row=0, column=7)

    invi_fr4=Frame(root1, height=50, bg='black').pack()


    fr4 = Frame(root1, bg='black')
    fr4.pack()

    phnLabel = Label(fr4, text='Phone no.: ', font=('arial',16,'bold'),
                      bg='black', fg='white', bd=8, justify='left')
    phnLabel.grid(columnspan=2, sticky='W', padx=5, pady=5)

    phnno = Label(fr4, width=30, text = phn, font=('arial',14,'italic'), bg='white',
                      fg='black', bd=4, relief='ridge')
    phnno.grid(row=0,column=2, columnspan=4)

    invi_fr2=Frame(fr4, width=100, bg='black')
    invi_fr2.grid(row=0, column=7)

    descLabel = Label(fr4, text='Professional Description:',
                      font=('arial',14,'bold'), bg='black', fg='white',
                      justify='left')
    descLabel.grid(row=0, column=8)

    emailLabel = Label(fr4, text='Email: ', font=('arial',16,'bold'),
                      bg='black', fg='white', bd=8, justify='left')
    emailLabel.grid(row=1,columnspan=2, sticky='W', padx=5, pady=5)

    email = Label(fr4, width=30, text=email, font=('arial',14,'italic'),
                  bg='white',fg='black', bd=4)
    email.grid(row=1,column=2, columnspan=4)

    invi_fr3=Frame(fr4, width=100, bg='black')
    invi_fr3.grid(row=1, column=7)

    profsnl_descr = Label(fr4, text=description,font=('arial', 14, 'italic'),
                          width=30, height=5, bd=4)
    profsnl_descr.grid(row=1,column=8,columnspan=4,sticky='NW')

    root1.mainloop()

