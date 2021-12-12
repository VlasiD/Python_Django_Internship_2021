# Task 1
original = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]
print('Original list:')
print(original)

second_items = [list_[1] for list_ in original]  # gets second items of internal lists

while bool(second_items):
    min_item_index = second_items.index(min(second_items))  # finds index of min element among the second items
    original.append(original[min_item_index])  # adds item with min 2-nd element to the end of list
    del original[min_item_index]  # removes item from its original position
    del second_items[min_item_index]  # removes item from second items list after transposition

print('\nTask 1: Sorted list by second element of internal lists:')
print(original)

# Task 2
dictionary = {}
for list_ in original:
    dictionary[list_[1]] = [list_[0]] + list_[2:]
    # dictionary[list_[1]] = [list_[i] for i in range(len(list_)) if i != 1]     # alternative version

print('\nTask 2: Created dictionary based on sorted internal lists:')
print(dictionary)

# Task 3
for pair in dictionary.items():  # pass through dictionary pairs
    pair[1].sort(reverse=True)  # sorts lists (dictionary values) in descending order
    dictionary[pair[0]] = pair[1]  # overwrites the value in the dictionary

print('\nTask 3: Sorted dictionary values (lists) in descending order:')
print(dictionary)

# Task 4
values_set = set()
for list_ in dictionary.values():
    values_set = values_set.union(list_)  # unites all dictionary values to set

print('\nTask 4: Created set based on all dictionary values:')
print(values_set)

# Task 5
string = str(values_set)
print('\nTask 5: String based on set:')
print(string)
