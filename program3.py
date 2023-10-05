from_file = open("/Users/tatoshkin/Desktop/python/scripts/task3.txt", "r")
readed_file = from_file.read()
print(readed_file)
print(from_file.read())
if "w" in readed_file or "W" in readed_file:
    print("W is in this file") 
else:
    print("W is not in this file")

