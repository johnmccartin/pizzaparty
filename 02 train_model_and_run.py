# Load libraries (these were taken from tutorials and might not all be necessary)
import sys
import scipy
import numpy
import pandas
import sklearn

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
classifier = LinearSVC(verbose=0)


#load the yelp data prepared on the node side
yelp_dataset = pandas.read_json('./data/yelp/yelp_restaurants_is_italian_pizza.json')

#create a training classifier on yelp data
data_train, data_test, y_train, y_true = model_selection.train_test_split(yelp_dataset['name'], yelp_dataset['italo_status'], test_size=0.4)

# compute n-grams of size 1 through 4
ngram_counter = CountVectorizer(ngram_range=(1, 4), analyzer='char')



#run n-grams on training data

X_train = ngram_counter.fit_transform(data_train)
X_test  = ngram_counter.transform(data_test)

#create a model for classifying yelp data based on business names
model = classifier.fit(X_train, y_train)


def show_most_informative_features(vectorizer, clf, n=20):
    feature_names = vectorizer.get_feature_names()
    coefs_with_fns = sorted(zip(clf.coef_[0], feature_names))
    top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
    for (coef_1, fn_1), (coef_2, fn_2) in top:
        print("\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))


show_most_informative_features(ngram_counter, classifier, n=20)

#print(model)

y_test = model.predict(X_test)
#print("Model Accuracy: " + str(sklearn.metrics.accuracy_score(y_true, y_test) ) )
#print(str(sklearn.metrics.classification_report(y_true, y_test)))


#load the esri data (this 2013 data of businesses in 44: retail (just food etc) or 72: accomodation and food service)
esri_dataset = pandas.read_csv('./data/esri/esri_ba13_naics44_72.csv')

#create an array of business names
esri_names = esri_dataset['CONAME']

#create the ngrams
esri_ngram = ngram_counter.transform(esri_names.values.astype('U'))

#predict whether it's italian based on the yelp classifier (this returns an array in the order of your names)
esri_prediction = model.predict(esri_ngram)

#join the prediction array to your esri data frame
esri_dataset['italo_prediction'] = esri_prediction

#select only businesses classified as italian
italian_places = esri_dataset.loc[ esri_dataset['italo_prediction'] == 'Italian' ]

#print summary statistics (to be compared to statistics for the real italy)
print( 'Shape: ' + str( italian_places.shape ) )
print( 'Total Sales Vol: ' + str( italian_places['SALES_VOL'].sum() ) )
print( 'Total Employees: ' + str( italian_places['NUMBER_EMP'].sum() ) )
print( 'Total Square Feet: ' + str( italian_places['SQFT'].sum() ) )

#output to csv for later analysis if needed
italian_places.to_csv('./results/italian_pizza_places.csv')








