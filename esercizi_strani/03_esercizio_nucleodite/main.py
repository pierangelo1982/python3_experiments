
def test_one():
    nucleotide = input("Inserisci un nucleotide (A,C,G,T)\n")
    if nucleotide == 'A' or nucleotide == 'a':
        print('T')
    elif nucleotide == 'C' or nucleotide == 'c':
        print('G')
    elif nucleotide == 'G' or nucleotide == 'g':
        print('C')
    elif nucleotide == 'T' or nucleotide == 't':
        print('A')

def test_two():
    nucleotide = input("Inserisci un nucleotide (A,C,G,T)\n").capitalize()
    if nucleotide == 'A':
        print('T')
    elif nucleotide == 'C':
        print('G')
    elif nucleotide == 'G':
        print('C')
    elif nucleotide == 'T':
        print('A')

def test_three():
    nucleotide = input("Inserisci un nucleotide (A,C,G,T)\n")
    nucleotide = nucleotide.capitalize()
    if nucleotide == 'A':
        print('T')
    elif nucleotide == 'C':
        print('G')
    elif nucleotide == 'G':
        print('C')
    elif nucleotide == 'T':
        print('A')


test_one()
test_two()
test_three()