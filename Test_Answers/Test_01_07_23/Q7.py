# sample list - fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# 7.Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
n_list = []
for i in fruits:
    n_list.append(len(i))
print(n_list)
