a=10
b=5
print("Arithmetic Operations")
print(f"Substarction :{a-b}")
print(f"Addition :{a+b}")
print(f"Multiplication :{a*b}")
print(f"Division :{a/b}")

print("LIST Operations")

L=[1,2,3]
sum=0
for i in L:
    sum=sum+i
    print (f"{i}")
print(f"list L sum :{sum}")
L.append(8)
print("After appending 8:")
for i in L:
    print (f"{i}")
print(f"After remove last")
L.pop()
for i in L:
    print (f"{i}")
print("First 2 elements :",L[:2])


print("SET OPERATIONS")
SET1={1,3,5}
SET2={2,4,6}
SET1.add(6)
print(f"{SET1}")
SET2.remove(4)
print(f"{SET2}")

v,f=True,False

print(v or f)    #or
print(v and f)    #and
print(v != f)     #xor
print(not f)    #not



dic={'name':'rashi','class':12,'city':'arrekode'}
print(f"{dic['name']}")
print('cat' in dic)
dic['phone']=8589912982
print(f"{dic}")


print("String manipulation")

word1="hello"
word2=" world"
w3="hello world"
print(f"{word1+word2}")
print("'hello world' length :",len(w3))
print("'hello world' uppercase :",w3.upper())
print("'hello world' capitilize :",w3.capitalize())
print(w3.rjust(5))
print(w3.center(7))
print(w3.replace('hello','hi'))
print(w3.strip('h'))
