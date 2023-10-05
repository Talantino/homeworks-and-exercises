name = input("Enter your name of the file: ")

import os.path
def create_file(file_name):
    if os.path.isfile(file_name):
        print("the file already exists")
        return

    open(file_name, "w").close()
    # with open(file_name, "w")as file:
    #     pass
print(create_file(name))
