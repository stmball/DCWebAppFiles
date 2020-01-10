import json

with open('cts_data_6.csv') as file:
    data = file.read()
    data = data.split('\n')[:100000]
    output = []
    for row in data[:-1]:
        row = row.split(',')
        output.append({'time': float(row[3]), 'actual': float(row[4]), 'predicted': float(row[2])})

with open('output4.json', 'w') as outfile:
    json.dump(output, outfile)
