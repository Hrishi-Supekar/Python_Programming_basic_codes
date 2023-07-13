# Q) Create a palindrome dictionary
l = ["john", "blake","ava", "martin","otto", "scott", "smith", "mom", "madam"]
p_dict = {}
for x in l:
    if x == x[::-1]:
        # print(f"{x}="palindrome")
        p_dict.update({x: "palindrome"})
    else:
        # print(f"{x}=not palindrome")
        p_dict.update({x: "Not palindrome"})
print(p_dict)