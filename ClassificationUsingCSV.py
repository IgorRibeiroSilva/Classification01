import csv

def loadCSVFile():
    data = []
    target = []

    filesss = open('dataSnake.csv', 'rb')
    reader = csv.reader(filesss)

    for longBody,creeps,poisonous,isSnake in reader:

        data.append([longBody, creeps, poisonous])
        target.append([isSnake])

    return data, target

print(loadCSVFile())