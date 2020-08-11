import random
import tkinter as tk
from tkinter import Label,Entry,Button,Listbox,Scrollbar,Frame,VERTICAL,END,Toplevel,StringVar
from PIL import ImageTk, Image
import sqlite3
import sys
con = sqlite3.connect('chatbot.db')
 
 

class Chatbot(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master=master
        self.load_gui()
        with con:
            cur=con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Chatbote(Chat TEXT)")
           
    def load_gui(self):
        self.label2=Label(self.master, text ='Hi! I am Sita, your personal chatbot.',font=("Phosphate",35),bg='#5cd9db',fg='#5670C2' )
        self.label2.grid(row=2,column=1)
        self.label1=Label(self.master, text ='How can I help you?',font=("Phosphate",35),bg='#5cd9db',fg='#5670C2' )
        self.label1.grid(row=3,column=1)
        self.button1=Button(self.master,text='Lets chat',highlightbackground='#5670C2',width= 12,height=2,command = lambda: self.Letchat())
        self.button_quit = Button(self.master, text="No,Chat Later",width=12,height=2,highlightbackground='#5670C2',command = lambda: self.close())
        self.my_img = ImageTk.PhotoImage(Image.open("/Users/saimilind/Desktop/python practice/chatbot.png"))
        self.my_label = Label(root, image=self.my_img,background="#5cd9db")
        self.my_label.grid(row=1,column=1,sticky='nsew')

   
        self.button_quit.grid(row=5,column=1)
        self.button1.grid(row=4,column=1)

    def close(self):
        self.master.destroy()
        
    def Letchat(self):
        x1=Toplevel(root)
        
        self.chat1 = Entry(x1,width=53, text = '')
        self.chat1.grid(row = 14,column = 1, sticky = 's')
        x1.geometry('1013x700')
        self.button = Button(x1,highlightbackground='#75B79E', width = 10,height = 2, text="Chat",command = lambda: self.add())
        self.button.grid(row = 15, column = 1, sticky = 'w')
        self.scrollbar1 = Scrollbar(x1, orient = VERTICAL)
        self.lstList1 = Listbox(x1, background="#F1FCFC", fg="black",selectbackground="#b9cced",highlightcolor="Red", width=54,height=36,exportselection = 0, yscrollcommand = self.scrollbar1.set)
        self.lstList1.place(relx = 0.5, rely = 0.5, anchor="e")
        self.lstList1.grid(row=0,column=1)
        self.scrollbar1.config(command = self.lstList1.yview)
        self.scrollbar1.grid(row = 1, column =13,rowspan = 7,columnspan=12 ,sticky = 'nes')
        self.lstList1.grid( row=0,column=1,rowspan = 5, columnspan = 10,sticky = 'nw')
        self.greetings={'hola':'hello','namaste':'salaam','how u doing':'good','whats up':'chill','kaise ho':'mast','aur kya haal':'bole to jhakaaaaas','where am i':'u are in mumbai','whats my location':'u are in navi mumabi','what is this place':'u r in the city of dreams','is this hell':'u r in kharghar'}
        self.image = Image.open('/Users/saimilind/Desktop/python practice/smartphone.png')
        self.image = self.image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(x1,bg='#2A7886', image = self.photo)
        self.label.image = self.photo
        self.label.grid(row=3)
        x1.configure(background='#2A7886')
        
    def add(self):
        for item in [self.chat1.get()]:
            if item=='hola' or item=='namaste' or item=='how u doing' or item=='whats up' or item=='kaise ho' or item=='aur kya haal' or item=='where am i' or item=='whats my location' or item=='what is this place':
                self.lstList1.insert(END,str('HUMAN:'),str(self.chat1.get()),str('ROBO:'),str(self.greetings.get(str(self.chat1.get()))))
            else:
                return 0
        with con:
            cur = con.cursor()    
            cur.execute("INSERT INTO Chatbote VALUES(?)",(str(self.chat1.get()),))
            cur.execute("INSERT INTO Chatbote VALUES(?)",(str(self.greetings.get(self.chat1.get())),))
            cur.execute("SELECT * FROM Chatbote")
            rows=cur.fetchall()
            print(rows)

 
         
            
if __name__=="__main__":
    root = tk.Tk()
    c=Chatbot(root)
  

    root.configure(background="#5cd9db")
    root.geometry('640x700')
    root.title("Sita- The ChatBot")
    root.mainloop()
