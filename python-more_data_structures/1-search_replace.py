#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy_list.append(replace)
            continue
        copy_list.append(my_list[i])
    return copy_list

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)