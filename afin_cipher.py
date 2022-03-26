# шифрование аффинного шифра. ax + b mod m ,m = |A|
def afin_encode(phrase, a, b, alphabet):
    encrypted = ''
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) != -1:
            encrypted += alphabet[(a * alphabet.find(phrase[i]) + b) % len(alphabet)]
        else:
            encrypted += phrase[i]
    return encrypted


# дешифрование аффинного шифра
def afin_decode(phrase, a, b, alphabet):
    decrypted = ''
    reverse = reverse_element(a, alphabet)
    for i in range(len(phrase)):
        if alphabet.find(phrase[i]) != -1:
            decrypted += alphabet[reverse * (alphabet.find(phrase[i]) - b) % len(alphabet)]
        else:
            decrypted += phrase[i]
    return decrypted


# нахождение обратного элемента
def reverse_element(a, alphabet):
    rev = 0
    while ((rev * a) % len(alphabet) != 1):
        rev += 1
    return rev
