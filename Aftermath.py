'''
a = int(input("Enter a Number"))
b = int(input("Enter second Number"))
i = input(" Choose the operator \"+\",\"-\",\"*\",\"/\" ")
if i is add or  or * or /:
    print(aib)
if i is "-":
    print(
''''''
#TIME Module
import time
timestamp = time.strftime('%H:%M:%S:%p')
print(timestamp)
timestamp1 = int(time.strftime("%H"))
timetstamp2 = int(time.strftime("%M"))
timestamp3 = int(time.strftime("%S"))
timestamp4 = (time.strftime("%p"))
if timestamp1 >0 and timestamp1<12:
    print("Good morning ")
else:
    timestamp1 >12 and timestamp1<15 and timestamp4 == "PM"
    print("Good Afternoon ")
else:
    timestamp1 >5 and timestamp1 <8 and timestamp4 == "PM" 
    print("Good night Mi amor")
else:
    timestamp1>8 and timestamp1<= 11 and timestamp == "PM"
    print("Good Night:)")'
##
''''''
#1 here range proceeds in ascending order so step"3rd" num will be choosed accordingly
for i in range(-1,-19,-7):
    print(i)
''''''
# for odd numbers
'''# method 1
'''for i in range(1,10,2):
    print(i)
''''''#method 2
a = int(input("Enter A number"))
for i in range(a):
    if i % 2 != 0:
        print(i)
# A program to display all the numbers divisible by 5 from 1 to n
a = int(input("Enter A number"))
for i in range(a):
    if i % 5 == 0:
        print(i)'''
# sum of n number
'''
a = int(input("Enter the number"))
sum = 0
for i in range(1,a+1):
    sum += i
print(sum)
  # prod of n number

a = int(input("Enter A Number"))
fact = 1
for i in range(1,a+1):
    fact *= i
print(fact)


a = int(input("Enter a number"))
sum = 0
for i in range(2,a+1,2):
    sum+=i
print(sum)
'''
'''
#display the square of all number from 1 to n
a = int(input("Enter the number"))
for i in range(1,a+1):
    i = i**2
    print(i)
'''
'''
#display the sum of square/ or power of anything
a = int(input("ENter a number"))
b = int(input("Enter 2nd number"))
sum = 0
for i in range(1,a+1):
    i= i**b
    sum += i
print(sum)
'''

'''# sum of 1+1/2+1/3....n
a = int(input("Enter the num"))
sum1 = 0
for i in range(1,a+1):
    print(1/i,end=",")
    sum1 += 1/i
print(sum1)
 '''
'''
# replace 1 by x from above problem
a = int(input("Enter the num"))
n = int(input("2nd no."))
sum1 = 0
for i in range(1,a+1):
    print(n/i,end=",")
    sum1 += 1/i
print(sum1)
'''

'''a = int(input("Enter a num"))
b = int(input("2nd No'))"))
sum1 = 0
for a in range(1,b+1):
    sum1 += a**b
    print(sum1)
   '''
