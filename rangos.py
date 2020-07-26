# my_range = range(1, 5)
# # print(type(my_range))

# for i in my_range: # not included
#     print(i)

# my_range = range(0, 7, 2)
# my_other_range = range(0, 8, 2)

# for i in my_range:
#     print(f'R1: {i}')

# for x in my_other_range:
#     print(f'R2: {x}')

# print(my_range == my_other_range) # value equality. Only matter the value. In this case, both ranges has the same values

# print(my_range is my_other_range) # object equality

even_range = range(0, 101, 2)
odd_range = range(1, 100, 2)

# for i in even_range:
#     print(f'Even: {i}')

for i in odd_range:
    print(f'Odd: {i}')

