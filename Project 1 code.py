import csv

with open('SampleSuperstore.csv', 'r') as dataset:
    csv_reader = csv.reader(dataset)
    header = next(csv_reader)
    for row in csv_reader:
        # do stuff
        print(row)
        