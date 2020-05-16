import mysql.connector
 
 
name =input("Enter name: ")
con = mysql.connector.connect(host = "localhost",
                              user = "root",
                              password="root",
                              database = "db")
if(con):
     c = con.cursor()
     
     q = "DELETE FROM myguests3 WHERE name =%s"
     data = (name,)
     c.execute(q, data)
     """c.execute(q,data)"""
     con.commit()
     print("Deleted")
     con.close()
else:
    print("Not connected")
