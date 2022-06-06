from vizhner_decode import vizh_decode, vizh_open_decode, vizh_cipher_decode
from vizhner_encode import vizh_encode, vizh_open_encode, vizh_cipher_encode


def main():
    print('Выберите шифр:')
    print('1 -- Шифр Виженера')
    print('2 -- Шифр Виженера с самоключом по открытому тексту:')
    print('3 -- Шифр Виженера с самоключом по шифртексту:')
    cipher_type = int(input())
    if cipher_type < 0 or cipher_type > 2:
        raise TypeError('Неизвестный шифр')

    print('Выберите язык:')
    print('1 -- РУС')
    print('2 -- ENG')
    language = int(input())
    if language == 0:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    elif language == 1:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
    else:
        raise TypeError('Неизвестный язык')

    print('Использовать расширенный? -- y/n? (пробел, запятые и т.д.)')
    ext = str(input())
    if ext == 'y' or ext == 'Y' or ext == '1':
        alphabet += ' .,?!'
        print('Вы выбрали расширенный алфавит')
    else:
        print('Вы выбрали стандартный алфавит')

    print('Зашифрование/Расшифрование')
    cipher_mode = int(input())
    if cipher_mode < 0 or cipher_mode > 1:
        raise TypeError('Неизвестный метод')

    print('Вставьте фразу:')
    phrase = str(input())
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) == -1:
            raise TypeError('Невалидная фраза (символ)')

    print('Вставьте ключ:')
    key = str(input())
    for i in range(len(key)):
        if alphabet.find(key[i]) == -1:
            raise TypeError('Невалидный ключ (символ)')

    if cipher_type == 0:
        if cipher_mode == 0:
            print(vizh_encode(phrase, alphabet, key))
        else:
            print(vizh_decode(phrase, alphabet, key))
    elif cipher_type == 1:
        if cipher_mode == 0:
            print(vizh_open_encode(phrase, alphabet, key))
        else:
            print(vizh_open_decode(phrase, alphabet, key))
    else:
        if cipher_mode == 0:
            print(vizh_cipher_encode(phrase, alphabet, key))
        else:
            print(vizh_cipher_decode(phrase, alphabet, key))


if __name__ == '__main__':
    main()
