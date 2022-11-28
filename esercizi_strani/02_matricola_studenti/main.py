def test_one():
    personal_data = {
        'name': 'Pierangelo', 
        'surname': 'Orizio',
    }
    personal_data['matricola'] = '00001'
    print(personal_data)
    personal_data['exams'] = [
        {'exam': 'exam 1', 'vote': 100},
        {'exam': 'exam 2', 'vote': 75},
        {'exam': 'exam 3', 'vote': 50},
        {'exam': 'exam 4', 'vote': 25},
    ]
    print(personal_data)

def test_two():
    personal_data = {
        'name': 'Pierangelo', 
        'surname': 'Orizio',
    }
    personal_data['matricola'] = '00001'
    exams = [
        {'exam': 'exam 1', 'vote': 100},
        {'exam': 'exam 2', 'vote': 75},
        {'exam': 'exam 3', 'vote': 50},
        {'exam': 'exam 4', 'vote': 25},
    ]
    personal_data['exams'] = exams
    
    print(personal_data)

test_one()
test_two()