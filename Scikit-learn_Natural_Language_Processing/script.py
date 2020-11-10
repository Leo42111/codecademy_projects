from goldman_emma_raw import goldman_docs
from henson_matthew_raw import henson_docs
from wu_tingfang_raw import wu_docs

# Import necessary modules
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Setting up the combined list of friends' writing samples
friends_docs = goldman_docs + henson_docs + wu_docs
# Setting up training labels
friends_labels = [1] * 154 + [2] * 141 + [3] * 166

# Print out a document from each friend
#print(goldman_docs[10])
#print(henson_docs[10])
#print(wu_docs[10])

mystery_postcard = """
Perchance the poor quality of the material whence woman comes is responsible for her inferiority. At any rate, woman has no soul—what is there to know about her? Besides, the less soul a woman has the greater her asset as a wife, the more readily will she absorb herself in her husband. It is this slavish acquiescence to man's superiority that has kept the marriage institution seemingly intact for so long a period. Now that woman is coming into her own, now that she is actually growing aware of herself as a being outside of the master's grace, the sacred institution of marriage is gradually being undermined, and no amount of sentimental lamentation can stay it.
"""

# Create bow_vectorizer
bow_vectorizer = CountVectorizer()
# Define training_vectors
friends_vectors = bow_vectorizer.fit_transform(friends_docs)
# Define test_vector
mystery_vector = bow_vectorizer.transform([mystery_postcard])

# Define classifier
friends_classifier = MultinomialNB()
# Train the classifier
friends_classifier.fit(friends_vectors, friends_labels)
# Make predictions
predictions = friends_classifier.predict(mystery_vector)

# Get the prediction
mystery_friend = predictions[0] if predictions[0] else "someone else"

print("The postcard was from {}!".format(mystery_friend))