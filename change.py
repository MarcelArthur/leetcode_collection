# ~python3
import sys

if __name__ == '__main__':
    for i in sys.stdin:
        v = i.replace('\n', '') 
        print(v[::-1])

