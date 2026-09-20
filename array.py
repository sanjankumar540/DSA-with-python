#copy the elements of array into new array
"""n = 10
a=[10,20,30,40,50,60,70,80,90,100]
b=[0]*10
print(b)
for i in range(0,n):
    b[i]=a[i]
print(a)

a=[10,20,30,40,50,60,70,80,90,100]
n=0
for i in a:
    n+=1
print(n)  """

#prefix sum array
a=[4,7,3,19,45,39,5]
n=7
psum = [0]*n
psum[0] = a[0]
for i in range(1,n-1+1):
    psum[i]=psum[i-1]+a[i]
print(psum)
print(psum[n-1])  # sum of array
   

