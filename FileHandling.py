# fp = open("newFile.txt", "w")  # will open the file in write mode if exist it will overwrite the content and if not will create new file.
# fp.write("Hello this is hrishikesh")
# fp.writelines("This is new content\n"
#               "hello world\n"
#               "this is python programming")  # will write multiple lines in the file
# fp.write("\nThis is new content again")  # will write single line in file.
# fp = open("newFile.txt", "r")  # will open file in read mode
# print(fp.read()) # read only single line
# print(fp.read(7)) # will read only 7 words from the line.
# print(fp.readlines()) # read all lines and create a list of it.
# for x in fp:
#     print(x)
# for i in fp.readlines():
#     print(i.split())

# [print(i.split()) for i in fp.readlines()] # creating list of single words from line.


# ==============================================================================================================================================
# with open("C:/Users/Hrishikesh/Desktop/Desktop Applications/test.txt","w") as fp:
#     fp.write("Hello this is hrishikesh supekar,")
#     fp.write("I am learning python language,")
#     fp.write("python language is used for DS,ML,AI.")

# with open("C:/Users/Hrishikesh/Desktop/Desktop Applications/test.txt", "a") as fp:
#     fp.write("\nThis is new content")

# with open("C:/Users/Hrishikesh/Desktop/Desktop Applications/test.txt", "w+") as fp:
#     fp.write("\nDjango os the popular python framework for creating website")
#     fp.seek(0)
#     print(fp.tell())
#     print(fp.read())

# with open("C:/Users/Hrishikesh/Desktop/Desktop Applications/test.txt", "r") as fp:
#     fp.seek(4)
#     print(fp.tell())
#     print(fp.read())

# ==============================================================================================================================================
# import os
#
# # path = "C:/Users/Hrishikesh/Desktop/Desktop Applications"
# # print(os.listdir(path))  # will provide list of files present in mentioned dir.
#
# file_path = "C:/Users/Hrishikesh/Desktop/Desktop Applications/test1.txt"
# if os.path.exists(file_path):  # will check if file exist in the give path
#     print("Already exist")
# else:
#     with open(file_path, 'w') as fp:  # if file not exist then will create the file and will write the data in it
#         fp.write("This is first line")

# ==============================================================================================================================================
# Example:
# user_info=input("Please enter the info:")

# try:
#     with open("test.txt","a+") as fp:
#         fp.write(user_info)
#         fp.seek(0)
#         print(fp.read())
# except Exception as e:
#     print("There is a error!!!",e)

import pickle
my_dict={"Name":"Hrishi","Age":27,"City":"Pune"}
try:
    my_dict_obj=open("dict_pickle.pkl","wb")
    pickle.dump(my_dict,my_dict_obj)
    my_dict_obj.close()

    my_dict_obj1=open("dict_pickle.pkl","rb")
    my_dict=pickle.load(my_dict_obj1)
    my_dict.update({input("Enter the key:"):input("Enter the value:")})
    print(my_dict_obj1)
    pickle.dump(my_dict,my_dict_obj)
except Exception:
    print("Error occured")

