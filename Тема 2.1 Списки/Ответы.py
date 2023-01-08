# Задание №1
print("Задание №1")
list_in = [2, 4, 8]
print("Входной список: ", list_in)
print("Выходной список: ", list_in[::-1])

print("Входной список: ", list_in)
list_in.reverse()
print("Выходной список: ", list_in)

# Задание №2
print("Задание №2")
list_in = ["Егор", "", "Гена", "Валера", "", "Митя"]
print("Входной список: ", list_in)
print("Выходной список: ", list(filter(None, list_in)))

# Задание №3
print("Задание №3")
list_in = [1, 2]
print("Входной список: ", list_in)
list_in[0], list_in[-1] = list_in[-1], list_in[0]
print("Выходной список: ", list_in)

list_in = [1, 2, 3, 4]
print("Входной список: ", list_in)
list_in[0], list_in[-1] = list_in[-1], list_in[0]
print("Выходной список: ", list_in)

# Задание №4
print("Задание №4")
list_in = [1, 2, 3, 4, 5, 6, 7]
print("Входной список: ", list_in)
print("Выходной список: ", [x * x for x in list_in])

# Задание №5
print("Задание №5")
list_in = [1, 2, 3, 4, 5, 6, 7]
print("Входной список: ", list_in)
list_in.sort(key=lambda x: abs(x), reverse=True)
print("Выходной список: ", list_in)