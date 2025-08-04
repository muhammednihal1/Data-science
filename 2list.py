#write a program that takes two list and return true if they have atleast one common number

l=[1,2,3]
m=[1,4,5]

for i in l:
    if i in m:
        print(True)
        break
    else:
        print(False)
