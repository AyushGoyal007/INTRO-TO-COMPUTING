#question 1

#Defining function for tower of hanoi
def tower_of_hanoi(n , source, destination, auxiliary):
    step_number=1
    if n==1:
        print ("Move disk 1 from",source,"to",destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from",source,"to",destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)
#taking no. of disk input from user
no_of_disk=int(input("Enter number of disk in tower of Hanoi:"))
print("\nThe Disks are numbered starting from top of the tower."
      "\nSteps to move all disks from Source Tower to Destination Tower "
      "is given below:\n")
#Using the function of tower of hanoi
tower_of_hanoi(no_of_disk,"Source Tower","Destination","Auxiliary")

#question 2

#Recursive Approach
print("\n[Question.2](Recursive)\nThe Pascle's Triangle using"
      " recursive approach is:\n")

# forming function that will return next row of Pascel triangle
def psum(list1, row):#This funct takes current row element and row no. as  input and returns next row elements
    i1 = 0
    i2 = 1
    l = []
    for i1 in range(row - 1):
        l.append(list1[i1] + list1[i2])
        i1 = i1 + 1
        i2 = i2 + 1
    l.insert(0, 1)
    l.append(1)
    return (l)
#Forming a fun that uses recusion to print pascle's triangle
def pascle_triangle(n,list1,row):
    if n==0:
        return
    else:
        next=psum(list1,row)
        liste=next.copy()
        listp=list(map(str,liste))
        p="  ".join(listp)
        print("{s:^100}".format(s=p))
        pascle_triangle(n-1,next,row+1)

n=int(input("Enter number of rows in Pascle's Triangle:"))
#Alligning the pascle's triangle in triangular form using string formatting and printing it
if n==1:
    print("{a:^100}".format(a="1"))
elif n==2:
    print("{b:^100}".format(b="1"))
    print("{b:^100}".format(b="1 1"))
else:
    print("{b:^100}".format(b="1"))
    print("{b:^100}".format(b="1  1"))
    pascle_triangle(n-2,[1,1],2)


#[Question.2](Iterative)
#Iterative Approach


print("\n[Question.2](Iterative)\nThe Pascle's Triangle using "
      "iterative approach is:\n")
#taking number of rows as input
row=int(input("Enter number of rows:"))
#forming fuction that will return next row of pascel triangle
def psum(list1, row):
    i1 = 0
    i2 = 1
    l = []
    for i1 in range(row - 1):
        l.append(list1[i1] + list1[i2])
        i1 = i1 + 1
        i2 = i2 + 1
    l.insert(0, 1)
    l.append(1)
    return (l)

#forming function that will print all rows using function defined before
def ptriangle(rows):
    if rows == 1:
        print("{a:^100}".format(a="1"))
    elif rows == 2:
        print("{b:^100}".format(b="1"))
        print("{b:^100}".format(b="1 1"))
    else:
        f = "{p:^100}".format(p=1)
        print(f)
        f = "{p:^100}".format(p="1  1")
        print(f)
        l1 = [1, 1]
        row = 2
        for i in range(rows - 2):
            v = psum(l1, row)
            v2 = v.copy()
            v2 = list(map(str, v2))
            n = rows
            k = "  ".join(v2)
            f = "{p:^100}".format(p=k)
            print(f)
            row = row + 1
            l1 = v
ptriangle(row)

#question 3
a=int(input("Enter the first integer: "))
b=int(input("Enter the second integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")


#question 4
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object not valid.")

#creating object
student1 = Student("AYUSH GOYAL", 21105020)
print("Object created")

#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")

#deleting object
del student1
print("")


#question 5
class employees:
    #Using constructor to for class objects
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def pfun(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
#emp_n name and salaray
emp_1=employees("YOGESH",40000)
emp_2=employees("Ashok",50000)
emp_3=employees("JUSTIN",60000)
#print employee detail
emp_1.pfun()
emp_2.pfun()
emp_3.pfun()
#Updating salary of YOGESH to 70000
print("\nQue.5a")
emp_1.salary=70000
print("YOGESH salary Updated to 70000")
emp_1.pfun()
#Deleting JUSTIN's data
print("\nQue.5b")
del emp_3
print("Employee JUSTIN's data has been removed.")



#question 6
gap=" "*10
print(f"\n{gap}WELCOME TO THE FRIENDSHIP GAME")
#definig principle of game i.e. anagram
def anagram(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1=str(input("\nEnter Player1 name:"))
player2=str(input("Enter Player2 name:"))
#taking words spoken by written
word_player1=str(input(f"\nEnter Word by {player1}:"))
word_player2=str(input(f"Enter Word by {player2}:"))
#using anagram function
result=anagram(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")
