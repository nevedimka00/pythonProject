import os
import json
import csv

# class Employee:

#     def __init__(self,name,position):
#         self._name = name
#         self._position=position

#     def __repr__(self):
#         return(f"{self._name} : {self._position}")

#     def to_dict(self):
#         return {
#             "name" : self._name,
#             "position" : self._position
#         }


# file_path = "file_handling/test.txt"
# new_file_path = "file_handling/tetest.txt"
# txt_data = "I like pizza"
file_to_output = "file_handling/output.txt"
file_to_json = "file_handling/output.json"
file_to_csv = "file_handling/output.csv"

# emp = Employee("alik","support")


# print(emp)


# if os.path.exists(file_path):
#     print(f"Location {file_path} exists")
#     if os.path.isfile(file_path):
#         print("thats a file")
#         os.rename(file_path,new_file_path)
# else:
#     print("location doesent exist")

# with open(file=file_to_output,mode="w") as file:
#     file.write(txt_data)
#     print("text is written")

# with open(file=file_to_json,mode="w") as file:
#     json.dump(emp.to_dict(),file,indent=4)
#     print("json created")


# with open(file=file_to_csv,mode="w") as file:
#     writer = csv.writer(file)
#     writer.writerow(emp.__str__())
#     print("csv created")


try:
    with open(file_to_output,mode="r") as file:
        content = file.read()
        print(content)
except: print("File not find")


with open(file_to_json,"r") as file:
    content = json.load(file)
    print(content["name"])

with open(file_to_csv,"r") as file:
    content = csv.reader(file)
    print(content)
    for i in content:
        print(i)