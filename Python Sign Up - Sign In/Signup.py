from tkinter import *

window = Tk()
window.title("Signup Form")
window.geometry('600x250')
window.configure(background = "#1cf211");
head = Label(window ,text = "Sign UP here if you are not register", bg="#8da832",font='Helvetica 15 bold').grid(row = 0,column = 1)
a = Label(window ,text = "First Name:",bg="#1cf211",font='Helvetica 10 bold',fg="white").grid(row = 1,column = 0)
b = Label(window ,text = "Last Name:",bg="#1cf211",font='Helvetica 10 bold').grid(row = 2,column = 0)
c = Label(window ,text = "Email Id:",bg="#1cf211",font='Helvetica 10 bold',fg="white").grid(row = 3,column = 0)
d = Label(window ,text = "Contact Number:",bg="#1cf211",font='Helvetica 10 bold').grid(row = 4,column = 0)
gen = Label(window ,text = "Gender:",bg="#1cf211",font='Helvetica 10 bold',fg="white").grid(row = 5,column = 0)
pas = Label(window ,text = "Password:",bg="#1cf211",font='Helvetica 10 bold').grid(row = 6,column = 0)
cpass = Label(window ,text = "Confrome Password:",bg="#1cf211",font='Helvetica 10 bold',fg="white").grid(row = 7,column = 0)
a1 = Entry(window,width=50).grid(row = 1,column = 1)
b1 = Entry(window,width=50).grid(row = 2,column = 1)
c1 = Entry(window,width=50).grid(row = 3,column = 1)
d1 = Entry(window,width=50).grid(row = 4,column = 1)
pas1=Entry(window, show="*",width=50).grid(row = 6,column = 1)
cpass1 = Entry(window, show="*",width=50).grid(row = 7,column = 1)
Radiobutton(window, text="Male",  value=1,bg="#1cf211").grid(row=5,column=1)
Radiobutton(window, text="Female", value=2,bg="#1cf211").grid(row=5,column=2)
   
btn = Button(window ,text="Submit", bg="#d3e3d3").grid(row=8,column=0)
btn2 = Button(window ,text="Cancel", bg="red").grid(row=8,column=2)

window.mainloop()
