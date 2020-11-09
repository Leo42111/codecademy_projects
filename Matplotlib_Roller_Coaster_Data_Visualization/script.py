import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load rankings data & check dataframe
wood_coasters = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_coasters = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print(wood_coasters.info())
print(steel_coasters.info())
#print(wood_coasters.head())
#print(steel_coasters.head())

# function to plot rankings over time for 1 roller coaster
# parameters: coaster's name, park's name, dataframe
def one_coaster_graph(coaster_name, park_name, df):

  # filter dataframe to obtain rows of target coaster
  target_df = df[(df['Name'] == coaster_name) & (df['Park'].apply(lambda x: park_name in x))]

  # plot target coaster's year of rank vs ranking
  plt.plot(target_df['Year of Rank'], target_df['Rank'])
  plt.gca().invert_yaxis()
  ax = plt.subplot()
  ax.set_yticks(target_df['Rank'].unique())
  ax.set_yticklabels(target_df['Rank'].unique())
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.title('Ranking of ' + coaster_name, fontsize=15)
  plt.show()
  plt.clf()

# function testing
one_coaster_graph('El Toro', 'Six Flags', wood_coasters)

# function to plot rankings over time for 2 roller coasters
# parameters: 1st coaster's name, 1st park's name, 2nd coaster's name, 2nd park's name, dataframe
def two_coasters_graph(name1, park1, name2, park2, df):

  # filter dataframe to obtain rows of target coaster
  coaster1_df = df[(df['Name'] == name1) & (df['Park'].apply(lambda x: park1 in x))]
  coaster2_df = df[(df['Name'] == name2) & (df['Park'].apply(lambda x: park2 in x))]

  # plot target coaster's year of rank vs ranking
  plt.plot(coaster1_df['Year of Rank'], coaster1_df['Rank'], color='red')
  plt.plot(coaster2_df['Year of Rank'], coaster2_df['Rank'], color='blue')
  plt.gca().invert_yaxis()
  ax = plt.subplot()
  y_labels = list(set(coaster1_df['Rank'].unique()) | set(coaster2_df['Rank'].unique()))
  ax.set_yticks(y_labels)
  ax.set_yticklabels(y_labels)
  plt.legend([name1, name2])
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.title('Ranking of ' + name1 + ' vs ' + name2, fontsize=15)
  plt.show()
  plt.clf()

# function testing
two_coasters_graph('El Toro', 'Six Flags', 'Boulder Dash', 'Lake Compounce', wood_coasters)

# function to plot top n rankings over time
# parameters: n, dataframe
def top_n_coasters_graph(n, df):

  # filter dataframe to obtain all coasters on top n rankings
  top_n_coasters_df = df[df['Rank'] <= n]
  unique_coasters = top_n_coasters_df['Name'].unique()

  # plot all coaster rankings in the same plot
  plt.figure(figsize=(12.5, 10))
  for coaster in unique_coasters:
    coaster_df = top_n_coasters_df[top_n_coasters_df['Name'] == coaster]
    plt.plot(coaster_df['Year of Rank'], coaster_df['Rank'])

  # labelling
  plt.gca().invert_yaxis()
  ax = plt.subplot()
  plt.legend(unique_coasters, loc=4)
  y_labels = list(range(1, n + 1))
  ax.set_yticks(y_labels)
  ax.set_yticklabels(y_labels)
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.title('Ranking of Top ' + str(n) + ' Coasters Each Year', fontsize=15)
  plt.show()
  plt.clf()

# function testing
top_n_coasters_graph(5, wood_coasters)

# load roller coaster data & check dataframe
coaster_stats_df = pd.read_csv('roller_coasters.csv')
#print(coaster_stats_df.head())
print(coaster_stats_df.info())

# function to plot histogram of column values
def coaster_info_histogram(df, attr):

  plt.figure(figsize=(10, 8))
  plt.hist(df[attr].dropna())
  plt.xlabel(attr.capitalize())
  plt.ylabel('Count')
  plt.title('Histogram of Roller Coaster ' + attr.capitalize(), fontsize=15)
  plt.show()
  plt.clf()

# function testing
coaster_info_histogram(coaster_stats_df, 'speed')

# function to plot inversions by coaster at a park
def park_coaster_inversions(df, park_name):
  
  # obtain rows of coasters from target park
  park_df = df[df['park'] == park_name]
  park_df = park_df.sort_values('num_inversions', ascending=False)

  # plot bar graph of num of inversions
  plt.bar(range(len(park_df)), park_df['num_inversions'])
  ax = plt.subplot()
  ax.set_xticks(range(len(park_df)))
  ax.set_xticklabels(park_df['name'].values, rotation=45)
  plt.xlabel('Coasters')
  plt.ylabel('Number of Inversions')
  plt.title('Number of Inversions for Coasters in ' + park_name, fontsize=15)
  plt.show()
  plt.clf()

# function testing
park_coaster_inversions(coaster_stats_df, 'Parc Asterix')

# function to plot pie chart of operating status
def operation_pie_chart(df):

  # obtain labels & values(counts of operating/closed definintely coasters)
  filter_df = df['status'].value_counts().filter(items=['status.operating', 'status.closed.definitely'])
  labels = ['Operating', 'Closed Definitely']
  values = filter_df.values

  # pie chart plotting
  plt.pie(values, labels=labels, autopct='%.01f%%')
  plt.axis('equal')
  plt.title('Distribution of Coasters Operating vs closed Definitely', fontsize=15)
  plt.show()
  plt.clf()

# function testing
operation_pie_chart(coaster_stats_df)

# function to create scatter plot of any two numeric columns
def coaster_scatter(df, attr1, attr2):
  plt.scatter(df[attr1], df[attr2], alpha=0.5)
  attr1 = attr1.capitalize()
  attr2 = attr2.capitalize()
  plt.xlabel(attr1)
  plt.ylabel(attr2)
  plt.title('Coaster ' + attr1 + ' vs ' + attr2, fontsize=15)
  plt.show()
  plt.clf()

# function testing
coaster_scatter(coaster_stats_df, 'speed', 'length')

# Which roller coaster seating type is most popular?
def seating_distribution(df):
  # obtain seating type labels & counts
  seating_df = df.dropna()['seating_type'].value_counts()
  seating_type_labels = list(seating_df.index)
  seating_type_count = seating_df.values

  # plot bar graph of seating types
  plt.bar(range(len(seating_type_labels)), seating_type_count)
  ax = plt.subplot()
  ax.set_xticks(range(len(seating_type_labels)))
  ax.set_xticklabels(seating_type_labels, rotation=45)
  plt.xlabel('Seating Type')
  plt.ylabel('Count')
  plt.title('Distribution of Coaster Seating Types', fontsize=15)
  plt.show()
  plt.clf()

seating_distribution(coaster_stats_df)

# Any relations between seating type & height/speed/length?
def seating_relations(df, target_attr):
  df = df.dropna()
  ax = plt.subplot()
  sns.boxplot(data=df, x='seating_type', y=target_attr)
  plt.xticks(rotation=30)
  plt.xlabel('Seating Type')
  plt.ylabel(target_attr)
  plt.title('Coaster Seating Type vs ' + target_attr.capitalize(), fontsize=15)
  plt.show()
  plt.clf()

seating_relations(coaster_stats_df, 'height')
seating_relations(coaster_stats_df, 'speed')
seating_relations(coaster_stats_df, 'length')
