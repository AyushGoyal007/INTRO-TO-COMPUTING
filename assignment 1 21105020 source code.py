#first program
a=int(input("enter first no:"))
b=int(input("enter second no:"))
c=int(input("enter third no:"))
avg=(a+b+c)/3
print("average of no.s is:",avg,"\n")


#second program
a=int(input("GROSS INCOME:"))
b=int(input("NO. OF DEPENDENTS:"))
c=standard_deduction=10000
d=dependant_deduction=3000
e=tax_rate=0.20                    
f=taxable_income=a-c-(b*d)
tax=f*e
print("tax is:",tax,"\n")

#third program
student=(21105020,"AYUSH GOYAL","M","ECE",9.2)
print("DETAILS OF STUDENTS ARE AS FOLLOWS:",student,"\n")


#fourth program
marks=[12,78,98,45,34]
marks.sort()
print("MARKS ARE AS FOLLOWS:",marks,"\n")


#fifth program
color=["red","green","white","black","pink","yellow"]
color.pop(3)
print(color)
color.pop(3)
color.insert(3,"purple")
print(color,"\n")
