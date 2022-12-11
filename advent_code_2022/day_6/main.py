# 1 - identificare la prima posizione dove le prime 4 lettere ricevute sono TUTTE diverse
# 2 - in particolare, deve riportare il numero di caratteri dall'inizio del buffer alla fine del primo indicatore di quattro caratteri.


file =  open('input.txt', 'r')
# lines = [line.replace('\n', '') for line in file.readlines()]

datastream = file.read()

# === part 1 ===

for i in range(4, len(datastream)):
    s = set(datastream[(i-4):i])
    if len(s) == 4:
        print("answer to part1: ", i)
        break

# === part 2 ===
for i in range(14, len(datastream)):
    s = set(datastream[(i-14):i])
    if len(s) == 14:
        print("answer to part2: ", i)
        break
