# Dictionary: collection of data stored in key: value pair

student = {
    "name": "Ram",
    "age": 20,
    "address": "Dhangadhi"
}
print(student)

# properties:
# Mutable
# key-value pair
# keys are unique
# values can be duplicate
# unordered

# accessing values
# using key
student = {"name": "Ram", "age": 20, "address": "Dhangadhi" }
print(student["name"])

# using get() method
print(student.get("name"))

# looping through dictionary

# looping through key
for k in student:
    print(k)

# loping through value
for v in student.values():
    print(v)

# both
for k, v in student.items():
    print(k, v)

# methods in dictionary
# get()
# keys()
# values()
# items()

print(student.get("name"))
print(student.keys())
print(student.values())

# update existing data
student.update({"name": "Hari"})
print(student)

# insert new data
student.update({"roll": 2})
print(student)

# pop()
student.pop("name")
print(student)

# popitem()
student.popitem()
print(student)

# clear()
student.clear()
print(student)

# copy()
student1 = student.copy()
print(student1)

# fromkeys()
keys = ["a", "b", "c"]
d = dict.fromkeys(keys)
print(d)

d = {}

n = int(input("How many data? "))
for i in range(1, n+1):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    d[name]= age

print(d)

# converting list to dictionary
ls = [["Ram", 21], ["Shyam", 24]]
print(dict(ls))

# searching
d = {
    "name":["Ram", "shyam","Hari"],
    "age": [21, 23, 32]
}

found = False
for i in d["name"]:
    if i.lower()=="shyam":
        print("Found")
        found=True

if not found:
    print("Not Found")