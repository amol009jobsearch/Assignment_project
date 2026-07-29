'''
1.Write a program to display:
• Value
• Type
• Memory address
for a variable using appropriate built-in functions.
'''

#Note : Type built in function used to display the type of variable
# Id function is used to display the address
name = "Sachin"
age = 50
height = 5.4


print(f"name : {name} , type : {type(name)} and id: {id(name)}")
print(f"age : {age} , type : {type(age)} and id: {id(age)}")
print(f"height : {name} , type : {type(height)} and id: {id(height)}")