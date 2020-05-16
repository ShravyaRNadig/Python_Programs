import mysql.connector
 

con = mysql.connector.connect(host = "localhost",
                              user = "root",
                              password="root",
                              database = "db")
if(con):
     c = con.cursor()
     q = "SELECT * FROM myguests3"
     c.execute(q)
     output = c.fetchall()
     for x in output:
         print(x)
     """c.execute(q,(pa,em))"""
     con.commit()
     
     con.close()
else:
    print("Not connected")
