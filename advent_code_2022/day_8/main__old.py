import os

with open('test.txt', 'r') as file:
    data = file.read().split('\n')

print(data)

len_horizontal = len(data[0]) #lunghezza riga
len_vertical = len(data) #lunghezza colonna


def check_from_left_to_right(line, position, tree):
    for l in range(0, position):
        #print(line[l])
        if int(tree) <= int(line[l]):
            return False
            break
    return True

def check_from_right_to_left(line, position, tree):
    for l in range(position, len(line)):
        #print(line[l])
        if int(tree) <= int(line[l]):
            #print(line[l])
            return False
            break
    return True

def check_from_top_to_bottom(position_row, position_colum, tree):
    for index in range(0, position_row):
        #print("row index", data[index])
        columm = data[index][position_colum]
        if int(tree) <= int(columm):
            return False
            break
    return True

def check_from_bottom_to_top(position_row, position_colum, tree):
    for index in range(position_row, len(data)):
        #print("row index reverse", data[index])
        columm = data[index][position_colum]
        if int(tree) <= int(columm):
            return False
            break
    return True

counter = 0
for index_row in range(0, len(data)):
    print("index row", index_row)
    line = data[index_row]
    for index_column in range(0, len(line)):

        is_visible_from_left = check_from_left_to_right(line, index_column, line[index_column])
        print(line[index_column] + " is_visible_from_left ", is_visible_from_left)
        is_visible_from_right = check_from_right_to_left(line, index_column,  line[index_column])
        print(line[index_column] + " is_visible_from_right ", is_visible_from_right)

        is_visible_from_top = check_from_top_to_bottom(index_row, index_column, line[index_column])
        print(line[index_column] + " is_visible_from_top ", is_visible_from_top)
        is_visible_from_bottom = check_from_bottom_to_top(index_row, index_column, line[index_column])
        print(line[index_column] + " is_visble_from_bottom ", is_visible_from_bottom)

        if is_visible_from_left or is_visible_from_right or is_visible_from_top or is_visible_from_bottom:
            counter = counter + 1
        
        print("counter", counter)

'''
for index_row in range(0, len(data)):
    line = data[index_row]
    for index_column in range(0, len(line)):
        is_visible_from_left = check_from_left_to_right(line, index_column, line[index_column])
        print("is_visible_from_left", is_visible_from_left)
        is_visible_from_right = check_from_right_to_left(line, index_column, line)
        print("is_visible_from_right", is_visible_from_right)
        is_visible_from_top = check_from_top_to_bottom(index_row, index_column, line[index_column])
        print("is_visible_from_top", is_visible_from_top)
        is_visible_from_bottom = check_from_bottom_to_top(index_row, index_column, line[index_column])
        print("is_visble_from_bottom", is_visible_from_bottom)
        if is_visible_from_left or is_visible_from_right or is_visible_from_top or is_visible_from_bottom:
            counter = counter + 1

'''

print(counter)
        


