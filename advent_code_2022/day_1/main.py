# leggere lista txt
with open('input.txt', 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]
    total_calories_list = []
    total_calories = 0
    for line in lines:
        print(line)
        if line != '':
            total_calories += int(line)
        else:
            total_calories_list.append(total_calories)
            total_calories = 0
            print(total_calories)
    
    print(total_calories_list)
    max_calorias = max(total_calories_list)
    print("-----------------------------------")
    print(max_calorias)




