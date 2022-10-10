a=str(input("enter :"))
b=str(input("enter :"))
n=len(a)
print(n)
m=len(b)
print(m)

if (n>m):
    print("the 1st word is longer")
    for i in range(0,n):
        c=0
        for j in range(0,m):
            if (a[i]==b[j]):
                
                c+=1
        if (c==0):
            print("the extra letter is: ",a[i])
             
    
else:
    print("in this case the 2nd word is longer or the 2 words are of same length")
    for j in range(0,m):
        c=0
        for i in range(0,n):
            if (b[j]==a[i]):
                c+=1
        if (c==0):
            print("the extra letter is :",b[j])
                
                 
        