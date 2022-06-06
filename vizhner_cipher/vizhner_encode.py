def vizh_encode(phrase, alphabet, key):
    while(len(key) < len(phrase)):
        key += key
    ans = ''
    for i in range(len(phrase)):
        ch_num = alphabet.find(phrase[i]) + alphabet.find(key[i])
        ch_num %= len(alphabet)
        ans += alphabet[ch_num]
    return ans

def vizh_open_encode(phrase, alphabet, key):
    if len(key) != 1:
        raise TypeError("Invalid key (len)")
    key += phrase
    ans = vizh_encode(phrase, alphabet, key)
    return ans

def vizh_cipher_encode(phrase, alphabet, key):
    if len(key) != 1:
        raise TypeError("Invalid key (len)")
    ans = ''
    ch_num = alphabet.find(phrase[0]) + alphabet.find(key[0])
    ch_num %= len(alphabet)
    key += alphabet[ch_num]
    ans += alphabet[ch_num]
    for i in range(len(phrase) - 1):
        ch_num = alphabet.find(phrase[i+1]) + alphabet.find(key[-1])
        ch_num %= len(alphabet)
        key += alphabet[ch_num]
        ans += alphabet[ch_num]
    return ans
