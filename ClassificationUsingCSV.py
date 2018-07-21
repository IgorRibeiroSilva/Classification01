# This program read data from the CSV file and uses a Naive Bayes Multinomial model to 
# fit to the data and predic the results. Then tries to predict the results for the same 
# samples used for training and calculate the hit rate
from readCSV import loadCSVFile

X,Y = loadCSVFile()

from sklearn.naive_bayes import MultinomialNB 

model = MultinomialNB()
model.fit(X, Y)
result = model.predict(X)
diferents = result - Y
right = [d for d in diferents if d == 0]

rightRate = 100*len(right)/len(X)

print(rightRate) 