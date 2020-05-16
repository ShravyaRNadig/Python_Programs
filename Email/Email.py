import smtplib
import random
fromaddr="techcitiforyou@gmail.com"
toaddr=input("Enter Email Id : ")
msg=str(random.randint(1000,9999))
print(msg)
username="techcitiforyou@gmail.com"
password="techcititech@123"
server=smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddr,msg)
print("msg send success")
server.quit()
