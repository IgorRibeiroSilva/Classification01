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

def loadCSVCategoric():
    data = []
    target = []

    filesss = open('categoricos.csv', 'r')
    reader = csv.reader(filesss)
    next(reader)
    
    for home, busca, logado, comprou in reader:
        line = [int(home), busca, int(logado)]
        data.append(line)
        target.append(int(comprou))
    
    return data, target