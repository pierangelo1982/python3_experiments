names = ['Numa', 'Tullo', 'Anco']
surnames = ['Pompilio', 'Ostilio', 'Marzio']

def test_one():  
    index = 0
    dictionary_list = []
    
    for item in names:
        dictionary = {
            'nome': item,
            'cognome': surnames[index]
        }
        dictionary_list.append(dictionary)
        index += 1

    print (dictionary_list)

def test_two():
    list = []
    for name, surname in zip(names,surnames):
        list.append({'name': name, 'surname': surname})
    
    print(list)

def test_three():
    list = [{'name': name, 'surname': surname} for name, surname in zip(names, surnames)]
    print (list)

test_one()
test_two()
test_three()
