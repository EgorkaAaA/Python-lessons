from functools import lru_cache
from functools import partial
from functools import wraps
from functools import total_ordering
import time

# Задание №1
print('Задание №1')
def calc_sum(list):
    if not list:
        return 0
    else:
        summ = calc_sum(list[1:])
        summ = summ + list[0]
        return summ
list_in = [1, 2, 3, 4, 5]
print('Входной список: ', list_in)
print('Сумма: ', calc_sum(list_in))

# Задание №2
print('Задание №2')
def fibonacci(n, list):
    count = len(list)
    if len(list)<2:
        return []
    num1 = list[count - 2]
    num2 = list[count - 1]
    if (num1 + num2) < n:
        list = list + [num1 + num2]
        return fibonacci(n, list)
    else:
        return list

n = 50
list_in = [0, 1]
print('Максимальная сумма: ', n)
print('Начальный список: ', list_in)
list_out = fibonacci(n, list_in)
print("Полученный список: ", list_out)

# Задание №3
print('Задание №3')
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print([fib(n) for n in range(100)])

# Задание №4
@total_ordering
class Student:
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

# Задание №5
print('Задание №5')
def logger(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start = time.time()
        f(*args, **kwds)
        print(f.__name__ + " отработал за ", time.time() - start)
    return wrapper

@logger
def print_hello_world():
    time.sleep(1)
    print('Hello world!')
print_hello_world()

# Задание №6
print('Задание №6')
list_in = [1, 2, 3, 4, 5, 6]
list_out = list(map(lambda x: pow(x, 4), list_in))
print('Полученный список: ', list_out)

# Задание №7
print('Задание №7')
list_in = [1, 2, -3, 4, -5, -6]
print('Начальный список: ', list_in)
list_out = list(map(lambda x: x > 0, list_in))
print('Полученный список: ', list_out)

# Задание №8
print('Задание №8')
text_in = 'Hello World!'
print('Начальный текст: ', text_in)
list_out = list(map(lambda x: ord(x), text_in))
print('Полученный список: ', list_out)

# Задание №9
print('Задание №9')
def cipher(text_in):
    print(''.join(list(map(lambda x: chr(ord(x) - 1), text_in))))

cipher('Ifmmp!xpsme"')