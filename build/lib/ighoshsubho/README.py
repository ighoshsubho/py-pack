import json

f = open('./ighoshsubho/data.json')

data = json.load(f)

print(data)

f.close()