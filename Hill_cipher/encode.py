import numpy as np

def hill_encode(phrase, alphabet, key):
    n = len(key)
    while (len(phrase) % n != 0):
        phrase += '.'
    ans = ''
    block = list()
    for i in range(len(phrase)):
        block.append(alphabet.find(phrase[i]))
        if i % n == n - 1:
            block = np.array(block)
            block = block.dot(key)
            for elem in block:
                ans += alphabet[int(elem) % len(alphabet)]
            block = list()
    return ans

def req_hill_encode(phrase, alphabet, key1, key2):
    n = len(key1)
    while (len(phrase) % n != 0):
        phrase += '.'
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
            block = block.dot(key)
            for elem in block:
                ans += alphabet[int(elem) % len(alphabet)]
            block = list()
            block_count += 1
    return ans
