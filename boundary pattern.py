"""
n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==9 or j==1 or j==9:
            print("* ",end="")
        else:
            print("  " ,end="")
    print()   

n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==9 or j==1 or j==9 or i==j:
            print("* ", end="")
        else:
            print("  ",end="")
    print()     
 

n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==9 or j==1 or j==9 or (i+j)==n+1 :
            print("* " ,end="")
        else:
            print("  ", end="")
    print()   

n=30
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1 or j==(n/2) or j==1 or j==n or i ==1 or i==n or i==n/2 :
            print("* ",end="")
        else:
            print("  " ,end="")
    print()   

n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n or i==j:
            print("*", end="")
        else:
            print(" " , end="")
    print()    

n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i+j==n+1:
            print("* ",end="")
        else:
            print("  " , end="")
    print() 

n= 9
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==j or i+j==n+1 :
            print("*" , end="")
        else:
            print(" ",end="")
    print()  

n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1-4 or i==j+4 or i==j-4 or i+j==n+1+4:
            print("* ",end="")
        else:
            print("  ", end="")
    print()   """

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==j or i+j ==n+1:
            print("* ", end="")
        else:
            print(" ",end="")
    print()

    

    
