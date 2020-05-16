import mysql.connector
idd =input("Enter the id") 
name = input("input the name ")
email = input("input the email ")
subject = input("input the subject ")
message =input("input the message ")

con = mysql.connector.connect(host = "localhost",
                              user = "root",
                              password="root",
                              database = "db")
if(con):
     c = con.cursor()
     q = "insert into myguests3 values(%s,%s,%s,%s,%s)"
     c.execute(q,(idd,name,email,subject,message))
     """c.execute(q,(pa,em))"""
     con.commit()
     print("Inserted")
     con.close()
else:
    print("Not connected")
