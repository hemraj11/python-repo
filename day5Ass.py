# palindrom number 121
num = 121
rev = 0
temp = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome Number")

# program to ignore multiple of 3 (1,22)
for i in range(1, 22):
    if i % 3 ==0:
        continue
    print(i, end=" ")

# program to print 5 odd number betweeen 1-20
count=0
for i in range(1,20):
    if i % 2 == 0:
        continue
    print(i, end=" ") 
    if count==5:
        break

# program to find sum of even number from 1 to n
n=int(input("Enter a number:"))
sum=0
for i in range(1,n):
    if i%2 !=0:
        continue
    print(i)
    sum=sum+i
print("Sum of even numbers:",sum)


# program to find 1st number divisible by 7 between 1-100
for i in range(1,100):
    if i % 7 != 0:
        continue
    print("1st number divisible by 7 is:",i)
    break
