# leggere lista txt
with open('input.txt', 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]
    total_calories_list = []
    total_calories = 0
    for line in lines:
        #print(line)
        if line != '':
            total_calories += int(line)
        else:
            total_calories_list.append(total_calories)
            total_calories = 0
            #print(total_calories)
    
    #print(total_calories_list)
    max_calorias = max(total_calories_list)
    #print("-----------------------------------")
    print("max calorias", max_calorias)

    ### ottenere top 3 e somma della top tre
    sortes_total_calories_list = sorted(total_calories_list, key=int, reverse=True)
    #print(sortes_total_calories_list)
    top_three_total = sum(sortes_total_calories_list[:3])
    print("top three sum", top_three_total)





