import csv

def loadCSVFile():
    data = []
    target = []

    filesss = open('dataSnake.csv', 'r')
    reader = csv.reader(filesss)
    next(reader)
    
    for longBody,creeps,poisonous,isSnake in reader:
        line = [int(longBody), int(creeps), int(poisonous)]
        data.append(line)
        target.append(int(isSnake))

    return data, target