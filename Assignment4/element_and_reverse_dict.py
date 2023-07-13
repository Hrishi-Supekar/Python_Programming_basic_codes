l = ["john", "blake", "martin", "scott", "smith", "mom", "madam"]
r_dict = {}
for x in l:
    r_dict.update({x: x[::-1]})
print(r_dict)