'''a = int(input("Enter the number"))
b = int(input("Enter 2nd number"))
fact= 1
sum1 = 0
for b in range(1,a+1):
    fact *= b
    b = b**a/fact
    sum1 += b
    print(b)

'''
'''
#fibonaciii series
n = int(input("number of terms"))
a = 0
b = 1
if n == 1:
    print(a)
elif n == 2:
    print(a,b)
else:
    print(a,b,end='')
    for i in range(3,n+1):
        c = a+b
        print(c,end='')
        a = b
        b = c# here we are replacing cause fibonacii series is sum of previous two numbers
'''
'''
# program to enter n numbers and find the larges
n = int(input("how many nos. you want to put in here"))
big = 0
for i in range(n+1):
    a = int(input("enter your nos"))
    if a > big:
        big = a
print("the biggest no is" , big)
'''
'''# count no of vowels
a = input("Enter your string")
b = len(a)
char = 0
for i in a:
    if i == "a" or i == "e" or i == "i" or i =="o" or i == "u":
        char += 1
print(char)
'''
'''# Count no. of words
a = input("Enter your sentence")
b = a.count(" ")
c = b+1
print(c)
'''
'''#Count no of +ve and - ve nos
b = int(input("ENter no the numbers"))
pos = 0
neg = 0
for a in range(b):
    a = int(input("enter the numbers"))
    if a >0:
        pos+=1
    if a <0:
        neg+=1
    if a == 0:
        print("Neither pos nor negative")

print(pos)
print(neg)
'''
'''#write the tabule
a = int(input("Enter the number for the tabule"))
for i in range(1,11):
    b = i*a
    print(a, "X", i, "=",b)
'''
'''
a = int(input("kitne ka average nikalna hai"))
sum1 = 0
for i in range(a):
    i = int(input("Enter those nos."))
    sum1 += i
    #print(sum1)
c = sum1/a
print(c)
'''
'''
# how to find a prime number
a = int(input("Enter the no."))
count1 = 0
for i in range(2,a):
    if a%i == 0:
        print("its not prime")
        break
        #count1+=1
#print(count1)
    else:
        print("its prime")
        break
'''
'''
#while Loop
n = int(input("Enter the number"))
i = 0
while i<n:
    i += 1
    print(i)
'''
'''
# to count +ve and -ve nos and terminates when entered zero
pos = 0
neg = 0
i = 1
while i!= 0:
    i = int(input("Enter the intergers"))
    if i>0:
        pos += 1
    print(pos)
    if i <0:
        neg += 1
    print(neg)
 '''
'''
# A program to find average of +ve nos and terminate when zero is entered
# some problem
sum1 = 0
chrt1 = 0
i = int(input("Enter the nos"))
while i != 0:
    if i > 0 :
        sum1 += i
        chrt1 +=1
        avg = sum1/chrt1
        i = int(input("Enter the nos"))
        print(avg) 
'''
'''a = int(input("Enter your number"))
while a > 0:
    b = a % 10
    print(b)
    b += b// 10

'''
'''
##############################################
#lists
num1 = [90,87,34,67,90,56]

''''''for i in range(l):
    print(num1[i],end = '*')'''
'''num1.sort(reverse = True)
print(num1)
l = [53,63,67,36,86,38]
''''''a = l + num1
print(a)
''''''
# to add the elements of two lists
c = [0,0,0,0,0,0]
a = len(l)
for i in range(a):
    c[i] = num1[i] + l[i]
print(c)'''
 # here we can only add list of same length so if there is not same length of list then make the smaller one equal to larger by adding element 0
# to add list of n numbers
'''a = int(input("enter the no. of list u wanna add"))
t = 0
for t in range(a):
    t += 1
    c = []
    p = int(input("enter the no. of element you wanna add"))
    g = 0
    i = 0
    while i <= p-1:
        i += 1
        c.append(g)
    print(c)
    lst = []
    for i in range(p):
        num = int(input("Enter the elements"))
        lst.append(num)
    print(lst)
    c[i] = c[i] + lst[i]
print(c)
print(t)
''''''lst = []
m = 4
g = 0
i = 0
while i <= m:
    i += 1
    lst.append(g)
print(lst)
    '''
'''lst = []
for num in range(4):
    num = int(input("entr no."))
    lst.append(num)
print(lst)
'''
'''
# Step/ method 2
a = int(input("enter the no. of list u wanna add"))
c = []
p = int(input("enter the no. of element you wanna add"))
g = 0
i = 0
while i <= p-1:
    i += 1
    c.append(g)
print(c)
for t in range(a):
    lst_t = []
    for i in range(p):
        num = int(input("Enter the elements"))
        lst_t.append(num)
    print(lst_t)
    c[i] = lst_t[i] + c[i]# i dont know how to solve from here 
print(c)
'''
'''
# searchng aelement in list
lst = []
a = int(input("Enter the number of elements u wanna add"))
for i in range(a):
    ele = int(input("Enter the elements"))
    lst.append(ele)
print(lst)
b = int(input("enter the element you wanna find"))
#method 1:
for no in range(a):
    if lst[no] == b:
        print("found succesfully at",no+1)
        break
    else:
        print("Doesn't exist")
        break
#method 2:
#use of lst.index is to find where is that element
a = lst.index(b)
print(a+1)
#method 3
if b in lst:
    print("found")'''
