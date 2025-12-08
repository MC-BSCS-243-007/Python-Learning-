# # ##################################### Getting Started with Python ###################################

# # Install Python from https://www.python.org/downloads/
# # Install IDE (Integrated Development Environment) like VSCode
# # Create a new Python file with .py extension (e.g., first.py)
# # open terminal or command prompt
# # Navigate to the directory where your Python file is located using 'cd' and press tab key for auto-completion
# # PS C:\Users\HC\Desktop\.py\PY.code>  python first.py
# # To check Python version installed
# # PS C:\Users\HC\Desktop\.py\PY.code> python --version

# ##################################### Getting Started with Python ######################################


# ### Python Basics                   


# Printing Hello World
print("Hello World")

# Printing single value
print(3)

# Printing multiple values
print(3,2,1)

# Printing the sum of values
print(3+2+1)

#  Printing number and string
print("name ",3+3)


# Variables
A = 22
B = 33
C = A + B
print(C)

# Printing name and age
age = 23
name = "Khan"
print(name,":",age)
print(age)

# Multiple variable assignment
A,B,C = "Orange","Banana","Apple"
print(A,B,C)

# List of fruits
Fruit = ["Orange","Banana","Apple"]
print(Fruit)
print(type(Fruit))

# Range of numbers
X=range(10)
print(X)
print(type(X))

# Dictionary to store student information
Student={
    "Name":"M.Abdul Wassay Khan",
    "Reg#":"MC-BSCS-243-007",
    "CGPA":"3.75",
    "Email":"mawk@example.com",
    "Phone":"123-456-7890",
    "Address":"123 Main St, Multan, Pakistan",
}
print(Student)
print(type(Student))
print(Student["Name"])
print(len(Student))

# Single line comment

'''
Multi-line comment
This is a multi-line comment
'''

# Boolean values

print(10<5)
print(8==7)
print(5>2)

# Declaration of variables of integer data types

a,b,c,d,e,f,g,h,i,j= 1,2,3,4,5,6,7,8,9,10
print(a,b,c,d,e,f,g,h,i,j)

# Getting input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name:",name)
print("Age:",age)

# Python Operators
# Arithmetic Operators
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3
print("x after += 3:", x)
x *= 2  # Equivalent to x = x * 2
print("x after *= 2:", x)
x -= 4  # Equivalent to x = x - 4
print("x after -= 4:", x)
x /= 2  # Equivalent to x = x / 2
print("x after /= 2:", x)
x %= 3  # Equivalent to x = x % 3
print("x after %= 3:", x)
x **= 4  # Equivalent to x = x ** 4
print("x after **= 4:", x)
x //= 3  # Equivalent to x = x // 3
print("x after //= 3:", x) 

# Conditions in python
a=12
b=11
if a > b :
    print("a is greater then b ")


realage = 23
fakeage = 23
if realage > fakeage:
    print("real age is :",realage)
elif realage > fakeage:
    print("fake age is:",fakeage) 
elif realage == fakeage :
    print("real age is equals to fake age")
else :
    print("real age is :",realage)

# # Loops in python
# for i in range(5):
#     print("Iteration number:", i)
# count = 0
# while count < 5:
#     print("Count is:", count)
#     count += 1



# print number 1 to 10 using while loop
i = 1
while i <= 10:
        print(i)
        i += 1
# print number 10 to 1 using while loop
i = 10
while i >=1:
        print(i)
        i -= 1


# print My name 5 times using while loop
a=1
while a <= 5:
        print("Abdul-Wassay,Khan")
        a += 1

# Print Sum of numbers from 10 to 1

i = 10
while i >=1:
        print("Sum :",i+i)
        i -= 1

# Nested Loops in Python
for i in range(1, 4):  # Outer loop 
    for j in range(1, 4):  # Inner loop
        print(f"i: {i}, j: {j}")

# break and continue statements
for i in range(1, 11):
    if i == 6:
        break  # Exit the loop when i is 6
    print("Break Example - Current number:", i)
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print("Continue Example - Current number:", i)


# defining & calling a function
def greet(name):
    print("Hello,", name)
greet("Wassay")
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)

# Function Parameters (positional, keyword, default, *args, **kwargs)
def describe_person(name, age=30, *hobbies, **attributes):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print("Hobbies:", hobbies)
    print("Attributes:", attributes)
describe_person("Alice", 25, "Reading", "Traveling", height=165, weight=60)

# returning multiple values from a function
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result
sum_val, diff_val = calculate(10, 5)
print("Sum:", sum_val)
print("Difference:", diff_val)

# scope of variables (local and global)
global_var = "I am a global variable"
def my_function():
    local_var = "I am a local variable"
    print(local_var)
    print(global_var)
my_function()
print(global_var)
# print(local_var)  # This will raise an error because local_var is not defined globally  
print ("---------------------------------------------------")











# #<!-------------------------------------- End of Python Basics ------------------------------------------!># #


