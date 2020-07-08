# https://www.hackerrank.com/challenges/most-commons/problem
if __name__ == '__main__':
    s = input()
    count = {}
    for i in s:
        count[i] = count.get(i, 0) + 1
    
    new_count = []
    for k, v in count.items():
        new_count.append( (v, k) )

    new_count.sort(reverse = True)

    rv = []
    index = 0
    while index != len(new_count)-1:
        num = new_count[index][0]
        l = []
        for i in new_count:
            if i[0] == num:
                l.append(i)
        l.sort()
        for i in l:
            if i not in rv:
                rv.append(i)
        index += 1
    print(rv)
    n = 0
    while n != 3:
        print(f'{rv[n][1]} {rv[n][0]}')
        n += 1