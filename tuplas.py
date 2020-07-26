my_tuple = ()
my_tuple_2 = (1)

my_tuple = (1, 'dos', True)
my_tuple_4 = (99,)
my_tuple_2 = (1,) # int
# my_tuple_2 = (1,) # tuple
# print(type(my_tuple_2))

# print(f'-> {my_tuple[0]}')

# my_tuple[0] = 2 // wecan't

my_tuple_3 = (2, 3, 4)
my_tuple_2 += my_tuple_3
# print(my_tuple_2)
my_tuple_4 += my_tuple_3
# print(my_tuple_4)

x, y, z = my_tuple_3
# print(f'-> {x}-{y}-{z}') // kind of destructuring in python

def coordenadas():
    return (5, 4)

c1, c2 = coordenadas()

print(f'{c1}--{c2}')
