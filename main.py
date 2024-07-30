# importing the required libraries
import pandas as pd
from sklearn.naive_bayes import GaussianNB, CategoricalNB
from mixed_naive_bayes import MixedNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder,LabelEncoder
from sklearn.metrics import accuracy_score

# training data using CategoricalNB
def cnb_train(X_train, y_train, classier):
    classier.fit(X_train, y_train)


# training data using GaussianNB
def gnb_train(X_train, y_train, classier):
    classier.fit(X_train, y_train)


# training data using MixedNB
def mnb_train(X_train, y_train, classier):
    classier.fit(X_train, y_train)


# predicting data using CategoricalNB
def cnb_pred(X_test, y_test, classier):
    y_pred_cnb = classier.predict(X_test)
    
    print("1. CategoricalNB | accuracy: ", end = " ")
    print(round(accuracy_score(y_test,y_pred_cnb),4))
    print("")

# predicting data using GaussianNB
def gnb_pred(X_test, y_test, classier):
    y_pred_gnb = classier.predict(X_test)
    
    print("2. GaussianNB    | accuracy: ", end = " ")
    print(round(accuracy_score(y_test,y_pred_gnb),4))
    print("")

# predicting data using MixedNB
def mnb_pred(X_test, y_test, classier):
    y_pred_mnb = classier.predict(X_test)
    
    print("3. MixedNB       | accuracy: ", end = " ")
    print(round(accuracy_score(y_test,y_pred_mnb),4))

# predicting with custom data(input)
def pred(classifier):
    y = input()

if __name__ == "__main__":
    print("-" * 40)
    print(" "*15 + "Car adviser")
    print("-"* 40 + "\n")

    cnb = CategoricalNB()
    gnb = GaussianNB()
    mnb = MixedNB(categorical_features=[2, 3])

    # Reading external data
    df = pd.read_csv("car.data")
    X = df[['buying','maint','doors','persons','lug_boot','safety']]
    y = df['class']

    buying = ['vhigh','high','med','low']
    maint = ['vhigh','high','med','low']
    doors = ['2','3','4','5more']
    persons = ['2','4','more']
    lug_boot = ['small','med','big']
    safety = ['low','med','high']

    # Enconding data into integers
    on_enc = OrdinalEncoder(categories=[buying,maint,doors,persons,lug_boot,safety])
    on_enc.fit(X)
    features = on_enc.transform(X)

    lab_enc = LabelEncoder()
    lab_enc.fit(y)
    target = lab_enc.transform(y)

    # Splitting data into train and test
    X_train, X_test, y_train, y_test = train_test_split(features, target)

    # Training the data
    cnb_train(X_train,y_train,cnb)
    gnb_train(X_train,y_train,gnb)
    mnb_train(X_train,y_train,mnb)
    print("_"*40 + "\n")

    
    # Predicting and finding accuracy of classifier
    cnb_pred(X_test,y_test,cnb)
    gnb_pred(X_test,y_test,gnb)
    mnb_pred(X_test,y_test,mnb)
    print("_"*40 + "\n")


    # Training model with entire data
    cnb_train(features, target, cnb)
    gnb_train(features, target, gnb)
    mnb_train(features, target, mnb)
    print("_"*40 + "\n")

    # Predicting input data using CategoricalNB classifier
    data = input("Enter data separated by commas: ").split(",")

    d = {'buying': [data[0]],'maint':[data[1]],'doors': [data[2]],'persons':[data[3]],'lug_boot':[data[4]],'safety':[data[5]]}
    df = pd.DataFrame(data = d)

    X = df[['buying','maint','doors','persons','lug_boot','safety']]

    print("")
    print(X)

    on_enc.fit(X)
    X = on_enc.transform(X)

    y = lab_enc.inverse_transform(cnb.predict(X))[0]
    result = ''

    if (y == 'unacc'):
        result = 'UNACCEPTABLE'
    elif (y == 'acc'):
        result = 'ACCEPTABLE'
    elif (y == 'good'):
        result = 'GOOD'
    elif(y == 'v-good'):
        result = 'VERY GOOD'

    print("\nThe car condition is " + result)