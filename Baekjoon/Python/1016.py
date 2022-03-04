import sys


def eratos(minimum, maximum):
    global no_sqr

    result = maximum - minimum + 1

    i = 2
    while i * i <= maximum:
        temp = minimum // (i ** 2)
        if minimum % (i ** 2):
            temp += 1
        
        while temp * (i ** 2) <= maximum:
            if nono[temp * (i ** 2) - minimum]:
                nono[temp * (i ** 2) - minimum] = False
                result -= 1
            temp += 1
        i += 1
    return result
        
minimum, maximum = map(int, sys.stdin.readline().split())
nono = [True for i in range(maximum - minimum + 1)]
print(eratos(minimum, maximum))
