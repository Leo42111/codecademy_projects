import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv("tennis_stats.csv")
'''
print(df.head())
print(df.info())
print(df.describe())
'''


## exploratory analysis
# this function plots scatter plots to check if there are any relationship between x and y
def exploratory_analysis(x_attr, y_attr):
  for y in y_attr:
    for x in x_attr:
      plt.close()
      plt.scatter(df[x], df[y], alpha=0.4)
      plt.xlabel(x)
      plt.ylabel(y)
      plt.show()

# lists of attributes
offensive_attributes = ["Aces", "DoubleFaults", "FirstServe", "FirstServePointsWon", "SecondServePointsWon", "BreakPointsFaced", "BreakPointsSaved", "ServiceGamesPlayed", "ServiceGamesWon", "TotalServicePointsWon"]
defensive_attributes = ["FirstServeReturnPointsWon", "SecondServeReturnPointsWon", "BreakPointsOpportunities", "BreakPointsConverted", "ReturnGamesPlayed", "ReturnGamesWon", "ReturnPointsWon", "TotalPointsWon"]
y_attributes = ["Wins", "Losses", "Winnings", "Ranking"]
# perform exploratory analysis
'''
exploratory_analysis(offensive_attributes, y_attributes)
exploratory_analysis(defensive_attributes, y_attributes)
'''

## single feature linear regressions
# this function builds linear regression models for one single x feature
def single_linear_regression(x_attr, y_attr):
  # obtain x values and y values
  x = df[x_attr].values.reshape(-1, 1)
  y = df[y_attr]

  # split data into training set and validation set
  x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=10)

  # building model
  slr = LinearRegression()
  slr.fit(x_train, y_train)

  # get y predictions using the model and plot scatter graph to observe the results
  y_prediction = slr.predict(x_test)
  plt.close()
  plt.scatter(y_test, y_prediction, alpha=0.4)
  plt.xlabel("Actual Values")
  plt.ylabel("Predictions")
  plt.title(x_attr + " vs " + y_attr)
  plt.show()

selected_x_attr = ["Aces", "DoubleFaults", "BreakPointsFaced", "ServiceGamesPlayed", "BreakPointsOpportunities", "ReturnGamesPlayed"]

# perform single feature linear regressions
'''
for x_attr in selected_x_attr:
  single_linear_regression(x_attr, "Wins")
'''

## two feature linear regressions
# this function builds linear regression models for two x feature
def multiple_linear_regression(x_attr_list, y_attr):
  # obtain x values and y values
  x = df[x_attr_list]
  y = df[y_attr]

  # split data into training set and validation set
  x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=10)

  # building model
  dlr = LinearRegression()
  dlr.fit(x_train, y_train)

  # get y predictions using the model and plot scatter graph to observe the results
  y_prediction = dlr.predict(x_test)
  plt.close()
  plt.scatter(y_test, y_prediction, alpha=0.4)
  plt.xlabel("Actual Values")
  plt.ylabel("Predictions")
  title = ""
  if len(x_attr_list) == 2:
    title = x_attr_list[0] + " & " + x_attr_list[1]
  elif len(x_attr_list) == 18:
    title = "All Attributes"
  plt.title(title + " vs " + y_attr)
  plt.show()

# creating x attribute pairs
selected_x_attr_pair = []
for i in range(len(selected_x_attr)):
  for j in range(i+1, len(selected_x_attr)):
    selected_x_attr_pair.append([selected_x_attr[i], selected_x_attr[j]])
#print(selected_x_attr_pair)

# perform two feature linear regressions
'''
for x_attr_pair in selected_x_attr_pair:
  multiple_linear_regression(x_attr_pair, "Wins")
'''


## multiple feature linear regressions
all_attributes = offensive_attributes + defensive_attributes
'''
multiple_linear_regression(all_attributes, "Wins")
'''
