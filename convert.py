import csv
import json

# open a file for reading
csvfile = open('OrderNo.csv', 'r')

# create the csv reader object
reader = csv.reader(csvfile)

# skip the first line (header)
next(reader)

# empty list
dataorder = []

# extract each data row one by one
for row in reader:
    dataorder.append(row)

# close the csv file
csvfile.close()

# now we will open a file for writing
jsonfile = open('dataorder.json', 'w')

# write data into it
jsonfile.write(json.dumps(dataorder))

# close the file
jsonfile.close()


