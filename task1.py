url  = "./database.txt"
database = open(url, "r")

usernames = {}
print(usernames)

login = input("Enter your username: ")

for lines in database.readlines():
	users,password,access = line.split()[0:3]
	usernames[users] = password, access
if login not  in usernames:
	print("Username doesn't exists")	
	exit()

password = input("Enter your password: ")
if password == usersnames.get(login)[0]:
	print("Welcome",usernames.get(login)[1])
	
else:
	print("Continue your registranion")


print(database)




