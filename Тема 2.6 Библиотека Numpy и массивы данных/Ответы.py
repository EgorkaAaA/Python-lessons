import numpy as np

# Задание №1
print('Задание №1')
print('Полученный массив: ', np.zeros(10))

# Задание №2
print('Задание №2')
print('Полученный массив: ', np.full(10, 2.5))

# Задание №3
print('Задание №3')
print('Полученный двумерный массив: ', np.arange(9).reshape(3,3))

# Задание №4
print('Задание №4')
array = np.random.random((10, 10))
print('Максимум: ', array.max(), 'Минимум: ', array.min())

# Задание №5
print('Задание №5')
array = np.random.random(30)
print('Среднее: ', array.mean())

# Задание №6
print('Задание №6')
print('Произведение: ', np.dot(np.ones((5,3)), np.ones((3,2))))

# Задание №7
print('Задание №7')
array_1 = np.random.randint(0, 2, 5)
print('Первый массив: ', array_1)
array_2 = np.random.randint(0, 2, 5)
print('Второй массив: ', array_2)
print('Равенство: ', np.allclose(array_1, array_2))

# Задание №8
print('Задание №8')
array = np.random.random(10)
print('Начальный массив: ', array)
array[array.argmax()] = 0
print('Полученный масиив', array)

# Задание №9
print('Задание №9')
array = np.arange(100)
print('Начальный массив: ', array)
value = np.random.uniform(0, 100)
print('Искомое число: ', value)
index = (np.abs(array - value)).argmin()
print('Полученное значение: ', array[index])

# Задание №10
print('Задание №10')
n = 3
p = 3
array = np.zeros((n, n))
print('Начальный массив: ', array)
np.put(array, np.random.choice(range(n * n), p, replace=False), 1)
print('Полученный массив: ', array)