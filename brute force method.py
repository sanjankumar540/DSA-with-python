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
    print()    


# brute force method to generate all the subarray  (First loop chooses the starting point → second loop chooses the ending point → third loop prints the subarray between them.) important
a = [10,20,30,40,50] 
for i in range(0,len(a)-1+1):
    for j in range(i,len(a)-1+1):
        for k in range(i,j+1):
            print(a[k],end=" ")
        print()

# print the sum of all the subarrays
a = [10,20,30,40,50]
for i in range(0,len(a)+1-1):
    for j in range(i,len(a)+1-1):
        sum = 0
        for k in range(i,j+1):
            sum = sum+a[k]
            print(a[k],end=" ")
        print("sum= ",sum)
        print() 
            
# count all the subarray with sum = k (assume k =30)
a = [10,20,30,40,50,60]
count = 0
target = 30
for i in range(0,len(a)+1-1):
    for j in range(i,len(a)+1-1):
        sum = 0
        for k in range(i,j+1):
            sum = sum+a[k]
            #print(a[k],end="")
        #print(f"sum is equal to {sum}")
        if sum == target:
            count =count+1
        print()
print( "count of subarray:",count)  """

#another example
a=[10,20,30,30,20,40,50,60,0,70,80,90,100]
count = 0
target = 60
for i in range(0,len(a),1):
    for j in range(i,len(a),1):
        sum = 0
        for k in range(i,j+1):
            sum = sum+a[k]
            #print(a[k],end=" ")
        #print(f"the sum of subarray is {sum}")
        if sum == target:
            count=count+1
        #print()
print(f"the count of subarray is :{count}")

            
