from readCSV import loadCSVFile

X,Y = loadCSVFile()

from sklearn.naive_bayes import MultinomialNB 

model = MultinomialNB()
model.fit(X, Y)
result = model.predict(X)

diferents = result - Y
right = [d for d in diferents if d == 0]
totalRights = len(right)
totaLElements = len(X)
rightRate = 100*totalRights/totaLElements

print(rightRate) 