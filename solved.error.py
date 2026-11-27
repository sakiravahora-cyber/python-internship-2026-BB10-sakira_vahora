#q1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum:", sum)

#q2
length = 10
width = 5

area = length * width

print("Area:", area)

#q3
for i in range(1, 11):
    print(i)
    
#q4
number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
#q5
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[-1])

#q6
def square(number):
    result = number * number
    return result

print(square(6))

#7
numbers = [10, 15, 20, 25, 30, 35]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Even Sum:", total)

#8
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
    
#9
marks = [80, 75, 90, 65, 70]

total = 0

for mark in marks:
    total += mark

percentage = total / (len(marks) * 100) * 100 if marks else 0

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)

#10
cart = [
    ["Keyboard", 800],
    ["Mouse", 400],
    ["USB Cable", 200]
]

total = 0

for item in cart:
    total += item[1]

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)