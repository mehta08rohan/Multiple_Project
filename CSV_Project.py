path = "C:\Work\8.Aug2019\Data7602.csv"

file = open(path)

Data =[line.strip().split(',') for line in file]

print(Data[0:2])


import csv


path = "C:\Work\8.Aug2019\Data7602.csv"

file = open(path,newline='')

reader = csv.reader(file)

data=[]

for row in reader:
    an = str(row[0])
    area = str(row[1])
    year = str(row[2])
    ge0_count = str(row[3])
    ec_count = str(row[4])

    data.append([an,area,year,ge0_count,ec_count])

print(data[0:5])



