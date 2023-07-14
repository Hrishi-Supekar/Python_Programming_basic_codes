# 3. Write a function in Python to count and display the total number of words in a text file.
def read_total_no_of_words():
    sum = 0
    with open("story.txt", "r") as fr:
        for x in fr:
            y = x.split()
            le = len(y)
            sum += le
        print(sum)


read_total_no_of_words()
