import json

with open("words.json", encoding='utf-8') as keywords:
    Data = json.load(keywords)

for i in Data:
    print(i)

print('- '*10)

if "Dólar" in Data[-1]:
    print("Dólar está caríssimo.") 

with open("words.json", encoding='utf-8') as datajson:
    Data = json.load(datajson)