def reverse_element(a, alphabet):
    rev = 0
    while ((rev * a) % len(alphabet) != 1):
        rev += 1
    return rev


# шифрование рекурентного аффинного шифра
def recurent_afin_encode(phrase, alphabet, a1, a2, b1, b2):
    encrypted = ''
    for i in range(len(phrase)):
        if i == 0:
            a = a1
            b = b1
        elif i == 1:
            a = a2
            b = b2
        else:
            a = (a1 * a2) % len(alphabet)
            b = (b1 + b2) % len(alphabet)
            a1, a2 = a2, a
            b1, b2 = b2, b

        if alphabet.find(phrase[i]) != -1:
            encrypted += alphabet[(a * alphabet.find(phrase[i]) + b) % len(alphabet)]
        else:
            encrypted += phrase[i]
    return encrypted


# дешифрование рекурентного аффинного шифра
def recurent_afin_decode(phrase, alphabet, a1, a2, b1, b2):
    decrypted = ''
    for i in range(len(phrase)):
        if i == 0:
            a = a1
            b = b1
        elif i == 1:
            a = a2
            b = b2
        else:
            a = (a1 * a2) % len(alphabet)
            b = (b1 + b2) % len(alphabet)
            a1, a2 = a2, a
            b1, b2 = b2, b

        reverse = reverse_element(a, len(alphabet))
        if alphabet.find(phrase[i]) != -1:
            decrypted += alphabet[reverse * (alphabet.find(phrase[i]) - b) % len(alphabet)]
        else:
            decrypted += phrase[i]
    return decrypted