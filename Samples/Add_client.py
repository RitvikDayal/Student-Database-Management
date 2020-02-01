from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from validate_email import validate_email
import Store_info


def addClient():
    root = Tk()
    app = addingData(root)

class addingData:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Client")
        self.master.geometry('1200x700+60+0')
        self.master.config(bg = "black")
        self.fr1 = Frame(master, bg='black')
        self.fr1.pack()
        
        self.name = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.phn = StringVar()
        self.descrp = StringVar()
        
        #-------------------------------------------------------------------------------------------------------------------------
        self.titleLabel = Label(self.fr1, text='Add New Client', font=('arial',28,'bold'),
                       bg='black', bd=8, fg='white')
        self.titleLabel.grid(columnspan=4)
    
        self.invi_frfr1=Frame(self.master, height=50, bg='black').pack()
    
        self.fr2 = Frame(self.master, bg='black')
        self.fr2.pack()
    
        self.nameLabel = Label(self.fr2, text='Name: ', font=('arial',16,'bold'),
                          bg='black', fg='white', bd=8)
        self.nameLabel.grid(columnspan=2, sticky='W', padx=5, pady=5)
    
        self.nameEntry = Entry(self.fr2, width=30, font=('arial',14,'italic'), bg='white',
                          fg='black', textvariable=self.name, bd=4, relief='ridge')
        self.nameEntry.grid(row=0,column=2, columnspan=4)
    
        self.invi_frfr2=Frame(self.fr2, width=250, bg='black')
        self.invi_frfr2.grid(row=0, column=7)
    
        self.addpic_btn = Button(self.fr2, text='Add a picture', bg='grey', fg='white', command=self.select_image,
                            bd=5, font=('arial',12,'bold'))
        self.addpic_btn.grid(row=0,column=8, padx=10, pady=10)
    
        self.invi_fr3=Frame(self.master, height=50, bg='black').pack()
    
        self.fr3 = Frame(self.master, bg='black')
        self.fr3.pack()
    
        self.addLabel = Label(self.fr3, text='Address: ', font=('arial',16,'bold'),
                          bg='black', fg='white', bd=8)
        self.addLabel.grid(columnspan=2, sticky='NW', padx=5, pady=5)
    
        self.addEntry = Text(self.fr3, font=('arial', 14, 'italic'), width=30, height=5, 
                       bd=4)
        self.addEntry.grid(row=0,column=3,columnspan=4,sticky='NW')
    
        self.invi_fr2=Frame(self.fr3, width=420, bg='black')
        self.invi_fr2.grid(row=0, column=7)
    
        self.invi_fr4=Frame(self.master, height=50, bg='black').pack()
    
    
        self.fr4 = Frame(self.master, bg='black')
        self.fr4.pack()
    
        self.phnLabel = Label(self.fr4, text='Phone no.: ', font=('arial',16,'bold'),
                          bg='black', fg='white', bd=8, justify='left')
        self.phnLabel.grid(columnspan=2, sticky='W', padx=5, pady=5)
    
        self.phnEntry = Entry(self.fr4, width=30, font=('arial',14,'italic'), bg='white',
                          fg='black', textvariable=self.phn, bd=4, relief='ridge')
        self.phnEntry.grid(row=0,column=2, columnspan=4)
    
        self.invi_frfr2=Frame(self.fr4, width=100, bg='black')
        self.invi_frfr2.grid(row=0, column=7)
    
        self.descLabel = Label(self.fr4, text='Professional Description:',
                          font=('arial',14,'bold'), bg='black', fg='white',
                          justify='left')
        self.descLabel.grid(row=0, column=8)
    
        self.emailLabel = Label(self.fr4, text='Email: ', font=('arial',16,'bold'),
                          bg='black', fg='white', bd=8, justify='left')
        self.emailLabel.grid(row=1,columnspan=2, sticky='W', padx=5, pady=5)
    
        self.emailEntry = Entry(self.fr4, width=30, font=('arial',14,'italic'), bg='white',
                          fg='black', textvariable=self.email, bd=4, relief='ridge')
        self.emailEntry.grid(row=1,column=2, columnspan=4)
    
        self.invi_fr3=Frame(self.fr4, width=100, bg='black')
        self.invi_fr3.grid(row=1, column=7)
    
        self.descrEntry = Text(self.fr4, font=('arial', 14, 'italic'), width=30, height=5, 
                       bd=4)
        self.descrEntry.grid(row=1,column=8,columnspan=4,sticky='NW')
        
        self.invi_fr4=Frame(self.master, height=50, bg='black').pack()
        
        self.fr5 = Frame(self.master, bg='black')
        self.fr5.pack()
        
        self.sub_bttn = Button(self.fr5,text='ADD CLIENT', bg='green', fg='white', command=self.store_client,
                            bd=5, font=('arial',12,'bold') ).pack()
        
        self.master.mainloop()

        #-------------------------------------------------------------------------------------------------------------------------

    def select_image(self):
        self.file = ""
        self.file_path = filedialog.askopenfile()

    def store_client(self):
        self.n = self.name.get()
        self.add = self.address.get()
        self.p = int(self.phn.get())
        self.eml = self.email.get()
        self.dsrp = self.descrp.get()
        self.image_path = self.file_path.name
        
##        try:
##           self.val = int(self.p)
##        except ValueError:
##           tkinter.messagebox.showerror("Invalid Phone No.", "Enter a valid 10 digit Phone number.")
##           self.phn.set(0)
           
        if validate_email(self.eml) == False :
            tkinter.messagebox.showerror("Invalid Email", "Enter a valid Email address.")
            self.email.set("")
        else:
            Store_info.store_data(self.n, self.add, self.p, self.eml, self.dsrp, self.image_path)

