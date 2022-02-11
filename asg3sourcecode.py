#first program

a=input("ENTER THE STRING:")
b=a.lower().split()
d1=dict()
c=len(b)
for word in b:
    if c>1:
       if word in d1:
        d1[word]=d1[word]+1
       else:
        d1[word]=1
    elif c==1:
        for letter in b[0]:
            if letter in d1:
                d1[letter]=d1[letter]+1
            else:
                d1[letter]=1

print("OCURRENCES OF THE WORDS ENTERED IN STRING IS:\n",d1,"\n")


#second question
year= int(input("enter the year[1800 - 2025]:"))        
if year in range(1800,2026):               #taking year as input from user
    if year%4==0:                          #checking leap year 
       leap_year=True                   
    else:
       leap_year=False

    

    month=int(input("enter the month[1-12]:"))
    if month in range(0,13):                         #taking month as input
        if month in (1,3,5,7,8,10,12):
            days=31
        elif month==2:
            if leap_year:
                days=29
            else:
                days=28
        elif month in (4,6,9,11):
            days=30
    
        date=int(input("enter the date[1-31]:"))                 #taking date as input
        if date<days:
            date+=1
            print("The next date is [yyyy-mm-dd] %d-%d-%d."%(year,month,date),"\n")
            
        elif date==days:
            date=1
            if month==12:
                year+=1
                month=1
                print("The next date is [yyyy-mm-dd] %d-%d-%d."%(year,month,date),"\n")
            else :
                month+=1
                print("The next date is [yyyy-mm-dd] %d-%d-%d."%(year,month,date),"\n")
                
        else:
            print("error","\n")
    else:
        print("error","\n")
else:
    print("error","\n")


#third program
l1=list()
n=int(input("ENTER LENGTH OF LIST:"))
for i in range(0,n):
      elemt=int(input())
      l1.append(elemt)
print(l1)
new_list=[]
for i in l1:
    new_list.append((i,i**2))
print("LIST WITH FIRST ELEMENT AS NO, AND SECOND AS ITS SQUARE:",new_list,"\n")


#fourth question
#input for grade evaluation
x=int(input("ENTER THE GRADE PLEASE:"))
#putting conditions for grading system from if else loop
if x in range(4,11):
    if x==10:
        grade="A+"
        performance="OUTSTANDING"
    elif x==9:
        grade="A"
        performance="EXCELLENT"
    elif x==8:
        grade="B+"
        performance="VERY GOOD"
    elif x==7:
        grade="B"
        performance="GOOD"
    elif x==6:
        grade="C+"
        performance="AVERAGE"
    elif x==5:
        grade="C"
        performance="BELOW AVERAGE"
    elif x==4:
        grade="D"
        performance="POOR"

    print("Your grade is %s and %s performance."%(grade,performance),"\n")
else:
    print("ERROR!NO GRADING POSSIBLE.GRADES ARE IN 4 TO 10 RANGE.","\n")
    

#fifth program
a="ABCDEFGHIJK"
l=0
while len(a)-l*2>=1:
    print(" "*l ,a[0:int(len(a)-l*2)],"\n")
    l+=1

#sixth program
a="Y"
d1=dict()
while a == "Y":                      #creating student detail dictionary
    d1[int(input("ENTER SID:"))]=input("NAME:")
    a=input("DO YOU WANT MORE?:")
    
    if a=="N":                        #exiting the loop
        break

print("DETAILS OF THE STUDENTS ENTERED IS:",d1)


rev_dict={}                                        #sorting using VALUES
for key,value in d1.items():
    rev_dict.update({value:key})
    rev_dict_items=rev_dict.items()
    Sorted_items=sorted(rev_dict_items)
print("SORTING THROUGH STUDENTS DETAILS IS:",Sorted_items)


d1_items=d1.items()                             #sorting using KEYS
sorted_items=sorted(d1_items)
print("SORTING SID OF STUDENTS IS :",sorted_items)


input_sid=int(input("SID PLEASE:"))
if input_sid in d1:                              #getting student's name through SID
     print("STUDENT DETAILS FROM SID IS:",d1.get((input_sid)),"\n")
    
else:
    print("ERROR!NO SUCH DATA AVAILABLE","\n")



#seventh program
n=int(input("LENGTH OF FIBONACCI SEQUENCE REQUIRED:"))  #taking n as input from user for length of Fibonacci sequence.

a=0   
b=1

if n<=0:
    print("ERROR!!NO FIBONACCI SEQUENCE POSSIBLE.")

else:
    list=[]   
    for i in range (0,n-1):
        if i==0:
            list.append(a)    #fibonacci seq for i=0 
        if i==1:
            list.append(b)    #fibonacci seq for i=1
            continue
        sum=a+b
        a=b
        b=sum
        list.append(sum)      #fibonacci seq for rest of the cases
        sum+=sum

    print("FIBONACCI SEQUENCE IS:",list)

    
    
    sum=0                       #calculating sum of terms in list
    for items in list:
        sum=sum+items
        average=sum/len(list)  #calculating average
    print("AVERAGE OF FIBONACCI SEQUENCE IS",average,"\n")



#eighth program
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

a_set=set1^set2
print("SET OF ELEMENTS IN SET1 AND SET2 BUT NOT BOTH IS:",a_set)                      #part 1

b_set=set1^set2^set3
print("SET OF ALL ELEMENTS THAT ARE IN ONLY ONE OF THE THREE SETS IS:",b_set)        #part 2

c_set=(set1|set2|set3)-(set1^set2^set3)-(set1&set2&set3)
print("ELEMENTS THAT ARE EXACTLY IN TWO SETS IS:",c_set)                              #part 3

d_set=set()
for i in range(1,11):
    if i not in set1:
        d_set.add(i)
print("SET OF ALL INTEGERS IN RANGE 1 TO 10 THAT NOT IN SET1 IS:",d_set)              #part 4

e_set=set(range(1,11))-(set1|set2|set3)
print("SET OF ALL INTEGERS IN RANGE 1 TO 10 THAT ARE NOT IN SET1,SET2 AND SET3:",e_set)     #part 5
 
