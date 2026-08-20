# lambda function
square = lambda x: x * x

print(square(5))

# lambda function for even and odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(11))

# lambda for multiplication 
multiply = lambda a, b: a * b

print(multiply(5,3))

# lambda function with two arguments 
add = lambda a, b: a + b

print(add(10,40))

# lambda function with map() 
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared) 
