# URL : https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    ## Normal way
    # re = 96 + size
    # for i in range(size):
    #     for k in range(size-i, 1, -1):
    #         print('--', end='')
    #     for j in range(i):
    #         print(chr(re-j), end='-')
    #     for l in range(i, -1, -1):
    #         if l == 0:
    #             print(chr(re-l), end='')
    #         else:
    #             print(chr(re-l), end='-')
    #     for k in range(size-i, 1, -1):
    #         print('--', end='')
    #     print()

    # for i in range(size-1):
    #     for k in range(1, i+2):
    #         print('--', end='')
    #     for j in range(0, size-i-1):
    #         if size-i-1 == 1:
    #             print(chr(re-j), end='')
    #         else:
    #             print(chr(re-j), end='-')
    #     for l in range(size-i-3, -1, -1):
    #         if l == 0:
    #             print(chr(re-l), end='')
    #         else:
    #             print(chr(re-l), end='-')
    #     for k in range(1, i+2):
    #         print('--', end='')
    #     print()

    ## Optimized & simple way
    import string
    alpha = string.ascii_lowercase
    n = size
    l = []
    for i in range(n):
        s = '-'.join(alpha[i:n])
        aa = (s[::-1]+s[1:]).center(4*n-3, "-")
        l.append( aa )
    print( '\n'.join( l[:0:-1]+l ) )

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
