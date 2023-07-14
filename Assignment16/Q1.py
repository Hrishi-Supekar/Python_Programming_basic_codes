# 1. Write a function in python to read the content from a text file "poem.txt" line by
# line and display the same on screen.

with open("poem.txt", "w") as fp:
    fp.writelines("Johnny, Johnny.\n"
                  "Yes, Papa?\n"
                  "Eating sugar?\n"
                  "No, Papa.\n"
                  "Telling lies?\n"
                  "No, Papa.\n"
                  "Open your mouth\n"
                  "Ha! Ha! Ha!")


def file_read():
    with open("poem.txt", "r") as fr:
        print(fr.read())


file_read()
