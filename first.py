#1. Positive or Negative
num = int(input("Enter Number: "))

if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")
#2. Even or Odd
num = int(input("Enter Number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
#3. Greater Number Between Two Numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a > b:
    print("Greater Number =", a)
else:
    print("Greater Number =", b)
#4. Eligible to Vote
age = int(input("Enter Age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")
#5. Divisible by 5
num = int(input("Enter Number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
#6. Leap Year
year = int(input("Enter Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
#7. Vowel or Consonant
ch = input("Enter Character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
#8. Largest Among Three Numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)
#9. Grade System
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
#10. Number Between 1 to 100
num = int(input("Enter Number: "))

if 1 <= num <= 100:
    print("Number is in Range")
else:
    print("Number is Out of Range")
________________________________________
Python For Loop
#1. Print 1 to 10
for i in range(1, 11):
    print(i)
#2. Print 10 to 1
for i in range(10, 0, -1):
    print(i)
#3. Even Numbers Between 1 to 20
for i in range(2, 21, 2):
    print(i)
#4. Odd Numbers Between 1 to 20
for i in range(1, 21, 2):
    print(i)
#5. Sum from 1 to 100
total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)
#6. Multiplication Table
num = int(input("Enter Number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#7. Star Pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
Output:
*
* *
* * *
* * * *
* * * * *
#8. Print Each Character of String
name = input("Enter String: ")

for ch in name:
    print(ch)
#9. Factorial Using For Loop
num = int(input("Enter Number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)
#10. Pyramid Pattern
for i in range(1, 6):
    print("*" * i)
Output:
*
**
***
****
*****
________________________________________
#Python While Loop
#1. Print 1 to 10
i = 1

while i <= 10:
    print(i)
    i += 1
#2. Print 10 to 1
i = 10

while i >= 1:
    print(i)
    i -= 1
#3. Even Numbers Between 1 to 20
i = 2

while i <= 20:
    print(i)
    i += 2
#4. Odd Numbers Between 1 to 20
i = 1

while i <= 20:
    print(i)
    i += 2
#5. Sum from 1 to 100
i = 1
total = 0

while i <= 100:
    total += i
    i += 1

print("Sum =", total)
#6. Multiplication Table
num = int(input("Enter Number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
#7. Count Digits
num = int(input("Enter Number: "))

count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits =", count)
#8. Reverse a Number
num = int(input("Enter Number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse =", reverse)
#9. Factorial Using While Loop
num = int(input("Enter Number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial =", fact)
#10. Password Checker
correct_password = "python123"

password = ""

while password != correct_password:
    password = input("Enter Password: ")

print("Login Successful")

