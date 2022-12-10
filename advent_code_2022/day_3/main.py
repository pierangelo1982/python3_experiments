import string

alphabet = list(string.ascii_letters)
print(alphabet)
print(alphabet.index('p') + 1)

def letter_value(letter):
    return int(alphabet.index(letter) + 1)

def get_input_data():
    file =  open('input.txt', 'r')
    lines = [line.replace('\n', '') for line in file.readlines()]
    return lines

""" def get_duplicate_items_list(items):
    x = [item for item in set(items) if items.count(item) > 1]
    return x """

lines = get_input_data()

totale = 0
for line in lines:
    line_len = len(line)
    line_part_1 = line[:line_len//2]
    line_part_2 = line[line_len//2:]
    print(line)
    print(line_part_1)
    print(line_part_2)

    for char in alphabet:
        if char in line_part_1 and char in line_part_2:
            totale += letter_value(char)

print("risposta 1", totale)

## -------------------------------------------------------------- ##

j = 3
total_sum = 0
for i in range(0, len(lines), 3):
    rucksacks = lines[i:j]
    j += 3
    print(rucksacks)

    for char in alphabet:
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            total_sum += letter_value(char)


print("risposta 1", totale)
print("risposta 2", total_sum)

        
