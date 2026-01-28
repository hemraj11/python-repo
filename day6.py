# list-- it is the colection of items which is ordered, chmngable and allows duplicate values

myList = [10,20,50,70]
print(myList)  # [10, 20, 50, 70]

fruits = ["apple", "orange", "mango"]
print(fruits[1])
print(fruits[-1])

multi = [[1,3,5], [2,4,6,8]]
print(multi[0][1])


# method of list: append(), insert(), remove(), pop(), sort(), reverse(), len(), clear(), count(), index()
numbers = [10,5,8,3,6]
numbers.append(12)
print(numbers)  # [10, 5, 8, 3, 6, 12]

numbers.insert(2, 15)
print(numbers)  # [10, 5, 15, 8, 3, 6, 12]

numbers.remove(3)
print(numbers)  # [10, 5, 15, 8, 6, 12]

popped_value = numbers.pop()
print(popped_value)  # 12

numbers.sort()
print(numbers)  # [5, 6, 8, 10, 15]

numbers.reverse()
print(numbers)  # [15, 10, 8, 6, 5]

length = len(numbers)
print(length)  # 5

numbers.clear()
print(numbers)  # []

fruits = ["apple", "banana", "apple", "orange", "banana"]
count_apple = fruits.count("apple")
print(count_apple)  # 2

index_orange = fruits.index("orange")
print(index_orange)  # 3

