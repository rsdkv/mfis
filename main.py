import math
from simple import simple_encode, simple_decode, simple_key_check
from afin_cipher import afin_encode, afin_decode
from recurent_afin import recurent_afin_encode, recurent_afin_decode

def main():
    print('Программа принимает только нижний регистр! ')
    print('Выберите шифр: ')
    print('1 - Шифр простой замены ')
    print('2 - Аффинный шифр ')
    print('3 - Аффинный рекурентный шифр ')

    variant_cipher = int(input())
    if variant_cipher < 1 or variant_cipher > 3:
        raise TypeError('Неизвестный вариант шифра')

    print('Выберите язык: ')
    print('1 - RUS')
    print('2 - ENG')
    language = int(input())
    if language == 1:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    elif language == 2:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    else:
        raise TypeError('Неизвестный язык')

    print('Шифрование - 1')
    print('Дешифрование - 2')
    cipher_mode = int(input())
    if cipher_mode < 1 or cipher_mode > 2:
        raise TypeError('Неизвестная операция')

    print('Вставьте фразу:')
    phrase = str(input())

    if variant_cipher == 1:
        print('Введите ключ:')# пример для RUS: шщъыьэюяабвгдеёжзийклмнопрстуфхцч
        key = str(input())  # пример для ENG: yzabcdefghijklmnopqrstuvwx
        simple_key_check(key, alphabet)
        if (cipher_mode == 1):
            print(simple_encode(phrase, alphabet, key))
        else:
            print(simple_decode(phrase, alphabet, key))

    elif variant_cipher == 2:
        print('Введите ключ (a, b):')
        a, b = map(int, input().split())
        if math.gcd(a, len(alphabet)) != 1:
            raise TypeError('Invalid key')

        if cipher_mode == 1:
            print(afin_encode(phrase, a, b, alphabet))
        else:
            print(afin_decode(phrase, a, b, alphabet))
    else:
        print('Введите ключ (a1, a2, b1, b2):')
        a1, a2, b1, b2 = map(int, input().split())
        if math.gcd(a1, len(alphabet)) != 1 or math.gcd(a2, len(alphabet)) != 1:
            raise TypeError('Неправильный ключ')

        if cipher_mode == 1:
            print(recurent_afin_encode(phrase, a1, a2, b1, b2, alphabet))
        else:
            print(recurent_afin_decode(phrase, a1, a2, b1, b2, alphabet))


if __name__ == '__main__':
    main()
