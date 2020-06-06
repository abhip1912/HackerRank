##url of problem
##https://www.hackerrank.com/challenges/python-string-formatting/problem

max_bin = len(str(bin(n)[2:])) + 1
for number in range(1, n+1):
    print( str(number).rjust( max_bin - 1 ) + str(oct(number))[2:].rjust( max_bin ) + str(hex(number))[2:].upper().rjust( max_bin )  + str(bin(number)[2:]).rjust(max_bin) )
