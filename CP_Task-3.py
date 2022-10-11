from array import *
#from numpy import *
def swap(x,y): 
    print("Before swapping a :",x)
    print("Before swapping b :",y)
    #logic to swap without using third variable 
    temp=x
    x=y
    y=temp
    return x,y 
#a=int(input("Enter value of a : "))
#b=int(input("Enter value of b: "))    
#a,b=swap(a,b) 
#print("After swapping a becomes :",a)
#print("After swapping b becomes :",b)
a=array('i',[])
b=array('i',[])
n=int(input("enter the length of array:"))

for i in range(n):
    x=int(input("enter value:"))
    a.append(x)
    a=b
print(a)
#for i in range(n-1):
 #   a[i]=b[i]

#for i in range(n):
 #   print(b[i])
print(b)
for i in range(0,n+1):
    if(b[i]>b[i+1]):
        swap(b[i],b[i+1])
for i in range(0,n):
    print(b[i])
for i range(0,n):
    if (a[i]==b[i]):
        if(b[i]<b[i+1]):
            swap(b[i],b[i+1])
for i range(0,n):
    print(b[i])
#n=int(input("enter lenght of string:"))
#for i in range(0,n):
 #   a=int(input("enter value:"))
#for i in range(0,n-1):
 #       print(a[i])

#print(a)