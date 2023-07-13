# sample list - fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# 6.Make a list that contains fruits that have less than 5 characters


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
n_list=[]
for i in fruits:
    if len(i) < 5:
        n_list.append(i)
print(n_list)