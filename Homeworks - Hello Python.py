#Problem 1:
a = int(input("Enter a number "))
if a % 2 == 0:
  print("even number")
elif a % 2 != 0:
  print("odd number")
if a % 3 == 0:
  print("Bez ostatka")
elif a % 3 != 0:
    print("S ostatkom")
b = 2
total = a ** b
if total >= 1000:
  print(" a > 1000")
else:
  print("Ne bolshe")

#Problem 4
if True:
  print(1)

#Problem 5
a = 10 // 5
b = 10 / 5
if a == b:
    print(a + b)

#Problem 6
number = int(input("Enter a number: "))
if number < 0:
    print(number)
else:
    print("This is a positive number")

#Problem 7 and 8
a = 10
b = 5
if a > 0 and b > 0:
    print("Positive")
if a > b:
    print (a + 2)
else:
    print(b + 2)

# Problem 9
any_number = int(input("Enter a number: "))
if any_number > 0:
    print("Positive number")
elif any_number == 0:
    print ("Zero")
else:
    print("Negative number")

#Problem 10
age = int(input("Enter your age: "))
if age > 18:
    print("Access approved")
elif age <= 4:
    print("Not for kids, access restricted")
else:
    print("Underage")

#Problem 11
var1 = 45
var2 = 6
if var1 % var2 == 0:
    print("It can be divided")
else:
    print("It cannot be divided")

#Problem 12
year = int(input("Enter the year:"))
current_year = 2023
if year < current_year:
    print("PAST YEAR - ", year)
elif year == current_year:
    print("Current Year - ", year)
else:
  print("Future year - ", year)

#Problem 13
year = int(input("Enter your year of birthday: "))
current_year = 2023
age = current_year - year
if age >= 18:
    print("Access approved")
elif age <= 4:
    print("Not for kids, access restricted")
else:
    print("Underage")

#Problem 14
num = 478
num2 = 575
num3 = 222
if num > num2 and num > num3:
    print("num is the maximum")
elif num < num2 and num < num3:
    print("num is the minimum")
elif num2 > num and num2 > num3:
    print("num2 is the maximum")
elif num2 < num3 and num2 < num:
    print("num2 is the minimum")
elif num3 > num2 and num3 > num:
    print("num3 is the maximum")
elif num3 < num2 and num3< num:
    print("num3 is the minimum")

x = 13 ** 2
print(x)
# if x < 172:
#   print(x ** 2)
a = input("Enter a word")
print(a * 2)
