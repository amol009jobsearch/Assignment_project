'''
2. What is the difference between:
a = 10
b = 10
and
a = [10]
b = [10]
Explain using id().
'''

#a = [10]
#b = [10] 

a = 10
b = 10

print(f"a = : {a}, id {id(a)}")
print(f"b = : {b}, id {id(b)}")

if id(a) == id(b):
    print("Immutable object")
else:
    print("Mutable object")    

'''
Immutable objects may share memory; mutable objects always get their own memory unless explicitly referenced.

a = 10 and b = 10 are Immutable objects
a = [10] and b = [10] are mutable objects they will always get their own memory

'''