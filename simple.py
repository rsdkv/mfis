import math


# шифрование
def simple_encode(phrase, alphabet, key):
    ans = ''
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) != -1:  # поиск буквы, -1, если не найдена в алфавите
            ans += key[alphabet.find(phrase[i])]  # добавление элементов по ключу
        else:
            ans += phrase[i]
    return ans


# дешифрование
def simple_decode(phrase, alphabet, key):
    ans = ''
    for i in range(len(phrase)):
        if key.find(phrase[i]) != -1:
            ans += alphabet[key.find(phrase[i])]
        else:
            ans += phrase[i]
    return ans


def simple_key_check(key, alphabet):
    if (len(key) != len(alphabet)):
        raise TypeError('Неправильная длина параметра (length)')
    for i in range(len(key)):
        if key.find(key[i]) != key.rfind(key[i]) or alphabet.find(key[i]) == -1:
            raise TypeError('Invalid key (symbols)')
