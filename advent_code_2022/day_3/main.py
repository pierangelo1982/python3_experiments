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

print(totale)