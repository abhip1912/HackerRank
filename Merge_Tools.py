#  https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    length = 0
    while(length != len(string)):
        rv = ''
        for i in range(k):
            rv += string[length]
            length += 1
        new_rv = ''
        for i in rv:
            if i not in new_rv:
                new_rv += i
                
        print(new_rv)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)