import numpy as np
import math
from decode import hill_decode, req_hill_decode
from encode import hill_encode, req_hill_encode


def main():
    print('Выберите шифр:')
    print('1 - Шифр Хилла ')
    print('2 - Рекуррентный шифр Хилла  ')
    cipher_type = int(input())
    if cipher_type < 1 or cipher_type > 2:
        raise TypeError('Ошибка: неизвестная команда')

    print('Выберите язык :')
    print('1 - RUS(дополненный)')
    print('2 - ENG(дополненный)')
    language = int(input())
    if language == 1:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,?&'
    elif language == 2:
        alphabet = 'abcdefghijklmnopqrstuvwxyz.,?'
    else:
        raise TypeError('Неизвестный язык')

    print('1 - Зашифрование ')
    print('2 - Расшифрование ')
    cipher_mode = int(input())
    if cipher_mode < 1 or cipher_mode > 2:
        raise TypeError('Ошибка: неизвестная команда')

    print('Вставьте фразу:')
    phrase = str(input())

    print('Вставьте размер матрицы :')
    n = int(input())

    print('Вставьте ключ-матрицу:')
    key = list()
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != n:
            raise TypeError('Неверный размер')
        key.append(row)
    key = np.array(key)
    key = np.round(key) % len(alphabet)
    if math.gcd(int(np.linalg.det(key)), len(alphabet)) != 1:
        raise TypeError('Неверный ключ')

    if cipher_type == 1:
        if cipher_mode == 1:
            print('Шифртекст: ')
            print(hill_encode(phrase, alphabet, key))
        else:
            print('Расшифрованный текст: ')
            print(hill_decode(phrase, alphabet, key))

    elif cipher_type == 2:
        print('Вставьте вторую ключ-матрицу:')
        key2 = list()
        for i in range(n):
            row = list(map(int, input().split()))
            if len(row) != n:
                raise TypeError('Неверный размер')
            key2.append(row)
        key2 = np.array(key2)
        key2 = np.round(key2) % len(alphabet)
        if math.gcd(int(np.linalg.det(key2)), len(alphabet)) != 1:
            raise TypeError('Неверный ключ')
        if (len(key) != len(key2)):
            raise TypeError('Длина второго ключа не соответсвует длине первого')

        if cipher_mode == 1:
            print('Шифртекст: ')
            print(req_hill_encode(phrase, alphabet, key, key2))
        else:
            print('Расшифрованный текст: ')
            print(req_hill_decode(phrase, alphabet, key, key2))


if __name__ == '__main__':
    main()
