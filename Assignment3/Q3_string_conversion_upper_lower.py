msg = "My name is Hrishikesh"  # string is immutable hence cannot change it
msg1 = ""  # so we use an empty str and concatenate the char in new str.
for i in msg:
    if i.isupper():
        msg1 += i.lower()
    else:
        msg1 += i.upper()
print(msg1)
# print(msg.upper())
# print(msg.lower())
