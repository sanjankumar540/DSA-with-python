n=5
for i in range(1,n+1):
    for j in range(1,i-1):
        print("*",end="")
    print()
    

n=5
for i in range(1,n+1):
    for j in range(1,i+(i-1)+1):
        print("*",end="")
    print()   


n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end="")
    print()

n=10
for i in range(1,n+1):
    for j in range(1,i+2):
        print('*', end="")
    print()

n=7
for i in range(1,n+1):
    for j in range(1,i+(i-1)+1):
        print("*",end="")
    print()   


n=5
for i in range(1,n+1):
    for j in range(1,i+i+1):
        print('*',end="")
    print()   """
"""
# phase 2 of patterns 
n=5
for i in range(1,n+1):
    for j in range(1,(n-i)+1+1):
        print('*',end="")
    print()
    
n=5
for i in range(1,n+1):
    for j in range(1,(n-i)+(n-i+1)+1):
        print("*",end="")
    print()     


n=5
for i in range(1,n+1):
    for j in range(1,(n-i)+(n-i)+2+1):
        print("*",end="")
    print() 

# 2nd session
n=5
for i in range(1,n+1):
    for j in range(1,n-i +1):
        print(" ", end="")
    for j in range(1,i +1):
        print("*",end="")
    print()    

n=5
for i in range(1,n+1):
    for j in range(1,i-1+1):
        print(" " , end="")
    for j in range(1,(n-i)+1+1):
        print("*" , end="")
    print()

# important (equilateral triangle)
n=5
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(" ", end="")
    for j in range(1,i+(i-1)+1):
        print("*", end="")
    print()


n=5
for i in range(1,n+1):
    for j in range(1,i-1+1):
        print(" " , end="")
    for j in range(1,(n-i)+(n-i+1)+1):
        print("*", end="")
    print()

# inportant
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end="")
    print()
n=4
for i in range(1,n+1):
    for j in range(1,n-i+1+1):
        print("*",end="")
    print()  

#important
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" " , end="")
    for j in range(1,i+i-1 +1):
        print("*", end="")
    print()
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" " , end="")
    for j in range(1,(n-i)+(n-i)+1 +1):
        print("*",end="")
    print()   


#
n=5
x=1
for i in range(1,n+1):
    for j in range(1,i+1):
        x=j
        print(x,end="") 
    print()    

n=5
y=1
for i in range(1,n+1):
    y=5
    for j in range(1,i+1):
        print(y, end="")
        y=y-1  
    print()
   

n=5
y=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(y,end="")
        y+=1
    print()   

n=5
y=15
for i in range(1,n+1):
    for j in range(1,i+1):
        print(y,end="")
        y=y-1
    print()   

n=5

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    x=1
    for j in range(1,i+1):      
        print(x,end="")
        x+=1
    y=i-1
    for j in range(1,i-1+1):
        print(y,end="")
        y-=1
    print()   

n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" " , end="")
        
    x=i
    for j in range(1,i+1):
        print(x, end="")
        x-=1
        
    y=2
    for j in range(1,i-1+1):
        print(y,end="")
        y+=1
    print()   """

'''
n=5
for i in range(1,n+1):
    
    for j in range(1,i-1+1):
        m=j
        print(m,end="")
        
    for j in range(1,(n-i)+(n-i)+1):
        x=i
        print(x,end="")
        
    y=i
    for j in range(1,i+1):
        print(y,end="")
        y=y-1
    print()
n=4
for i in range(1,n+1):
    a=1
    for j in range(1,n-i+1):
        print(a,end="")
        a+=1
    y=n-i+1
    for j in range(1,i+i+1+1):
        print(y,end="")
        
    c=n-i
    for j in range(1,n-i+1):
        print(c,end="")
        c-=1
    print()    
n=4
y=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(y,end='')
        y=y+1
    print()




    

    
