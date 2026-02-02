# Tuple: it is a collection of data which is ordered and immutable (cannot be changed once decelered)

# tup = (12,11,13,14)
# print(type(tup))
# print(tup)

# tuple with different data types
# tup_data = (23, "Hem", 4.8, True)
# print(tup_data)
# print(type(tup_data))

# tuple with single element must have comma
# t = ("python",)
# print(type(t))

# indexing in tuple
# color = ("red", "blue", "orange","yellow")
# print(color[2])
# print(color[-1])
# print(color[1:3])
# print(color[:3])
# print(color[2:])
# print(color[::-1])


# methods in tuple
# count():how many times an element repeat in tuple
# index(): position of element
# t = (10,52,58,47,12,13)
# print(t.count(47))
# print(t.index(52))
# print(len(t))

# looping in tuple
# color = ("red", "orange", "black")
# for items in color:
#     print(items, end=" ")


# concatination
# t1 = (1,3,5,6)
# t2= (2,3,5,9)
# print(t1 + t2)

# repetation
# t3 = (3,6)
# print(t3 * 3)

# meembership 
# t = (10,20,30)
# print(20 in t)
# print(10 in t)

# unpacking
# t = (10,20,30)
# a,b,c=t
# print(a)
# print(b)
# print(c)

# converting list to tuple and vise versa

# list to tuple
# lst = [2,4,5,6]
# print(type(lst))
# t = tuple(lst)
# print(type(t))

# tuple to list
# tpl = (10,28,67)
# print(type(tpl))
# lst = list(tpl)
# print(type(lst))

# set: collection of unique elements and is unordered and mutable(can be changed)
s = {23,34,543,56}
print(type(s))

# accessing element in set
# for i in s:
#     print(i)

# check if element is in set or not
# if 34 in s:
#     print('Yes')
# else:
#     print("No")

# add element in set
# s.add(56)
# print(s)

# update
# s.update([20,30,40,50])
# print(s)

# remove
# s.remove(56)
# print(s)

# discard()
# s.discard(34)
# print(s)


# pop()
# s.pop()
# print(s)

# clear()
# s.clear()
# print(s)

# union
a = {1,4,5,6,7}
b = {3,4,6,8,9}

# print(a.union(b))
# print(a | b)

# intersecion
# print(a.intersection(b))
# print(a & b)

# difference
# print(a.difference(b))
# print(a-b)

# subset
# print(a.issubset(b))

# superset
# print(b.issuperset(a))

# isdisjoint
# print(a.isdisjoint(b))