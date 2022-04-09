def find_reverse(a, m):
    rev = 0
    while ((rev*a) % m != 1):
        rev += 1
    return rev


# шифрование рекурентного аффинного шифра
def recurent_afin_encode(phrase, a1, a2, b1, b2, alphabet):
    ans = ''
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
            ans += alphabet[(a*alphabet.find(phrase[i]) + b) % len(alphabet)]
        else:
            ans += phrase[i]
    return ans


def recurent_afin_decode(phrase, a1, a2, b1, b2, alphabet):
    ans = ''
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

        rev = find_reverse(a, len(alphabet))
        if alphabet.find(phrase[i]) != -1:
            ans += alphabet[rev*(alphabet.find(phrase[i]) - b) % len(alphabet)]
        else:
            ans += phrase[i]
    return ans
