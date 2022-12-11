with open("input.txt") as file:

    # separo il primo blocco rispetto alle istruzioni
    # split legge tutto il file e lo divide in due \n\n
    # strip legge la riga ed elimina gli elemnti dichiarati esempio \n
    stack_strings, instructions = (i.splitlines() for i in file.read().strip("\n").split('\n\n'))

## creo un dictionary a cui assegnare le colonne (stack) da 1 a 9
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}
## creo un indice numerico per lgli stack (da 0 a 8)
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]
# funzione usata per mostrare il contenuto di ciascun stack
def display_stacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")


def load_stacks():
    for string in stack_strings[:-1]:
        stack_number = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_number].insert(0, string[index])
            stack_number += 1

def empty_stacks():
    for stack_number in stacks:
        stacks[stack_number].clear()

def get_stacks_ends():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer 

load_stacks()

# ==== PART 1 ===
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]
    
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for crate in range(crates):
        create_removed = stacks[from_stack].pop()
        stacks[to_stack].append(create_removed)
    
print("risposta parte 1", get_stacks_ends())


## ==== PART 2 ===
empty_stacks()
load_stacks()

for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]
    
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    crates_to_remove = stacks[from_stack][-crates:] # trovo i crane da rimuovere
    stacks[from_stack] = stacks[from_stack][:-crates] # rimuovo crates

    for crate in crates_to_remove:
        stacks[to_stack].append(crate) #aggiungomi crate al nuovo stack


display_stacks()
print("risposta parte 2", get_stacks_ends())