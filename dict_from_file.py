


my_dict = {}

with open('raw_dictionary.txt', 'r') as file:
    for line in file:
        number, letters = line.split()
        my_dict[number] = letters
print(my_dict)






# with open('raw_dictionary.txt', 'r') as file:
#     my_dict = {int(line.split()[0]): line.split()[1] for line in file}

# print(my_dict)