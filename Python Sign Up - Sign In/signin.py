from tkinter import *

window = Tk()
window.title("SingIN Form")
window.geometry('450x200')
window.configure(background = "#7913ed");
head = Label(window ,text = "LOGIN HERE", bg="#8da832",font='Helvetica 15 bold').grid(row = 0,column = 1)

c = Label(window ,text = "Email Id:",bg="#7913ed",font='Helvetica 10 bold',fg="white" ).grid(row = 3,column = 0)
 
pas = Label(window ,text = "Password:",bg="#7913ed",font='Helvetica 10 bold',fg="white").grid(row = 6,column = 0)
 

c1 = Entry(window,width=60).grid(row = 3,column = 1)

pas1=Entry(window, show="*",width=60).grid(row = 6,column = 1)

   
btn = Button(window ,text="Login", bg="#d3e3d3",width=50).grid(row=8,column=1)
btn2 = Button(window ,text="Cancel", bg="red",width=50).grid(row=9,column=1)

window.mainloop()
