# 7: Return the count of a given substring from a string
msg = "Emma is a good developer. Emma is a writer. She works at a good mnc in india"
checkword = input("Enter the word to check in the string:")


def check_char_present(msg1):
    cnt = 0
    l = list(msg1.split())
    print(l)
    for i in l:
        if i == checkword:
            cnt += 1
    print(f"{checkword} appeared {cnt} times!!!")


check_char_present(msg)
