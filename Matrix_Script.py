# URL : https://www.hackerrank.com/challenges/matrix-script/problem
# Not completed - working
import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()
n, m = int(first_multiple_input[0]), int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ''.join(matrix[word][counter] for counter in range(m) for word in range(n))

# for counter in range(m):
#     for word in range(n):
#         letter = matrix[word][counter]
#         s += letter
print( s,end='')
