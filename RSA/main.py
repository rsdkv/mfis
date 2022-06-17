import math  # for math.gcd()


def IsPrime(n):
    a = 2
    while a**2 <= n and n % a != 0:
        a += 1
    return a**2 > n


def get_keys(p, q):
    n = p * q
    fi = (p - 1) * (q - 1)
    while True:
        print('Выберите простое e до', fi, ':')
        e = int(input())
        if math.gcd(e, fi) != 1:
            print('Не простое число, попробуйте снова.')
        else:
            break

    d = 1
    while (e * d) % fi != 1:
        d += 1

    return e, n, d


def encript(e, n, phrase):
    m_list = []
    for i in range(len(phrase)):
        if (ord(phrase[i]) >= n):
            raise TypeError('Недопустимый символ. Попробуйте увеличить n (p и q)')
        m_list.append(ord(phrase[i]))
    c_list = []
    for i in range(len(m_list)):
        c_list.append((m_list[i]**e) % n)
    return c_list


def decrypt(n, d, c_list):
    ans = []
    for i in range(len(c_list)):
        ans.append(chr((c_list[i]**d) % n))
    return ans


def main():
    print('Выберите вариант работы:')
    print('0 -- С помощью использования простых чисел (p, q, e)')
    print('1 -- С помощью открытого и закрытого ключа')
    cipher_type = int(input())
    if cipher_type < 0 or cipher_type > 1:
        raise TypeError('Ошибка: Неизвестный вариант')

    print('Вставьте фразу:')
    phrase = str(input())

    if cipher_type == 0:
        print('Выберите простые p и q :')
        p, q = map(int, input().split())
        if not IsPrime(p):
            raise TypeError(f'{p} не простое')
        if not IsPrime(q):
            raise TypeError(f'{q} не простое')

        e, n, d = get_keys(p, q)

        print(f'Публичный ключ (e, n) это ({e}, {n})')
        print(f'Чтобы не потерять, ваш приватный ключ {d}')

        c_list = encript(e, n, phrase)
        print(f'Шифртекст:\n {c_list}')
        ans = ''.join(decrypt(n, d, c_list))

        print(f'Расшифрование:\n {ans}')

    else:
        print('Введите e, n, d :')
        e, n, d = map(int, input().split())
        c_list = encript(e, n, phrase)
        print(f'Шифртекст:\n {c_list}')
        ans = ''.join(decrypt(n, d, c_list))

        print(f'Расшифрование :\n {ans}')


if __name__ == '__main__':
    main()