# swap array
"""arr = [10,20,30,40,50,60,70,80]
n=len(arr)
i=0
j=n-1
while i<j:
    arr[i] = arr[i]+arr[j]
    arr[j] = arr[i]-arr[j]
    arr[i] = arr[i]-arr[j]
    i+=1
    j-=1
print(arr)


a=[1,2,3,4,5,6,7,5,3,7,8,0,9,0,6]
s=set(a)
print(s)"""

class Dt:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
x=Dt(10,23.5,"pavan")
print(x)
print(x.__dict__)
y=Dt(13,29.5,"kumar")

y=None
print(y)

