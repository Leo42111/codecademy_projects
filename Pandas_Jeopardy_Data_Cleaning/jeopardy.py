import pandas as pd
pd.set_option('display.max_colwidth', None)

# load csv into dataframe and clean column names
df = pd.read_csv('jeopardy.csv')
df.columns = ['Show Number', 'Air Date', 'Round', 'Category', 'Value', 'Question', 'Answer']

# display dataframe info and print first few values for each column
'''
print(df.info())
print(df['Show Number'].head())
print(df['Air Date'].head())
print(df['Round'].head())
print(df['Category'].head())
print(df['Value'].head())
print(df['Question'].head())
print(df['Answer'].head())
'''

# function to filter dataframe if all words in keyword_list is in the question
def filter_questions(df, keyword_list):
  new_df = df[df['Question'].apply(lambda x: all(word.lower() in x.lower() for word in keyword_list))]
  return new_df

# function testing
keyword_1 = ["King", "England"]
filtered_df = filter_questions(df, keyword_1)
print(filtered_df["Question"])

# clean 'Value' column, remove 'None' values and convert values to float
df = df[df['Value'] != 'None']
df['Value'] = df['Value'].replace('[\$,]', '', regex=True)
df['Value'] = df['Value'].astype(float)
print(df['Value'])

# function to return count of unique answers to all the questions in dataset
def count_unique_ans(df):
    return df['Answer'].value_counts()
    
# function testing
print(count_unique_ans(filtered_df))