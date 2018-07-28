import csv

def loadCSVFile(fileName):
    data = []
    target = []
    listColumn = []
    
    filesss = open(fileName, 'r')
    reader = csv.reader(filesss)
    for line0 in reader:
        listColumn = line0
        break

    numberColumns = len(listColumn) - 1

    for listFeatures in reader:
        line = []
        for i in range(0, numberColumns):
            line.append(returnData(listFeatures[i]))
        
        data.append(line)
        target.append(returnData(listFeatures[numberColumns]))

    return data, target

def returnData(data):
    try: 
        int(data)
        return int(data)
    except ValueError:
        return data