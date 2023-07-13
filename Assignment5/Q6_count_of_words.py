para = '''Python is a high-level, general-purpose programming language. 
        Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.
        Python is dynamically typed and garbage-collected. 
        It supports multiple programming paradigms, including structured (particularly procedural), 
        object-oriented and functional programming. It is often described as a "batteries included" 
        language due to its comprehensive standard library'''
# Occurrence of every word in the string:
# l=para.split()
# mydict={}
# for i in l:
#     cnt=l.count(i)
#     mydict.update({i:cnt})
# print(mydict)
# ---------------------------------------------------------------------------------------
# Occurrence of every character in the string:
mydict = {}
for i in para:
    cnt = para.count(i)
    mydict.update({i: cnt})
print(mydict)
