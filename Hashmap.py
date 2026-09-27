"""
h = {}
h[1]='sanjan'
h[2]='kumar'
h[3]='sowbhagya'
h[4]='sarangi'
print(h)
print(h[1])
h[2] = 'chethan'  # value get updated
print(h.keys())
print(h.values())
print(h[2]=='chethan')

print(1 in h.keys())
print("sanjan" in h.values())
"""

# iterating the hashmap using keys

h = {1: 'sanjan', 2: 'kumar', 3: 'sowbhagya', 4: 'sarangi',5:"chethan"}
for i in h.keys():
    print(i)   # to fetch all the keys


h = {1: 'sanjan', 2: 'kumar', 3: 'sowbhagya', 4: 'sarangi',5:"chethan"}
for i in h.keys():
    print(h[i]) # to fetch all the values
