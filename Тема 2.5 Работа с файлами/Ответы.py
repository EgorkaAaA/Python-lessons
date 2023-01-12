import os

# Задание №1
print('Задание №1')
def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
read_last(5, 'text.txt')

# Задание №2
print('Задание №2')
def tree(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)


tree('1')

# Задание №3
print('Задание №3')
def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            print('Самое большое слово: ', sought_words[0])
        else:
            print('Самые большие слова: ', sought_words)
longest_words('text.txt')