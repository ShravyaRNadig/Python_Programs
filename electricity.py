name = input("Enter Customer Name : ")
billno = input("Enter Bill Number : ")
unit = int(input("Enter Units : "))
if(unit<=100):
    charge = 0
elif(unit>100 and unit<=200):
    charge = (100*0)+((unit-100)*1)
elif(unit>200 and unit<=300):
    charge = (100*0)+(100*1)+((unit-200)*2)
else:
    charge = unit*3
print("***** Invoice *****")
print("Customer Name  : ",name)
print("Bill No : ",billno)
print("Total Unit : ",unit)
print("Total Amount : ",charge)
