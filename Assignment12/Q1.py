# 1)write a function that accepts string and counts the number of upper and lower case letter
msg = "My name is Hrishikesh Supekar. I am from pune. I have completed my BE in mechanical engg."


def string_lw_up_cnt(msg1):
    my_dict = {}
    for i in msg1:
        my_dict.update({i: msg1.count(i)})
    print(my_dict)


string_lw_up_cnt(msg)

