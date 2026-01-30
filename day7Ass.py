# Solve the following using list comprehensions
# create a list of even numbers from 1-20
even = [i for i in range(1,21) if i%2==0]
print(f"Even numbers from 1 to 20 are: {even}")

# create a list of odd numbers from 1-20
odd = [i for i in range (1,21) if i%2 !=0]
print(f"Odd numbers from 1 to 20 are: {odd}")

# create a list of square of numbers from 1-20
square = [i * i for i in range(1,21)]
print(f"Square of numbers from 1-20 are: {square}")

# create a list of length of each words in ["apple","orange","kiwi"]
fruits = ["apple","orange","kiwi"]
len_fruits = [len(fruit) for fruit in fruits ]
print(f"Length of each fruits is: {len_fruits}")

# create a list of squares of only even numbers from 1-20
even = [i*i for i in range(1,21) if i%2==0]
print(f"Square of even numbers from 1 to 20 are: {even}")


# create a list of numbers divisible by 3 from 1-100
num_divisible = [i for i in range(1,101) if i%3==0]
print(f"Number divisible by 3 are: {num_divisible}") 