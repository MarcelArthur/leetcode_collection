# -*- coding:utf-8 -*-
def slist(st):
    return [x for x in st]

Kaka ='PAYPALISHIRING'
print(slist(Kaka))

LK = [[x + 3 * k for x in range(1, 4)] for k in range(3) ]
print(LK)

# 质数列表
Lz = [x for x in range(1, 10) for b in range(2, x) if x % b == 0]


def status(s, numRows):
    length = len(s)
    Kipp = [x for x in s]
    if length == 0 or numRows <= 2 :
        return s
    ret = ''

    lag = 2 * numRows - 2
    for i in range(0, numRows):
        for j in range(i, length, lag):
            ret += Kipp[j]
            if (i > 0) and (i <numRows - 1):
                t = j + lag - 2 * i
                if t < length:
                    ret += Kipp[t]
    return ret


if __name__ == "__main__":
    p = 'PAYPALISHIRING'
    a = 'ABCD'
    u = 3
    kj = status(a, u)
    print(kj)



