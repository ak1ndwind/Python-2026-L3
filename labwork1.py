#excercise 1

import math

radius = float(input("Enter the circle radius: "))
circlearea = math.pi * (radius ** 2)
print(f"Circle area: {circlearea}")

#excercise 2

import math

celsius = float(input("Enter the temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in fahrenheit: {fahrenheit}")

#exercise 3

import math

i = int(input("Enter your number: "))

if i <= 2:
  print(f"{i} is a prime number")
else:
  for a in range(2, i):
    if i % a == 0:
      print(f"{i} is not a prime number")
      break
    else:
      print(f"{i} is a prime number")
      break

#exercise 4

import math

i = int(input("Enter your number: "))
sum = 0
a = 1

if i <= 0:
  print(f"{i} is not a perfect number")
else:
  for a in range(1, i):
    if i % a == 0:
      sum = sum + a
      a = a + 1
    else:
      a = a + 1
      continue
  if sum == i:
    print(f"{i} is a perfect number")
  else:
    print(f"{i} is not a perfect number")

#exercise 5

i = input("What is your favourite color: ")

colors = ["green", "yellow", "red"]
x = colors.index(i)
if i in colors:
  print(f"Your color is at index {x} in my list")
else:
  print(f"Your color is not in my list")

#exercise 6

range1 = range(0, 7)
print("Range 1:", list(range1))
range2 = range(1, 11, 3)
print("Range 2:", list(range2))
range3 = range(5, 0, -1)
print("Range 3:", list(range3))
range4 = range(6, -3, -2)
print("Range 4:", list(range4))

#exercise 7

def remove_dollar_sign():
  return s.replace("$", "")

s = "I have earned $1000 last month."
print(remove_dollar_sign())

#exercise 8

l = [1, 4, 5, -1, 10]

def extract_even():
  i = filter(lambda x: x % 2 == 0, l)
  return list(i)

print(extract_even())

#exercise 9

import math

i = int(input("Enter your number: "))
if i < 0:
  print(f"No negative intergers allowed")

def cac_fac():
  return math.factorial(i)

print(f"The factorial of {i}:", cac_fac())

#exercise 10

import math

i = int(input("Enter your number: "))

for a in range(-i, i + 1):
  if a == 0:
    a += 1
  elif i % a == 0:
    print(f"Division: {a}")
    a += 1
  else:
    a += 1
    continue

#exercise 11

import math

a = float(input("Enter x cordinate of point A: "))
b = float(input("Enter y cordinate of point A: "))
c = float(input("Enter x cordinate of point B: "))
d = float(input("Enter y cordinate of point B: "))

A = (a, b)
B = (c, d)

distance = math.dist(A, B)
print(f"The distance between two points A and B: {distance}")

#exercise 12

m = int(input("Length: "))
n = int(input("Width: "))
