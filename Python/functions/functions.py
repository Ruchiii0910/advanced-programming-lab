# simple function 
def greet():
    print("Hello, World!")

greet()

# function with parameters
def greet(name):
    print("Hello", name)

greet("Ruchita")

#function with return value 
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# function with default arguments
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Ruchita")

# function to check even or odd number 
def check_number(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_number(10)

# function for multiplication of two numbers
def multiply(a, b):
    return a * b

print(multiply(5, 4))

# function with no argument and no return value
def message():
    print("Welcome to Python")

message()