###########################################################
#tuple
# fstring
#letter = "Hey my name is {} and I live in {}"
'''name = input("Enter name")
place = input("Enter place")
#print(letter.format(name,place))
print(f"Hey my name is {name} and I live in {place}")  
'''
# decimal
'''price = float(input("enter no"))
txt = f"For only {price:.3f} ruppee"# agar . nahi lagaoge to piche se 3 ka round off kar dega
print(txt)

print(f"{2*3546}")
'''
'''# recurssion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))      
'''
'''
# KBC type questions
name = input("Enter name")
print(f"welcome to KBC, I am Alfax and this is {name} ,and we will be playing kaun banega crorepati")
print("your 1st question on your screen is for 10 thousands")
questions = ["Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station","longest railway station","None of the above"],
["Entomology is the science that studies","Behavior of human beings","Insects","The origin and history of technical and scientific terms","The formation of rocks"],
["Where is the Railway Staff College located?","Pune","Allahabad","Vadodara","Delhi"],
["Bijapur is known for its","severe drought condition","Gol Gumbaz","heavy rainfall","statue of Gomateswara"],
["'.MOV' extension refers usually to what kind of file?","Image file","Animation/movie file","Audio file","MS Office document"],
["'OS' computer abbreviation usually means ?","Order of Significance","Open Software","Operating System","Optical Sensor"],
["Which was the 1st non Test playing country to beat India in an international match?","Canada","Sri Lanka","Zimbabwe","East Africa"],
["Which was the 1st non Test playing country to beat India in an international match?","Canada","Sri Lanka","Zimbabwe","East Africa"],
["What is part of a database that holds only one type of information?","Report","Field","Record","File"]
levels = [10000,20000,40000,80000,160000,320000,10000000,25000000,50000000]
for i in range(len(questions)):
    print(f"this question is for Rs.{levels[i]}")
    print(
'''
'''
a = int(input("Enter any value between 5 & 9"))
if a >= 9 and a <= 5:
    raise SyntaxError("value should bet 5 and 9")
'''
'''a = int(input("enter your number"))
b = int(input("enter 2nd number"))
print("a is bigger") if a>b else print("both are equal") if a == b else print("b is bigger") if a<b else"" 
#print(473) if a<b else ""

'''
'''
import manji
manji.manj()
'''
'''
# sum from m to n using while loop
a = int(input("enter no:-"))
b = int(input("Enter 2nd no:-"))
sum1 = 0
if a >= b:
    while(a>=b):
        sum1 = sum1 + b
        b += 1
    print(sum1)
else:
    while(a<=b):
        sum1 = sum1 + a
        a += 1
    print(sum1)
'''
'''
#for binary to decimal
a = int(input("Enter only binary numbers"))
sum1 = 0.0
i = 0
while(a !=0):
    b = a%10
    c = (2**i)*b
    i += 1
    sum1 += c
    a //= 10
print(sum1)
'''
'''
#sum of any power of even nos.
a = int(input("enter no."))
n = int(input("enter no2."))
sum1 = 0
for i in range(a+1):
    if i % 2 == 0:
        b = i**n
        sum1 += b
print(sum1)
'''
'''
#paterrn1
a = int(input("enter no"))
for i in range(1,a+1):
    print("Pass ",i,"-",end=" ")
    for b in range(1,a+1):
        print(b,end = '')
    print(" \n")
'''
'''
#pattern 2
a = int(input("entero"))
b = "*"
c = a *2
for i in range(a):
    for j in range(c):
       print(b,end="")
    print()
'''
'''
#pattern 2
for output
1
12
123
1234
12345

a = int(input("enter no"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

'''
'''
#paterrn for output:-
1
22
333
4444
55555
a = int(input("enter no."))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i,end='')
    print()
'''
'''
# 4.51
a = int(input("enter no"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(" "*(a-j),j,end='')
    print()

'''
'''
# Introduction to oops in python

class person:
    name = "Name of person"
    job = "JoB of the person"
    salary = "salary_person"
    def info(self):
        print(f"{self.name} is a {self.job} and his salary is {self.salary}")
a = person()
b = person()
a.name= "Ram"
a.job = "Chor"
#a.salary = "200" you still don't know about salary 

b.name = "Kalu"
b.job = "slave"
#a.salary = "20"
a.info()
b.info()

'''
'''
class VECTOR:
  def __init__(self,i,j,k):
    self.i = i
    self.j = j
    self.k = k
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k" 
  def __add__(self,self2):
    return (f"{self.i+ self2.i}i  + {self.j+self2.j}j + {self.k+self2.k}k")
    #Note these fuctions with__somthin__ doesn't need to be called they are operator over loading....
  #Noter there is self and self2 so only two items can be added
  def __mul__(self,self3):
    return f"{self.i*self3.i}i + {self.j*self3.j}j +{self.k*self3.k}k"
v1 = VECTOR(5,6,7)
v2 = VECTOR(7,8,9)
v3 = VECTOR(1,2,3)
print(v2)
print(v3)
print(v1)
print(v1 + v2)
print(v1 * v2)
'''
'''
class Animal:
    def __init__(self,species):
        self.spci = species
    def species_name(self):
        print(f"{self.spci} This species wee are studing")
class Dog(Animal):
    def __init__(self,normal_name,breed):
        Animal.__init__(self,species = "Canis Lupus")
        self.name = normal_name
        self.breed = breed
    def make__sound(self):
        print(f"{self.name}  'Barks'")
sp1 = Dog("DOG","Pameraneon")
sp1.make__sound()
sp1.species_name()

'''
import time
'''
print("hi bro how are you")
time.sleep(5)
print('iam still sleepinh')
'''
'''
def foruse():
    for i in range(501):
        print(i)
def whileuse():
    i = 0
    while i<501:
        i=i+1
        print(i)
a = time.time()
foruse()
b = time.time()
A = time.time()
whileuse()
B = time.time()
print(b-a)
print(B-A)
'''
'''
t = time.localtime()
formatted_time = time.strftime('%Y-%m-%d %H:%M:%S, %y',t)
print(formatted_time)
print(t)
t1 = time.asctime(t)
print(t1)

'''
'''
import os
print(os.name)
print(os.sep)
print(os.getcwd())
current_dir = os.getcwd()
for index in os.walk(current_dir):
    print(index)
'''
'''


# right way to find amstrong number
b = int(input("enter num"))
a = b
c = 0
sum1 = 0
m = b
n = 0
while (a > 0):
  d = a%10
  a //= 10
  c += 1
  print(d)
while (m>0):
  k = m% 10
  m //= 10
  sum1 += k**c
if (sum1 == b):
  print("armstrong")
else:
  print("not armstrong")'''

