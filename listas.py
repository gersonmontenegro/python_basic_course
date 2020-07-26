my_list = [1, 2, 3]
my_list[1] = 99

my_list.append(4)
my_list.append('Grs')

# my_list.pop()

# for i in my_list:
#     print(i)

my_list_copy = my_list
my_list_copy[0] = 114

# print(my_list)
# print(f'1: {id(my_list)}, 2: {id(my_list_copy)}')

# clone the list
# 1
# my_immutable_list = list(my_list)
# my_immutable_list[0] = 814
# print(f'1. {my_list}')
# print(f'2. {my_immutable_list}')
# 2
# my_other_immutable_list = my_list[::]
# my_other_immutable_list[0] = 'Montes'
# print(f'1. {my_list}')
# print(f'2. {my_other_immutable_list}')


# list comprehension
# my_c_list = list(range(100))

# double = [i*2 for i in my_c_list]
# print(double)
# get even values
# even = [i for i in my_c_list if i % 2 == 0]
# print (even)

my_base_list = ['z', 'b', 'a']
# list.extend
# my_base_list.extend(my_list)
# insert
# my_base_list.insert(1, 99)
# sort
# my_base_list.sort()
# print(my_base_list)
second_base = my_base_list[::]
second_base.append([1, 2, 3])
second_base_copy = second_base.copy() # shallow copy
second_base_copy[1] = 'Grs'
second_base_copy[3][1] = 99
print(second_base)
print(second_base_copy)