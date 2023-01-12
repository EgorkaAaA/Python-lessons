# Задание №1
print('Задание №1')
def to_list(text):
    print('Входной текст: ', text)
    list_out = []
    for char in text:
        list_out.append(ord(char))
    print('Полученный массив: ', list_out)
to_list('Hello world!')

# Задание №2
print('Задание №2')
def cipher(text):
    new_text = ''
    for char in text:
        new_text += chr(ord(char) + 1)
    print(new_text)

cipher('Hello world!')

# Задание №3
print('Задание №3')
def big_text(*texts):
    print('Входные данные: ', texts)
    big_str = ''
    for text in texts:
        if len(text) > len(big_str):
            big_str = text
    print('Самая большая строка: ', big_str)
big_text('123', '1234', '1')

# Задание №4
print('Задание №4')
def small_number(digits):
    print('Входные данные: ', digits)
    small_digit = 1000000
    for digit in digits:
        if pow(digit, 2) < pow(small_digit, 2):
            small_digit = digit
    print('Самый маленький квадрат у числа: ', small_digit)
small_number([100, 22, 33, 45])

# Задание №5
print('Задание №5')
def sum_of_big_and_small(digits):
    print('Входные данные: ', digits)
    digits.remove(max(digits))
    digits.remove(min(digits))
    print(sum(digits))
sum_of_big_and_small([1, 66, 99, 32])