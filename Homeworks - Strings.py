# Class 3 - strings
# Task 0
sen = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
print(sen[0:len(sen)//2].upper())
print(sen[len(sen)//2:].lower())
# option 2
print("{}{}".format(sen[0:len(sen)//2].upper(),  sen[len(sen)//2:].lower()))
#option 3
print(f"{sen[0:len(sen)//2].upper()}{sen[len(sen)//2:].lower()}")

# #Task 1
first_boolean = "True"
second_boolean = str(True)
print(first_boolean)
print(second_boolean)

# #Task 2
symbol = input("enter a symbol: ")
string = 'GitHub'
print(symbol.join(string))

#Task 3
str5 = "Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500
зараженных систем"
print(str5.replace("е", "3"))

#Task 4
username = input("Enter your name: ")
movie = input("Enter your favorite movie: ")
print("Hello " + username)
print(movie + " ,  is a dope movie")

# # second option:
# print("hello {}, the best movie {}".format(username, movie))

#Task 5
string = "Google создаст специальную команду для поиска багов в особо важных приложениях."
word_count = len(string.split())
print(word_count)

#Task 6
str6 = "Самые важные собЫтия в миРе инфосека за сентябрь"
print("|".join(str6))

#Task 7
str3 = "хакеры слили в сеть данные пакистанской энергетической компании k-Electric"
print(str3.title())
