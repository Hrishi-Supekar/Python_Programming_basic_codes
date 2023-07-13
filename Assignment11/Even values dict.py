# 8. Let's assume - I have on dict - original_dict={'jack':38,'James':33,'martin':46,'joe':27}
# print only even values information in given dict means output will be - {'jack':38,'martin':46}

# n = int(input("Enter the number of elements in dict:"))
# my_dict = {input("Enter the key:"): input("Input the value:") for x in range(n)}
my_dict = {input("Enter the key:"): input("Enter the value:") for x in
           range(int(input("Enter the number of elements in dict:")))}
var = {f"{x}:{y}" for x, y in my_dict.items() if int(y) % 2 == 0}
print(var)
