# # print multiplication table of given number:
# # using while loop
# num = int(input("Enter a number: "))
# i =1 
# while i<=10:
#     print(f"{num} x {i} = {num*i}")
#     i += 1

# # using for lopp
# num = int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# Write a program to find the factorial of a given number.
num = int(input("Enter a number:"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"The factorial of {num} is {fact}")