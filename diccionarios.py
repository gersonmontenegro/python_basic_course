my_dict ={
    'David': 35,
    'Erika': 32,
    'Jaime': 50
}

# print(my_dict['Erika'])
# print(my_dict.get('Juan', 20))
# print(my_dict.get('Jaime', 20))

# reasign
my_dict['Jaime'] = 20
# add new key
my_dict['GRS'] = 41
# remove
del my_dict['David']
# iterate by key
# for key in my_dict.keys():
#     print(f'{key} = {my_dict[key]}')
# iterate by value
# for value in my_dict.values():
#     print(f'{value}')
# iterate by value and key
# for key, value in my_dict.items():
#     print(f'{key} = {value}')
# print(my_dict)
# search in the dict
# res = 'David' in my_dict
# print(res)
# res = 'Erika' in my_dict
# print(res)

# dict comprehension

dict_double = {k:v*2 for(k, v) in my_dict.items()}
print(dict_double)
dict_filter = {k:v for(k, v) in my_dict.items() if v > 20}
print(dict_filter)