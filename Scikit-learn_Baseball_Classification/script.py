import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

# function to check strike zone of different players
def investigate_strike_zone(player):
  fig, ax = plt.subplots() 

  # clear & relabel data
  player.type = player.type.map({'S':1, 'B':0})
  player = player.dropna(subset=['plate_x', 'plate_z', 'type'])

  # plot scatter graph
  plt.scatter(player.plate_x, player.plate_z, c=player.type, cmap=plt.cm.coolwarm, alpha=0.25)

  # split data into training and validation data
  training_set, validation_set = train_test_split(player, random_state=1)

  # search for best gamma and C for the model
  best_gamma = 0
  best_C = 0
  best_score = 0
  for i in range(1, 21):
    for j in range(1, 21):
      classifier = SVC(kernel = 'rbf', gamma=i, C=j)
      classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])
      score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type'])
      if score > best_score:
        best_gamma = i
        best_C = j
        best_score = score
  print('Best gamma: ' + str(best_gamma))
  print('Best C: ' + str(best_C))
  print('Best score: ' + str(best_score))

  # retrain model with best parameters
  classifier = SVC(kernel = 'rbf', gamma=best_gamma, C=best_C)
  classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

  # plot boundary in scatter plot
  draw_boundary(ax, classifier)
  plt.show()
  plt.clf()

#investigate_strike_zone(aaron_judge)
#investigate_strike_zone(jose_altuve)
investigate_strike_zone(david_ortiz)