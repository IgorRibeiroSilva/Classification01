import csv
def loadCSVCategoric():
    data = []
    target = []

    filesss = open('dataSnake.csv', 'r')
    reader = csv.reader(filesss)
    next(reader)
    
    for home, busca, logado, comprou in reader:
        line = [int(home), busca, int(logado)]
        data.append(line)
        target.append(int(comprou))
    print(data, target)
    return data, target