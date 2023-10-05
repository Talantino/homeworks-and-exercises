login = input("Enter your login: ")
password = input("Enter your password: ")

file = open("./users.txt","w")
file.write(f"{login}, {password}")
file.close()
