# -*- coding:utf-8 -*-


def kmp(str):
    next = [None for x in range(len(str))]
    next[0] = -1
    next[1] = 0
    j, k = 1, 0

    while j < len(str) - 1:
        if str[j] == str[k]:
            next[j+1] = k+1
            j += 1
            k += 1
        elif k == 0:
            next[j+1] = 0
            j += 1
        else:
            k = next[k]
    print(next)

if __name__ == '__main__':
    kmp('aaaaaaaadtesadtesadtes')





