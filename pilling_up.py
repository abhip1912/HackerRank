#  https://www.hackerrank.com/challenges/merge-the-tools/problem

def check(n, sL):
    if ( sL[0] == max(sL) or sL[-1] == max(sL) ):
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    T = int( input() )
    for _ in range(T):
        n = input()
        sideLength = list( map( int, input().split() ) )
        check(n, sideLength)