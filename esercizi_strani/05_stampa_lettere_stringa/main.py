list = 'abcdefghi'

def test_one():
    for letter in list:
        print(letter)

def test_two():
    for i in range(len(list)):
        print(list[i])

def test_three():
    listLenth = len(list)
    for i in range(listLenth):
        print(list[i])

test_one()
test_two()
test_three()