
mylist = ["milano", "parigi", "berlino", "londra", "madrid", "lisbona"]
country_list = ["italy", "france", "germany", "england", "spain", "portugal"]



for count, value in enumerate(mylist, start=1):
    print(count, value)

index_city = [dict({"index": count, "name": value}) for count, value in enumerate(mylist, start=1)]
print(index_city)

print("----------------------------------------------------------------")

for c in index_city:
    print(c['name'], c['index'])

print("----------------------------------------------------------------")

dictionary_list = []
for index, city in enumerate(mylist, start=1):
    dic = dict({
        "Name": city,
        "index": index,
        "info": [dict({"index": count, "name": value}) for count, value in enumerate(country_list, start=1)]
    })
    dictionary_list.append(dic)

print(dictionary_list)


