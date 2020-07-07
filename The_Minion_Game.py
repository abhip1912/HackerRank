# URL:  https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):

    ## For visualized the the substrings...
    string = string.upper()
    Kevin = {'total': 0}
    Stuart = {'total': 0}
    for i in range(len(string)):
        for j in range(len(string)+1):
            if i < j:
                s = string[i:j]
                if s[0] in ['A', 'E', 'I', 'O', 'U']:
                    Kevin[s] = Kevin.get(s, 0) + 1
                    Kevin['total'] += 1
                else:
                    Stuart[s] = Stuart.get(s, 0) + 1
                    Stuart['total'] += 1
                    
    if (Kevin['total'] > Stuart['total']):
        winner = f"Kevin {Kevin['total']}"
    elif ( Kevin['total'] == Stuart['total'] ):
        winner = 'Draw'
    else:
        winner = f"Stuart {Stuart['total']}"

    print(winner)
    


    #For just counting the substrings...
    # Kevin = 0
    # Stuart = 0
    # for i in range(len(string)):
    #     if s[i] in 'AEIOU':
    #         Kevin += (len(string)-i)
    #     else:
    #         Stuart += (len(string)-i)

    # if Kevin > Stuart:
    #     print ("Kevin", Kevin)
    # elif Kevin < Stuart:
    #     print ("Stuart", Stuart)
    # else:
    #     print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)