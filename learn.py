from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

import numpy as np
import pandas as pd
 
data = pd.read_csv('trial.csv')

#print data

train = np.array(data)
test = np.array(data)

#print train

train = train[range(1,300),:]
test = test[range(300,375),:]

print train

trainFeatures = train[:,range(0,5)]
trainResult = train[:,5]

testFeatures = test[:,range(0,5)]
testnResult = test[:,5]

print trainFeatures
print trainResult

adb = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=1500,
    learning_rate=1, random_state=25)
 
adb = adb.fit(trainFeatures, trainResult)

import sklearn.metrics as skm
 
training_pred = adb.predict(trainFeatures)
print skm.confusion_matrix(list(training_pred), list(trainResult))

test_pred = adb.predict(testFeatures)
print skm.confusion_matrix(list(test_pred), list(testnResult))



#adb = AdaBoostClassifier( DecisionTreeClassifier(max_depth=3), n_estimators=1000, learning_rate=0.4, random_state=42)
 

 
#Arrays where the match results are stored in
#results_train = np.array(dta.FTR[train_idx])
#results_test = np.array(dta.FTR[test_idx])
 
#adb = AdaBoostClassifier(
#   DecisionTreeClassifier(max_depth=3),
#    n_estimators=1000,
#    learning_rate=0.4, random_state=42)
 
#adb = adb.fit(feature_train, results_train)