
def get_input_data():
    file =  open('input.txt', 'r')
    lines = [line.replace('\n', '') for line in file.readlines()]
    return lines

lines = get_input_data()
pairs = 0

for line in lines:
    first, second = line.split(',')

    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    #print(first, second)

    if first[0] <= second[0] and first[1] >= second[1]:
        pairs += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        pairs += 1

print("risposta 1", pairs)

print("*************************")


overlapping = 0

for line in lines:
    first, second = line.split(',')

    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] is range(second[0], second[1]+1) or first[1] in range(second[0], second[1]+1):
        overlapping += 1
    elif second[0] is range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1):
        overlapping += 1

print(overlapping)
