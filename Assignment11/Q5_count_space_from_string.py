# 5.Count the number of spaces in a string.
msg = "This is hrishikesh supekar from pune i am studying python programming!"
# cnt = 0
# for x in msg:
#     if x == " ":
#         cnt += 1
# # print(f"The count of spaces is:{cnt}")
spaces = len([x for x in [x.count(" ") for x in msg] if x == 1])
print(f"The count of spaces is:{spaces}")
