# Словари
# Задание №1
print('Задание №1')
dictionary_1 = {'1': 'a', '2': 'b'}
dictionary_2 = {'3': 'c', '4': 'd'}
print('Входной словарь 1: ', dictionary_1)
print('Входной словарь 2: ', dictionary_2)
dictionary_out = dictionary_1.copy()
dictionary_out.update(dictionary_2)
print('Полученный словарь', dictionary_out)

# Задание №2
print('Задание №2')
def create_dict(a, b):
  return {i : i ** 2 for i in range(a, b + 1)}

print('Полученный словарь', create_dict(1,10))

# Задание №3
print('Задание №3')
list_1 = [1, 2, 3, 4]
list_2 = ['a','b', 'c', 'd']
print('Воходной лист 1: ', list_1)
print('Воходной лист 2: ', list_2)
dictionary_out = dict(zip(list_1, list_2))
print('Полученный словарь: ', dictionary_out)

# Задание №4
print('Задание №4')
dictionary = {'1': 200, '2': 300, '3': -150, '4': 3517}
print('Входной словарь 1: ', dictionary)
sum = 0
for key in dictionary:
  sum += dictionary[key]

print('Сумма: ', sum)

# Задание №5
print('Задание №5')
text = 'text in my txet'
print('Строка: ', text)
dictionary_out = {i: text.count(i) for i in text}
print('Полученный словарь: ', dictionary_out)

# Кортежи
print()
print('Кортежи')
# Задание №1
print('Задание №1')
tuple_1 = (18, 2, 1, 300, 9)
print('Входной кортеж: ', tuple_1)
print('Полученный кортеж: ', tuple(sorted(tuple_1)))

# Задание №2
print('Задание №2')
tuple_in = (1,2,3,4,1,3,4,5)
index = 1
print('Входной кортеж: ', tuple_in)
print('Индекс: ', index)

def slicer(tuple_in, index):
  if index in tuple_in:
    if tuple_in.count(index) > 1:
      first = tuple_in.index(index)
      second = tuple_in.index(index, first + 1) + 1
      return tuple_in[first:second]
    else:
      return tuple_in[tuple_in.index(index):]
  else:
    return ()
print('Полученный кортеж: ', slicer(tuple_in, index))

# Задание №3
print('Задание №3')
list_in = [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 9, 0 ,0 ,0 ,0]
print('Входной лист: ', list_in)
tuple_out = []
[tuple_out.append(item) for item in list_in if item not in tuple_out]
print('Полученный кортеж: ', tuple(tuple_out))

# Задание №4
print('Задание №4')
tuple_in = (
    ('Егор', 2.2),
            ('Аня', 3.6),
            ('Миша', 3.5),
            ('Женя', 4.2),
            ('Вася', 5.0),
            ('Петя', 4.0),
            ('Володя', 4.3),
            ('Евгений', 4.6),
)
print('Входной кортеж: ', tuple_in)
def find_student(tuple_in, mark):
    tuple_out = [student[0] for student in tuple_in if student[1] >= mark]
    print('Полученный кортеж: ', tuple(tuple_out))
find_student(tuple_in, 3)

# Множества
print()
print('Множества')
# Задание №1
print('Задание №1')
def set_and_power(*lists):
    print('Входные данные: ', lists)
    big_list = []
    for list in lists:
        big_list.extend(list)
    set_out = set(big_list)
    print('Полученное множество: ', set_out, ', мощность: ', len(set_out))

set_and_power(
    [1, 2, 3, 4],
    [2, 5, 6, 7, 4]
)

# Задание №2
print('Задание №2')
set_1 = {3, 4, 5, 6, 20}
set_2 = {4, 6, 7, 8, 9}
set_3 = {5, 3, 8, 1}
print('Входные данные: ', set_1, set_2, set_3)
print('Полученная разность: ', set_1 ^ set_2 ^ set_3)

# Задание №3
print('Задание №3')

def super_set(super_set, *sets):
    print('Предпалогаемое супермножество: ', super_set)
    print('Входные данные: ', sets)
    for set in sets:
        if super_set > set:
            print('Множество: ', super_set, ' является супер множеством для: ', set)
        else:
            print('Множество: ', super_set, ' не является супер множеством для: ', set)
super_set({1, 2, 3, 4, 5, 6, 7, 8}, {1, 2, 3}, {9, 0})

# Задание №4
print('Задание №4')
def find_repeat(list):
    print('Входной лсит: ', list)
    index = 0
    while index < len(list):
        cnt = list.count(list[index])
        if cnt > 1:
            list[index] = str(list[index]) * cnt
        index += 1

    print('Полученное множество: ', set(list))
find_repeat([1, 2, 4, 4, 4])