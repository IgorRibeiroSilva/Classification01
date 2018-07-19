snake1 = [1, 1, 1]
snake2 = [1, 0, 1]
snake3 = [1, 1, 0]
bird1 = [1, 0, 0]
bird2 = [1, 0, 0]
bird3 = [1, 0, 1]

data =  [snake1, snake2, snake3, bird1, bird2, bird3]

target = [1, 1, 1, 0, 0, 0]

otherAnimal = [1, 1, 0]
oneMoreAnimal = [1, 0, 0]

testArray = [otherAnimal, oneMoreAnimal]

from sklearn.naive_bayes import MultinomialNB

multiNomialModel = MultinomialNB()
multiNomialModel.fit(data, target)

print(multiNomialModel.predict(testArray))