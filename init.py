user1 = input('Name user 1: ')
ageUser1 = int(input('Age user 1: '))
user2 = input('Name user 2: ')
ageUser2 = int(input('Age user 2: '))

if ageUser1 < ageUser2:
    print(f'{user2} is older than {user1} by {ageUser2 - ageUser1} years')
elif ageUser2 < ageUser1:
    print(f'{user1} is older than {user2} by {ageUser1 - ageUser2} years')
else:
    print(f'{user1} and {user2} are the same age')


#name = input('Please enter your name: ')
#print(f'Welcome, {name}')

# age = int(input('Enter your age: '))
# if age > 40:
#     print('good old')
# elif age > 30:
#     print('good')
# else:
#     print('too young...bye!!')

