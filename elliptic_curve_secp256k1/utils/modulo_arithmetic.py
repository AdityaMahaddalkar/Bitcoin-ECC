import math


def get_modular_inverse(a: int, m: int):
    '''
    Input: a -> int, m -> int
    Output : x, such that ax = 1 (mod m)
    '''
    while a < 0:
        a += m

    x1, x2, x3 = 1, 0, m
    y1, y2, y3 = 0, 1, a

    q = math.floor(x3 / y3)
    t1 = x1 - q * y1
    t2 = x2 - q * y2
    t3 = x3 - q * y3

    while y3 != 1:
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3

        q = math.floor(x3 / y3)
        t1 = x1 - q * y1
        t2 = x2 - q * y2
        t3 = x3 - q * y3

    while y2 < 0:
        y2 += m

    return y2
