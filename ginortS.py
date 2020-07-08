# https://www.hackerrank.com/challenges/ginorts/problem
# working
def do_this(s, func):
    tmp = []
    for i in s:
        if func(i):
            tmp.append(i)
    tmp.sort()
    rv = ''.join(tmp)
    if func is str.isdigit:
        left = ''
        right = ''
        for i in rv:
            if int(i)%2==0:
                right += i
                continue
            left += i
        rv = left + right
    return rv

if __name__ == '__main__':
    s = input()
    string = ''
    string += do_this(s, str.islower)
    string += do_this(s, str.isupper)
    string += do_this(s, str.isdigit)
    print(string)