# This program read a CSV file and classifies using Multinomial Naive Bayes algorithm 
# and compare the results with a base algorithm.
# Some features are categoric, so we present a technique to treat them

from collections import Counter
import pandas as pd

rateTraining = 0.9
testTraining = 0.1

data = pd.read_csv('categoricData.csv')

Xdummies_df = pd.get_dummies(data[['longBody', 'color', 'poisonous']])

X = Xdummies_df.values
Y = data['isSnake'].values

trainingSize = rateTraining*len(Y)
testSize = testTraining*len(Y)

trainingData = X[:int(trainingSize)]
trainingTarget = Y[:int(trainingSize)]
testData = X[int(-testSize):]
testTarget = Y[int(-testSize):]

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(trainingData, trainingTarget)

results = model.predict(testData)

hits = (results == testTarget)
hitRate = 100.0 * sum(hits)/testSize

print("Our algorithm hit rate: %f" % hitRate)

# Base Algorithm 
hitBase = max(Counter(testTarget).values())
hitBaseRate = 100.0 * hitBase/testSize
print("Base algorithm hit rate: %f" % hitBaseRate)
