# Задание №1
print("Задание №1")
dictionary_1 = {'1': 'a', '2': 'b'}
dictionary_2 = {'3': 'c', '4': 'd'}
print("Входной словарь 1: ", dictionary_1)
print("Входной словарь 2: ", dictionary_2)
dictionary_out = dictionary_1.copy()
dictionary_out.update(dictionary_2)
print("Полученный словарь", dictionary_out)

# Задание №2
print("Задание №2")
def create_dict(a, b):
  return {i : i ** 2 for i in range(a, b + 1)}

print("Полученный словарь", create_dict(1,10))

# Задание №3
# Задание №4
# Задание №5