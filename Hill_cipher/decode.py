import numpy as np


"""
    Реализация расширенного евклидова алгоритма.
    Возвращает целое число x y и НОД(a,b) 
    ax + by = НОД(a, b)
"""
def gcd_extended(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return (x, y, a)

def true_reverse(key, alphabet):
    key_true_rev = np.linalg.inv(key)  # обратная
    det = round(np.linalg.det(key))  # определитель
    key_true_rev = np.round(key_true_rev * det)
    x, y, a = gcd_extended(len(alphabet), round(det) % len(alphabet))
    key_true_rev *= y
    key_true_rev = np.round(key_true_rev) % len(alphabet)
    return key_true_rev

def hill_decode(phrase, alphabet, key):
    key_true_rev = true_reverse(key, alphabet)
    n = len(key)
    if len(phrase) % n != 0:
        raise TypeError('Неверная фраза ')
    ans = ''
    block = list()
    for i in range(len(phrase)):
        block.append(alphabet.find(phrase[i]))
        if i % n == n - 1:
            block = np.array(block)
            block = block.dot(key_true_rev)
            for elem in block:
                ans += alphabet[int(elem) % len(alphabet)]
            block = list()
    return ans


def req_hill_decode(phrase, alphabet, key1, key2):
    n = len(key1)
    if len(phrase) % n != 0:
        raise TypeError('Неверная фраза')
    ans = ''
    block_count = 0
    block = list()
    for i in range(len(phrase)):
        block.append(alphabet.find(phrase[i]))
        if i % n == n - 1:
            block = np.array(block)
            if (block_count == 0):
                key = key1
            elif (block_count == 1):
                key = key2
            else:
                key = np.round(key2.dot(key1)) % len(alphabet)
                key1, key2 = key2, key
            key = true_reverse(key, alphabet)
            block = block.dot(key)
            for elem in block:
                ans += alphabet[int(elem) % len(alphabet)]
            block = list()
            block_count += 1
    return ans
