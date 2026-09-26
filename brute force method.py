"""#generating all the pairs of an array
a = [1,2,3,4,5]
for i in range (0,len(a)):
    for j in range (0,len(a)):
        print(a[i],",",a[j])
    print()

# with condition i<j (no repetitiion)
a = [10,20,30,40,50]
for i in range(0,len(a)-1+1):
    for j in range(i+1, len(a)-1+1):
        print(a[i] ,a[j])
    print()
    
# print all the sum of pairs
a = [10,20,30,40,50]
for i in range(0,len(a)-1+1):
    for j in range(0,len(a)-1+1):
        print(a[i],"+",a[j],"=",a[i]+a[j])
    print()

# print all the sum of distinct pairs

a = [10,20,30,40,50]
for i in range(0,len(a)-1+1):
    for j in range(i+1,len(a)-1+1):
        print(a[i]+a[j])
    print()   

#print all the pairs of i,j where sum = 60 and i<j
a = [10,20,30,40,50]
sum = 60
for i in range(0,len(a)-1+1):
    for j in range(i+1,len(a)-1+1):
        if a[i]+a[j]==sum:
            print(a[i],",",a[j])
    print()    


a = [10,20,30,40,50]
result = 60
for i in range (0,len(a)):
    for j in range (i+1,len(a)):
        for k in range (j+1,len(a)-1+1):
            if a[i]+a[j]+a[k] == result:
                print(a[i],",",a[j],",",a[k])
    print()   """


# brute force method to generate all the subarray
a = [10,20,30,40,50,60]
for i in range(0,len(a)-1+1):
    for j in range(i,len(a)-1+1):
        for k in range(j,len(a)-1+1):
            print(a[k],end=" ")
        print()
