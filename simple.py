# шифрование
def simple_encode(phrase, alphabet, key):
    encrypted = ''
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) != -1:  # поиск элемента, возвращает -1, если элемент не найден в алфавите
            encrypted += key[alphabet.find(phrase[i])]  # добавление элементов по индексу ключа
        else:
            encrypted += phrase[i]
    return encrypted


# дешифрование
def simple_decode(phrase, alphabet, key):
    decrypted = ''
    for i in range(len(phrase)):
        if key.find(phrase[i]) != -1:
            decrypted += alphabet[key.find(phrase[i])]
        else:
            decrypted += phrase[i]
    return decrypted


# проверка ключа для шифра простой замены
def simple_key_check(key, alphabet):
    if (len(key) != len(alphabet)):
        raise TypeError('Неправильная длина ключа ')
    for i in range(len(key)):
        if key.find(key[i]) != key.rfind(key[i]) or alphabet.find(key[i]) == -1:
            raise TypeError('Ошибка заданного алфавита ')




