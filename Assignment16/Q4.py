# 4. Write a function in Python to read lines from a text file "notes.txt".
# Your function should find and display the occurrence of the word "the".
# For example:
# If the content of the file is:
# "India is the fastest-growing economy. India is looking for more investments around the globe.
# The whole world is looking at India as a great market.
# Most of the Indians can foresee the heights that India is capable of reaching."
# The output should be 5.

with open("notes.txt", "w") as fw:
    fw.writelines(
        "Python is a high-level, general-purpose programming language. "
        "Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule. "
        "Python is dynamically typed and garbage-collected. "
        "It supports multiple programming paradigms, including structured (particularly procedural), "
        "object-oriented and functional programming. "
        "It is often described as a 'batteries included' language due to its comprehensive standard library. "
        "Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language "
        "and first released it in 1991 as Python 0.9.0. "
        "Python 2.0 was released in 2000. Python 3.0, released in 2008, "
        "was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, "
        "released in 2020, was the last release of Python 2. "
        "Python consistently ranks as one of the most popular programming languages. "
        "Python users are colloquially called pythonistas. "
        "The python is the best language")
    fw.close()


def count_occ():
    cnt = 0
    with open("notes.txt", "r") as fr:
        for x in fr:
            # print(x.split())
            for i in x.split():
                if i == 'the' or i == 'The':
                    cnt += 1
        print(cnt)


count_occ()
