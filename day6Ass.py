# create list of 5 fruits and display it
fruits = ["Apple", "Mango", "Banana", "Orange","Gauva"]
print(fruits)


# print the first and last element of list
print(fruits[0])
print(fruits[-1])

# take 5 numbers from user and store in list
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
    print(numbers)

# add one element at 2nd position of list
num = [2,3,5,6,7,8,9]
num.insert(1, 10)
print(num)


# remove an element from list
numList = [12,3,94,25,6,34,78]
numList.remove(numList[3])
print(numList)

# sort list in descending order
numList.sort()
print(numList)

# reverse a list using slicing
reversed_list = numList[::-1]
print(reversed_list)


# store at least 20 numbers in list and print only even numbers
numbers = []
for i in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("Even numbers in list: ")
for n in numbers:
    if n%2 == 0:
        print(n)

# store at least 20 numbers in list and print only odd numbers
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("Odd numbers in list: ")
for n in numbers:
    if n%2 != 0:
        print(n)

# program to find largest number in list
numbers = [2, 23,34, 44, 1, 7,78]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest number is:", largest)