#first question 
a="Python is a case sensitive language."
print(len(a))
print(a[::-1])
b=a[11:26]
print(b)
print(a.replace("a case sensitive","object oriented"))
print(a.find("a"))
print(a.replace(" ",""),"\n")


#seond question
a=input("What is your name:")
b=input("What is your SID:")
c=input("What is your department:")
d=input("What is your CGPA:")
print("Hey",a,"Here!")
print("My SID is",b)
print("I am from ",c,"department and my CGPA is",d,"\n")


#third question
#a=56=111000
#b=10=001010
a=56
b=10
print("a&b is:",a&b)
print("a|b is:",a|b)
print("a^b is:",a^b)
print("a<<2 :",a<<2,"\t b<<2:",b<<2)
print("a>>2 :",a>>2,"\t b>>4:",b>>4,"\n")

#fourth question
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b and a>c:
    print("a is the greatest number","\n")
elif b>c:
    print("b is the greatest number","\n")
else:
    print("c is the greatest number","\n")


#fifth question
a="My name is Ayush Goyal"
if "name" in a:
    print("yes","\n")
else:
    print("no", "\n" )


#sixth question
a=int(input("length of first side is:"))
b=int(input("length of second side is:"))
c=int(input("length of third side is:"))
if a>b+c:
   print("No")
elif b>a+c:
   print("No")
elif c>a+b:
   print("No")
else:
   print("Yes")





