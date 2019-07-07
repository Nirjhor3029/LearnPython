course = "Python's Course for Beginners"
print(course)

course = 'Python Course for "Beginners"'
print(course)

course = 'Python\'S Course for "Beginners"'
print(course)

course = '''
    Hey Nir,
        This is me.
        
'''
print(course)

course = 'Python Course for Beginners'

print(course[2])
print(course[1])
print(course[0])
print(course[-1])
print(course[-2])
# Advance
print('[0:3]=> '+course[0:3])
print('[0:]=> o to infinity =>  '+course[0:])
print('[1:]=> 1 to infinity =>  '+course[1:])

print('[:5]=> start to 5 =>  '+course[:5])

print('[:]=> All Character =>  '+course[:])

# Magic
name = "Nirjhor"
print(name[1:-1])

# Class 6
first = 'john'
last = 'smith'
message = first + ' [' + last + '] is a coder'
print(message)

msg =  f'{first} [{last}] is a coder '

print(msg)


# Class 7
print(len(msg))
print(message.capitalize())
print(message.upper())

# find the position of a character
print(message.find('o'))

# try to find total sequence
print(message.find('smeth'))

print(message.replace('john', 'Nirjhor'))

# That will change all the 'i' to 'e'
print(message.replace('i', 'e'))

is_have = 'john' in message
print(is_have)




