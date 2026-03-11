


# my_string = 'Four score and seven years ago'
# my_string_list = my_string.split()
# print(my_string_list)


# my_name = "Barker, Bob"
# last_name, first_name = my_name.split(', ')
# print(f"First Name: {first_name}\nLast Name: {last_name}")


# name = 'Barker, Bob, Miami, Fl`
# name_split_list = name.split(', ', 2)
# print(name_split_list)
# last_name, first_name, location = name_split_list
# print(f'{first_name} {last_name}, {location}')




# **********EXERCISE*********************
# with open('gettysburg_opening.txt', 'r') as read_file:
#     print(read_file.read())


# with open('gettysburg_opening.txt', 'r') as split_file:
#     text = split_file.read()
#     sentences = text.split('. ')
#     for sentence in sentences:
#         print(sentence + '.')

# ********THIS IS THE FINAL PRODUCT OF THE EXERCISE*************
# with open('gettysburg_opening.txt', 'r') as split_file:
#     text = split_file.read()
#     sentences = text.split('. ')
    
#     with open('output_sentences.txt', 'w') as output_file:
#         for sentence in sentences:
#             output_file.write(sentence + '.\n')
# ***************************************************************



# *****HEYDAR'S******
# with open("my_file.txt" , "r") as my_file:
#     text_1 = my_file.read()

# lines = text_1.split('. ')

# with open ("my_file2.txt", "w") as my_file_2:
#     for line in lines:
#         my_file_2.write(line + "\n")


# ***********13.3*****************************************
# NOTES*************
# my_tuple = ("Apple", "Banana", "Orange")

# output_string = '_'.join(my_tuple)

# print(output_string)

# Output
# Apple_Banana_Orange


# ***********ESERCISE******************

# with open('raw_data.txt', 'r') as split_file:
#     text = split_file.read()
#     avengers = text.split('|')

# avengers = ','.join(avengers)
# print(avengers)
    
# with open('new_data.txt', 'w') as output_file:
#     output_file.write(avengers)

# **********THIS IS CHAT GPT'S VERSION***********
# with open('raw_data.txt', 'r') as input_file:
#     with open('new_data.txt', 'w') as output_file:
#         for line in input_file:
#             line = line.strip()
#             parts = line.split('|')
#             joined_line = ','.join(parts)
#             output_file.write(joined_line + '\n')


# *************13.4 NOTES*********************************

# # Indexes:   0  1  2  3  4  5  6  7  8  9  10  11
# my_string = 'C  o  d  i  n  g     R  o  c  k   s'
# # Negative: -12-11-10-9 -8 -7 -6 -5 -4 -3 -2  -1

# my_string = 'Coding Rocks'
# new_string = my_string[1:5:1]

# print(new_string)


#  print(my_list[::-1])  Will print your list backwards (in other words, right to left).


# ******EXERCISES********************
# 1
# my_string = "Coding in Python is amazing"
# new_string = my_string[10:16]
# print(new_string)

# # 2
# my_tuple = (1, 5, 89, 234, 289, 445, 578, 623, 777, 898, 900)
# print(my_tuple[4:9])
# print(my_tuple[-7:-2])

# # 3
# this_string = "The quick brown fox jumps over the lazy dog"
# that_string = this_string[-33:-18]
# # that_string = this_string[10:26]
# print(that_string)


def sliced(iter_obj, start=0, stop=None, step=1):
    # Handle the case when stop is None, it should be the length of the iterable
    if stop is None:
        stop = len(iter_obj)

    # Create an empty list to store the sliced elements
    sliced_list = []

    # Iterate over the iterable from start to stop with the given step
    for i in range(start, stop, step):
        # Append each element to the sliced_list
        sliced_list.append(iter_obj[i])

    return sliced_list

# Test the function
print(sliced([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Default slice
# print(sliced([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 8, 2)) 