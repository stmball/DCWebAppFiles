import json

with open('outfinaltest78.csv') as file:
    data = file.read()
    data = data.split('\n')
    output = []
    for row in data[:-1]:
        row = row.split(',')
        output.append({'time': float(row[0]), 'actual': float(row[1])})

with open('output2.json', 'w') as outfile:
    json.dump(output, outfile)
