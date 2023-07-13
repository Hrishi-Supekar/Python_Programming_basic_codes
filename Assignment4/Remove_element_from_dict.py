# Ask user which key and value pair u want to remove from dict
dict1 = {"name": "Hrishi", "Age": 27, "city": "Pune", "course": "Python"}
k=input("Enter the key to remove key-value pair:")
dict1.pop(k)
print(dict1)