'''
import shutil
shutil.copy("file","file2")
import shutil
#shutil.copy("file.txt","file2.txt")
#shutil.copytree("shut","shut2")
#shutil.move("shut/file2.txt","file2.txt")
import os

# shutil.move("shut2/file2.txt","file2.txt")
# os.remove("file2.txt")
#os.rmdir("shut")
#shutil.copy("file.txt","file1.txt")
shutil.move("file1.txt","shut/file1.txt")
'''
'''
def large(index,arr,b):
    if index > len(arr)-1:
        return
    b = arr[index]
    if b < arr[index+1]:
        b = arr[index+1
    large(index+1,arr,b)
    if b > arr[index+1]:
            return b
print(large(0,[1,4,3],0))

'''
'''
temp=[]
def merge(arr,low,mid,high):
    left = low
    right = mid+1
    while (left<mid) and (right <= high):
        if arr[left]<= arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right += 1
    while (left<=mid):
        temp.append(arr[left])
        left += 1
    while (right <= high):
        temp.append(arr[right])
        right+=1
    print(temp)
    for i in range(low,high):
        arr[i] = temp[i-low]
    
            
            
def ms(arr,low,high):
    if (low>=high):
        return
    mid = (low + high)//2
    ms(arr,low,mid)
    ms(arr,mid+1,high)
    merge(arr,low,mid,high)
ms([1,3,4,2,5,7,4],0,6)
    
'''
'''
def swap(index,arr,num,lis):
    a = arr[index]
    b = arr[num]
    c = a
    a = b
    b = c
    if index>=num//2:
        lis.append(arr[index])
        print(lis)        
    lis.append(a)
    swap(index+1,arr,num-index-1,lis)
    lis.append(b)
arr= [1,2,3,4,5]
num = len(arr)
print(swap(0,arr,num-1,[]))
'''
'''
big = []
a = int(input("enter len"))
for i in range(a):
    name = input("Enter number")
    score = int(input("enter score"))
    lis = []
    scor = []
    lis.append(name)
    lis.append(score)
    scor.append(score)
    big.append(lis)
print(big)
a = min(scor)
scor.remove(a)
print(b)
for list1 in big:
    if list1[1] == a:
        big.remove(list1)
print(big)
'''
'''
entry = int(input("number of entery"))
student_marks = {}
for i in range(entry):
    key,*value = input("enter key then value ").split()
    score = list(map(float,value))
    student_marks[key] = score
query_name = input("enter the name")
marks = student_marks[query_name]
s = sum(marks)
m = 0
b = float(m)
for i in marks:
    b += 1
avg = s/b
average = f"{avg:.2f}"
print(average)

'''
'''
import time as t
import asyncio
async def fun1():
    await asyncio.sleep(3)
    print("tumri")
async def fun2():
    await asyncio.sleep(2)
    print("romari")
async def fun3():
    await asyncio.sleep(1)
    print("Romance")

async def main():
    L = await asyncio.gather(
        fun1(),fun2(),fun3()
        )
    print(L)
    

asyncio.run(main())
'''
'''
n = int(input())
arr = list(map(int, input().split()))
array = arr[:n]
print(array)
a = max(array)
b = set(array)
lis = list(b)
for index,items in enumerate(lis):
    if items == a:
        lis.pop(index)
print(min(lis))
'''
'''
if __name__ == '__main__':
    N = int(input())
    array = []
    for _ in range(N):
        s = input().split()
        val = s[0]
        for i in range(1,len(s)):
            s[i] = int(s[i])
        if val == "insert":
            array.insert(m,s[2])
        elif val == "print":
            print(array)
        elif val == "remove":
            array.remove(s[2])
        elif val == "append":
            array.append(9)
        elif val == "sort":
            array.sort()
        elif val == "pop":
            array.pop()
        elif val == "reverse":
            array.reverse()
'''
'''
a = int(input("enter height"))
h = 'H'
j = 0

while(j<a):
    print(" "*((a-j-1)),h*((2*j)+1))
    j+=1
for i in range(a+1):#29 as 29-4 = 25 25-10 = 15
    print(" "*((a-1)//2)+h*a+" "*(a*3)+h*a)
for i in range(3):#27 as 27-2= 25
    print(" "*((a-1)//2)+h*(a*a))
for i in range(a+1):
    print(" "*((a-1)//2)+h*a+" "*(a*3)+h*a)

i = 0
while(i<=a):
    z = " "*i+h*((a-i-1)*2+1)+" "*i
    print(a*4*(" ")+z)
    i+=1
'''
'''
def wrap(string,ln):
    for i in string:
        print(i)
wrap("ABCDEFGHIJKLMNOPQRSTUVWXYZ",4)
'''
'''
import textwrap

text = "This is a long sentence that needs to be wrapped to fit within a specified width."
wrapped_text = textwrap.fill(text, width=20)

print(wrapped_text)
import textwrap

text = "This is a long sentence that needs to be wrapped to fit within a specified width."
wrapped_text = textwrap.fill(text, width=20)

print(wrapped_text)
'''
'''
s = '1 w 2 r 3g'
s = s.title()
print(s)
a = "hello 67world"
for i in a.split():
    print(i)
'''
'''
a = "hello   world  lol"
def solve(s):
    a = ''
    for i in s.split():
        b = i.capitalize()
        c = " "+b
        a += c
            
    return a.strip()
print(solve(a)) 
'''
'''
#from coloroma import __Fore
#from termcolor import colored
import turtle
manj = turtle.Turtle()
print(manj)
print(manj.shape())
print(manj.shape('turtle'))
#shapes = 
print(manj.color())
print(manj.forward(50))
print(manj.color('red'))
print(manj.forward(50))
print(manj.color('blue','yellow'))
print(manj.forward(50))

# Back ground
wn = turtle.Screen()
(wn.bgcolor("cyan"))
print(wn)
#print(manj.backward(300))
print(wn.title("kalua"))

'''



