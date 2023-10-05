#WEEK 2 , BUILT IN FUNCTIONS

# #PROBLEM 2
# numbers = set()
# for i in range(5):
#   try:
#     num = int(input("Enter num: "))
#     numbers.add(num)
#   except TypeError:
#     print()
#     exit()
# print(min(numbers))

# #OPTION 2
# numbers = set()
# for i in range(5):
#   num = input("Enter your number: ")
#   if not num.isdigit:
#     print("Incorrect input")
#     exit()

#   numbers.add(int(num))

# print(min(numbers))

# functions = {"print":print, "all": all, "slice": slice}
# user_choice = input("Enter your function: ")
# if user_choice not in functions.keys():
#   print("Function doesn't exist")
#   exit()


# functions[user_choice]("This is print function : hello")

# #PROBLEM 3
# dict = {"name": "john", "lastname": "Snow", 12: "age"}
# for x in dict.keys():
#   try:
#     x +'abc'
#   except:
#     x = str(x)
#     x += "abc"

#   print(x)

# # Task 1
# list_1 = ['name', 'age', '1', '19', '35' , 'python']
# def split_list(input):
#   range = int(len(input) / 2)
#   first_list = input[0:range]
#   second_list = input[range:]
#   print(first_list)
#   print(second_list)
# split_list(input = list_1)

# #Zada4a 2
# import random
# def gen_number():
#   code = "0444"
#   for digit in range(6):
#     num = random.choice("145790")
#     code += num
#   return code
# print(gen_number())


# #Task FIBONACCHI
# def fibo():
#   list = [0,1]
#   a = 0
#   b = 1
#   for x in range(8):
#     c = a + b
#     a = b
#     b = c
#     list.append(c)
#   print(list)
# fibo()

##Week 2, Modules
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random_names = set()
# while len(random_names) < 3:
#   new_name = random.choice(names)
#   random_names.add(new_name)

# print(random_names)

# #TASK 3
# import sys
# print(os.name)

#Task 5
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# group1 = ""
# group2 = ""
# group3 = ""
# group4 = ""
# counts = round(len(names) / 4)

