import numpy as np
import math


# не работает с большими числами, так как math.ceil не может найти корень большого числа

# находит значение k для sqrt((s+k)^2 - n), где s - окр.вверх корень из n
def attack(n):
    s = math.ceil(np.sqrt(n))
    k = 0
    while True:
        value = (np.sqrt((pow(s + k, 2)) - n))
        k += 1
        if value.is_integer():
            print(k, value)
            break
    return k, value


def is_sqrt(number):
    x = number
    y = (x + number // x) // 2
    while y < x:
        x = y
        y = (x + number // x) // 2
    return x


def isqrt(n):
    return int(n ** .5)


# нахождение p q
def fermat(n, verbose=True):
    a = is_sqrt(n)
    b2 = a ** 2 - n
    b = isqrt(n)
    count = 0
    while b ** 2 != b2:
        if verbose:
            a += 1
            b2 = a ** 2 - n
            b = isqrt(b2)
            count += 1
    p = a + b
    q = a - b
    assert n == p * q
    return p, q

def s(n):
    return is_sqrt(n)


def get_keys(p, q, e):
    fi = (p - 1) * (q - 1)
    d = 1
    while (e * d) % fi != 1:
        d += 1

    return e, d


def main():
    print('Введите пару (e, n): ')
    e, n = map(int, input().split())
    print('Итерация и значение k для взлома: ' + str(attack(n)))
    print('Значение s: ' + str(s(n)))
    print('Найденные значения (p, q): ' + str(fermat(n)))
    print('Введите (p, q): ')
    p, q = map(int, input().split())
    print('Полученный резуельтат (e, d): ' + str(get_keys(p, q, e)))


# print(fermat(781))
if __name__ == '__main__':
    main()
# print(attack(
#    178542003245811211274167228297361192303886321036074276889145691522634525820185614278499562592134188995169731066418203258297035264969457638591284906658912408319763156912951486020761069099132619194489006875108217247513715271974383296142805846405783845170862140174184507256128825312324419293575432423822703857091))
# print(attack(781))
