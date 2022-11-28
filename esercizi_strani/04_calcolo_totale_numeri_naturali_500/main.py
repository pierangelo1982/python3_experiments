def test_one():
    totale = 0
    for i in range(500):
        totale += i
    print(totale)

def test_two():
    totale = 0
    for i in range(0,500):
        totale += i
    print(totale)

def test_three():
    totale = sum(range(0, 500))
    totale_due = sum(range(500))
    print(totale)
    print(totale_due)

def test_four():
    totale = (499*500)/2
    print(totale)

test_one()
test_two()
test_three()
test_four()
