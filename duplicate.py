l=[2,3,2,9,7,3]
unique=set(l)
print(unique)

#using loop
l1=[4,5,4,2]
r=[]
for i in l:
    if i not in l1:
        r.append(i)
print(r)
        