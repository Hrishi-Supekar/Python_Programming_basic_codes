# sample list - fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# 5.make a list that contains each fruit with exactly 5 characters.


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
n_list=[]
for i in fruits:
    if len(i) == 5:
        n_list.append(i)
print(n_list)