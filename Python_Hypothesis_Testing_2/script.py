# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

# check association of thalach (highest heart rate) and diagnosed with heart disease
# plot boxplot
sns.boxplot(x = heart.thalach, y = heart.heart_disease)
plt.show()
plt.clf()

# separate thalach values to with disease & without
thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']

# check mean & median difference
print(np.mean(thalach_no_hd) - np.mean(thalach_hd))
print(np.median(thalach_no_hd) - np.median(thalach_hd))

# Null hypothesis: The average thalach for a person with heart disease is equal to the average thalach for a person without heart disease.
# Alternative hypothesis: The average thalach for a person with heart disease is NOT equal to the average thalach for a person without heart disease.

# use two-sample t-test to check p-value
_, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)
# p-value under 0.05, there is a significant difference in thalach for people with heart disease compared to people without

# check association of cholesterol and diagnosed with heart disease
# plot boxplot
sns.boxplot(x=heart.chol, y=heart.heart_disease)
plt.show()
plt.clf()

# separate cholesterol values to with disease & without
chol_hd = heart.chol[heart.heart_disease == 'presence']
chol_no_hd = heart.chol[heart.heart_disease == 'absence']

# check mean & median difference
print(np.mean(chol_no_hd) - np.mean(chol_hd))
print(np.median(chol_no_hd) - np.median(chol_hd))

# use two-sample t-test to check p-value
_, pval = ttest_ind(chol_hd, chol_no_hd)
print(pval)
# p-value over 0.05, there is no significant difference in cholesterol for people with heart disease compared to people without

# check association of thalach and the type of heart pain
# plot boxplot
sns.boxplot(x=heart.thalach, y=heart.cp)
plt.show()
plt.clf()

# separate thalach values to different heart pain groups
thalach_typical = heart.thalach[heart.cp == 'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

# Null hypothesis: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people all have the same average thalach.
# Alternative hypothesis: People with typical angina, non-anginal pain, atypical angina, and asymptomatic people do not all have the same average thalach.

# use ANOVA to check p-value
_, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print(pval)
# p-value under 0.05, there is at least one pair of chest pain types have significantly different average thalach (max heart rates)

# run Tukey's range test to check which pair(s)
tukey_results = pairwise_tukeyhsd(heart.thalach, heart.cp, 0.05)
print(tukey_results)

# check association of kind of chest pain and whether or not a person have heart disease

# Null hypothesis: There is NOT an association between chest pain type and whether or not someone is diagnosed with heart disease.
# Alternative hypothesis: There is an association between chest pain type and whether or not someone is diagnosed with heart disease.

# create contingency table
Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

# run Chi-Square test
_, pval, _, _ = chi2_contingency(Xtab)
print(pval)
# p-value under 0.05, there is a significant association between these variables