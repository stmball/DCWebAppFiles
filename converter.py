import json

with open('outfinaltest78.csv') as file:
    data = file.read()
    data = data.split('\n')
    output = []
    for row in data[:-1]:
        row = row.split(',')
        output.append({'time': row[0], 'actual': row[1]})

with open('output.json', 'w') as outfile:
    json.dump(output, outfile)
