import mysql.connector
 
 
name =input("Enter name: ")
email = input("New email id: ")
con = mysql.connector.connect(host = "localhost",
                              user = "root",
                              password="root",
                              database = "shrav")
if(con):
     c = con.cursor()
     
     q = "UPDATE myguests3 SET email = %s WHERE name =%s"
     data = (email,name,)
     c.execute(q, data)
     """c.execute(q,data)"""
     con.commit()
     print("Data Updated")
     con.close()
else:
    print("Not connected")