'''
arr = [3,1,2]
n = len(arr)

def f(index,list1):
    if index >= n:
        if len(list1)==0:
            pass
        else:
            print(list1)
    else:
        list1.append(arr[index])
        f(index+1,list1)
        list1.pop()
        f(index+1,list1)

f(0,[])


'''

'''

def accept(A,str1):
    n = int(input("Enter the no. of students  "))
    for i in range(n):
        name = input("Say my name")
        if name not in A:
            A.append(name)
        else:
            print("Duplicate Entry")
            i -= 1
    return A



def Search(Arr,key):
    for i in range(len(Arr)):
        if key == Arr[i]:
            return 1
    return 0

def union(Arr1,Arr2,uni):
    for i in range(len(Arr2)):
        flag = Search(Arr1,Arr2[i])
        if flag != 1:
            uni.append(Arr2[i])
    return uni

#print(union)
    
def intersection(Arr1,Arr2,Empty_Arr):
    for i in range(len(Arr1)):
        flag = Search(Arr2,Arr1[i])
        if flag == 1:
            Empty_Arr.append(Arr1[i])
    return Empty_Arr



def compliment(Arr1,Arr2,emp):
    for i in range(len(Arr1)):
        flag = Search(Arr2,Arr1[i])
        if flag != 1:
            emp.append(Arr1[i])
    return emp



def main():
    Cricket = accept([],"Cricket")
    Badminton = accept([],"Badminton")
    Football = accept([],"Football")
    C = Cricket
    B = Badminton
    F = Football
    print(F)
    #intersections
    L = []
    M = []
    N = []
    # Unions
    Un1 = C
    Un2 = C
    Un3 = B
    #complimentries

    T = []
    P = []
    O = []
    
    while True:
        print("Enter the number from 1 to 5 of your choice \nFor both circket and badminton press 1\nFor either circket or badminton but not both2 \nFor students who play neither cricket not badminton press 3 \nThose who play cricket and football and not badminton press 4\n to exit press any number ")
        choice = int(input("enter number"))
        CUB = union(C,B,Un1)
        CUF = union(C,F,Un2)
       # print(CUF)
        CnB = intersection(C,B,L)
        CnF = intersection(C,F,M)
       

        if choice == 1:
            return CnB
        elif choice == 2:
            CuB_comp = compliment(CUB,CnB,T)
            #print(CuB_comp)
            return CuB_comp
        
        elif choice == 3:
           # print(3)
            F_comp = compliment(F,CUF,P)
            print(F_comp)
            return P
        
        elif choice == 4:
            #CnF- B
            CnF_comp = compliment(CnF,B,O)
            #print(CnF_comp)
            return O
        
        else:
            print("Exited")
            return False

def display():
    Arr = main()
   # print(Arr)
    #print("{",end='')
    for i in range(len(Arr)-1):
        print(Arr[i],end=",")
    print(Arr[len(Arr)-1],"}")

display()
'''
'''
b = ['a','b','c','a','d','b','a']
++l = ['a','b','c','a','d','b','a']
s = []
leng = len(l)
for i in range(leng):
    val = l.pop()
    if val in l:
        pass
    else:
        s.append(val)

print(s)
'''
'''
l1 = ["a","b","c","d"]
l2 = ["b","c","f"]

def Search(Arr,key):
    for i in range(len(Arr)):
        if key == Arr[i]:
            return 1
    return 0

emp = []
def compliment(Arr1,Arr2,emp):
    for i in range(len(Arr1)):
        flag = Search(Arr2,Arr1[i])
        if flag != 1:
            emp.append(Arr1[i])
print(emp)
'''
'''
def Search(Arr,key):
    for i in range(len(Arr)):
        if key == Arr[i]:
            return 1
    return 0

def compliment(Arr1,Arr2,emp):
    for i in range(len(Arr1)):
        flag = Search(Arr2,Arr1[i])
        if flag != 1:
            emp.append(Arr1[i])
    return emp

val = compliment(["b","d","f"],["a","b","c","d"],[])
print(val)
'''
