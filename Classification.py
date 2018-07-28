#Let's declare some snakes, frogs and its features. For example 'Have a long body', 'crawl' and 'is poisonous' 
snake1 = [1, 1, 1]
snake2 = [1, 0, 1]
snake3 = [1, 1, 0]
frog1 = [0, 0, 0]
frog2 = [0, 1, 0]
frog3 = [1, 0, 1]

#This will be our data array
data =  [snake1, snake2, frog3, frog1, frog2, frog3]

#And here we have our target array. Value '1' indicates that is a snake, '0' indicates a frog
target = [1, 1, 1, 0, 0, 0]

#Now let's declare two animals that can be snakes or frogs. Let's use them to test our program
otherAnimal = [1, 1, 0]
oneMoreAnimal = [1, 0, 0]
testArray = [otherAnimal, oneMoreAnimal]

#Importing Naive Bayes module from sklearn
from sklearn.naive_bayes import MultinomialNB

#Declaring a Multinomial Naive Bayes object
multiNomialModel = MultinomialNB()

#Here we train our object to fit to our data and target
multiNomialModel.fit(data, target)

#Finally, we can predict which animals are our animals in testArray
print(multiNomialModel.predict(testArray))