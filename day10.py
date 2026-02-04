# functions: block of code that performs specific task and run only when it is called

# function with no parameter but no ruturn value

# def greet():
#     print("Hello World!")

# greet()

# function with parameter but no return value
# def greet(name):
#     print(f"Hello {name}")

# greet("Hem")

# function with no parameter but return value
# def greet():
#     return ("My name is Hem.")

# x = greet()
# print(x)
# print(greet())

# function with parameter but return value
# def greet(name):
#     return(f"My name is {name}")

# print(greet("Raj"))

# def add(a,b):
#     sum = a+b
#     return (f"The sum of {a} and {b} is {sum}")

# print(add(2,3))

# default argument functions

# def greet(name="Hem"):
#     print(f"Hello {name}")

# greet()
# greet("Hari")

# keyword argument functions
# def student(name, age):
#     print(name, age)

# student(age=45, name="Hari")

# variable length arguments
def add(*num):
    print(num)
    total=0
    for i in num:
        total+=1
    return total
print(add(1,2,3,4))

# variable lenght
def greet(*name):
    for i in name:
        print(f"Hello {i}")
greet("Hem", "Raj")

# keyword variable length arguments
def student(**data):
    print(data)
    for k, v in data.items():
        print(k, ":", v)
    
student(name="Hem", age=23)