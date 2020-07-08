# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations as pmut

if __name__ == '__main__':
    ip = input()
    s, n= ip.split()
    l = list( pmut(s, int(n)) )
    l.sort()
    for i in l:
        print( ''.join(i) )
