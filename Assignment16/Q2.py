# 2. Write a function in python to count the number of lines from a text file "story.txt"
# which is not starting with an alphabet "T".
# Example:
# If the file "story.txt" contains the following lines:
# A boy is playing there.
# There is a playground.
# An airplane is in the sky.
# The sky is pink.
# Alphabets and numbers are allowed in the password.
# The function should display the output as 3.

with open("story.txt", "w") as fw:
    fw.writelines("The pilot and the passenger got into the plane.\n"
                  "It was a small plane.\n"
                  "It had one engine.\n"
                  "It was an old plane.\n"
                  "The pilot started the engine.\n"
                  "Are you okay?,he asked the passenger\n"
                  "She said she was okay.\n"
                  "They were flying to an island.\n"
                  "The island was only 30 minutes away.\n"
                  "It would be a short flight.\n"
                  "She was a nurse.\n"
                  "Her husband was a doctor.\n"
                  "The doctor was on the island.\n"
                  "The doctor needed some medicine.\n"
                  "She had the medicine in her bag.\n"
                  "The medicine would save a young boy.\n"
                  "The young boy was very sick.\n"
                  "The plane took off.\n"
                  "The engine sounded funny.\n"
                  "The pilot frowned.\n"
                  "Is everything okay?,the passenger asked.\n"
                  "I am afraid not,said the pilot.\n"
                  "There's something wrong with the engine and we have to land.\n"
                  "He landed the plane.\n"
                  "The nurse got out of the plane.\n"
                  "She looked around the airport.\n"
                  "She saw another plane.\n"
                  "This plane had two engines.\n"
                  "She walked over to the plane.\n"
                  "Is this a new plane or an old plane?,she asked the pilot.\n"
                  "The pilot said it was a new plane.\n"
                  "Good,she said.\n"
                  "Please take me to the island.")
    fw.close()


def read_story():
    cnt = 0
    with open("story.txt", "r") as fr:
        for x in fr:
            if x[0] != "T":
                cnt += 1
        print(f"The count of lines not starting with 'T':{cnt}")


read_story()
