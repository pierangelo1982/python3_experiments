
'''
A = rock -> value 1
B = paper -> value 2
C = scissor -> value 3

lose = 0
draw = 3
won = 6
'''

opponentElement = [
    {
    'name': "rock",
    'key': "A",
    'score': 1,
    },
    {
    'name': "paper",
    'key': "B",
    'score': 2
    },
    {
       'name': "scissor",
        'key': "C",
        'score': 3 
    }
]

meElement = [
    {
    'name': "rock",
    'key': "X",
    'score': 1,
    },
    {
    'name': "paper",
    'key': "Y",
    'score': 2
    },
    {
       'name': "scissor",
        'key': "Z",
        'score': 3 
    }
]

def responseToOpponent(move):
    return ''

def getElelement(key, elements):
     data = [d for d in elements if d['key'] in key]
     return data[0]

def result(opponent, me):
    me = me['name']
    opponent = opponent['name']
    print(opponent, me)
    if opponent == me:
        return 3
    if opponent == "scissor" and me == "rock":
        return 6
    elif opponent == "paper" and me == "scissor":
        return 6
    elif opponent == "rock" and me == "paper":
        return 6
    else:
        return 0

file =  open('input.txt', 'r')
lines = [line.replace('\n', '') for line in file.readlines()]

total_score = 0
move_score = 0
for line in lines:
    #print(line)
    opponent = getElelement(line[0], opponentElement)
    me = getElelement(line[2], meElement)
    #print(opponent['name'] + " vs " + me['name'])
    #print(str(opponent['score']) + " vs " + str(me['score']))
    move_score += int(me['score'])
    total_score += int(result(opponent, me))
    #print(move_score)

print("total score", total_score + move_score)

''' ------------------------------ part 2 --------------------------'''
print("-------------------------------------------------------------")
def resultStrategy(opponent, me):
    print(me)
    if me['key'] == 'Y':
        return getElelement(opponent['key'], opponentElement)
    elif me['key'] == 'X':
        if opponent['key'] == 'A':
            return getElelement('Z', meElement)
        elif opponent['key'] == "C":
            return getElelement("Y", meElement)
        elif opponent['key'] == "B":
            return getElelement("X", meElement)
        else:
            pass
    elif me['key'] == 'Z':
        if opponent['key'] == 'C':
            return getElelement('X', meElement)
        elif opponent['key'] == "B":
            return getElelement("Z", meElement)
        elif opponent['key'] == "A":
            return getElelement("Y", meElement)
        else:
            pass
    else:
        return ''
    
total_score = 0
move_score = 0
for line in lines:
    #print(line)
    opponent = getElelement(line[0], opponentElement)
    me = getElelement(line[2], meElement)
    me_strategy = resultStrategy(opponent, me)
    print(me_strategy)
    move_score += int(me_strategy['score'])
    total_score += int(result(opponent, me_strategy))

print("total score", total_score + move_score)