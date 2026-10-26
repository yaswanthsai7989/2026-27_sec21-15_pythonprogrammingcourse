#Write a python program to calculate compound interest
p=float(input("enter the principle amount in rupess :-"))
r=float(input("enter the rate of intrest in rupess:-"))
t=float(input("enter the time period in months:-"))
result=(p*((1+r)**t)/100)-p
print("compund intrest in rupess:-",result)
