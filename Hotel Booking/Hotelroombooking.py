"""
Customer Name
Contact
ID
Date
Days
room
rent =1000
tot =rent*days*rooms
0 - 5 = 5%
5 - 10 = 10%
10 - 15 = 15%
more than 15 = 20%
"""

name = input("Enter Customer Name : ")
contact = input("Enter Contact Number : ")
Id = input("Enter ID Number : ")
date = input("Enter Date of Booking : ")
days = int(input("Enter Number of Days : "))
rooms = int(input("Enter Number of rooms : "))
rent = 1000
tot = rent*days*rooms
if(days>0 and days<=5):
    dis = tot*0.05
    net = tot-dis
elif(days>5 and days<=10):
    dis = tot*0.1
    net = tot-dis
elif(days>10 and days<=15):
    dis = tot*0.15
    net = tot-dis
else:
    dis = tot*0.2
    net = tot-dis

print("******* Billing Information ********")
print("Customer Name : ",name)
print("Contact Number : ",contact)
print("ID Number : ",Id)
print("Date : ",date)
print("No.of.Days : ",days)
print("No.of.rooms : ",rooms)
print("Total Amount : ",tot)
print("Discount : ",dis)
print("Net Pay : ",net)
