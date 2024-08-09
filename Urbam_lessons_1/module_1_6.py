# Работа с словарями:

my_dict = {'Erzhan': 2003, 'Oleg': 1996, 'Anya': 1944}
print('Dict:', my_dict)

print('Existing value:', my_dict['Erzhan'])

print('Not existing value:', my_dict.get('Urban'))

my_dict.update({'Gosha':2020,'Roza':1880})

get_ = my_dict.pop('Oleg')
print('Deleted value:',get_)

print('Modified dictionary:',my_dict)

print(' ')# Отступ

# Работа с множествами:

my_set = {1,5,'Argus',5,'trump','trump'}
print('Set:',my_set)

my_set.add(7)
my_set.add('Winner')
my_set.discard(5)
print('Modified set:',my_set)