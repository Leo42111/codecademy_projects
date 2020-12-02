from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# get emails for train data and test data
train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset='train', shuffle=True, random_state=108)

test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'], subset='test', shuffle=True, random_state=108)

# transform the data
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)

train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

# create Naive Bayes classifier, train the model & check performance of model with test data
classifier = MultinomialNB()
classifier.fit(train_counts, train_emails.target)

test_score = classifier.score(test_counts, test_emails.target)
print("Test score: " + str(test_score))

