# searching

data = [
    ["Alex", 24, "USA"],
    ["John", 26, "Africa"],
    ["Joy", 26, "Africa"]
]
target_name = input("Enter name to be searched: ").lower()
target_add = input("Enter address to be searched: ").lower()
found = False
for item in data:
    item_name = str(item[0]).lower()
    item_address = str(item[2]).lower()
    if item_name == target_name or item_address == target_add:
        print(f"Found record: Name: {item[0]}, Age: {item[1]}, Address: {item[2]}")
        found = True
if not found:
    print("No matching record found")


# list comprehension
item = [i * i for i in range(1,6)]
print (item)

# taking list 
num = [1,2,3,4,5]
square = [i * i for i in num]
print(square)


#normal way even number
even=[]
for i in range(1,11):
    if i%2==0:
        even.append(i) 
print(even)

# list comprehension way to find even nuumber 
even = [i for i in range(1, 11) if i % 2 == 0]
print(even)

# print value in upper case
fruits = ["orange", "apple"]
new_list = [fruit.upper() for fruit in fruits]
print(new_list)

# input = [1,2,3,4,5]
# output = ['odd', 'even', 'odd','even','odd']

result = ["Even" if i%2==0 else "Odd" for i in range(1,6)]
print(result)


word=["madam", "lol", "level"]
palindrom = [i for i in word if i[::-1]==i]
print(palindrom)