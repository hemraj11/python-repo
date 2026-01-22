# WAP to enter 2 number and display greater number
num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))
if num1>num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")


# Wap to check if number lies between 1 to 100
num = float(input("Enter a number:"))
if 1<num<100:
    print(f"{num} lies between 1 to 100")
else:
    print(f"{num} does not lie between 1 to 100")

# Wap to check if user's age is less than 18
age = int(input("Enter your age:"))
if age<18:
    print("User age less than 18")
else: 
    print("User age is 18 or more")


# Wap to check if username and password is correct
username = input("Enter your name:")
password = input("Enter your password:")
if username=="admin" and password=="password123":
    print("Login successful")
else:
    print("Invalid username or password")
