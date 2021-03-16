# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')

# split into subsets with & without heart disease
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# extract cholesterol levels for patients with heart disease & calculate mean cholesterol level
chol_hd = yes_hd.chol
print(np.mean(chol_hd))

# Null hypothesis: People with heart disease have an average cholesterol level equal to 240 mg/dl
# Alternative hypothesis: People with heart disease have an average cholesterol level that is greater than 240 mg/dl

# use one-sample t-test to check if people with heart disease have higher cholesterol levels than average (240 mg/dl)
_, pval = ttest_1samp(chol_hd, 240)

# as the test is two-sided, obtain one-sided test p-value by dividing in half
print(pval/2)
# p-value under 0.05, heart disease patients have an average cholesterol level significantly higher than 240 mg/dl

# extract cholesterol levels for patients without heart disease & calculate mean cholesterol level
chol_no_hd = no_hd.chol
print(np.mean(chol_no_hd))

_, pval = ttest_1samp(chol_no_hd, 240)
print(pval/2)
# p-value over 0.05, non-heart disease patients have an average cholesterol level of 240 mg/dl

# get number of patients in dataset
num_patients = len(heart)
print(num_patients)

# get number of patients with fasting blood sugar >120
num_highfbs_patients = np.sum(heart.fbs == 1)
print(num_highfbs_patients)

# By some estimates, around 8% of the U.S. population had diabetes in 1988 when this data was collected, approximately among the sample size ~24 people have diabetes:
print(num_patients * 0.08)

# Null hypothesis: This sample was drawn from a population where 8% of people have fasting blood sugar > 120 mg/dl
# Alternative hypothesis: This sample was drawn from a population where more than 8% of people have fasting blood sugar > 120 mg/dl

# use binomial test to check if this sample come from a population in which the rate of fbs > 120mg/dl is equal to 8%
pval_3 = binom_test(num_highfbs_patients, num_patients, 0.08, alternative='greater')
print(pval_3)
# p-value under 0.05, null hypothesis rejected, this sample was drawn from a population where more than 8% of people have fbs >120mg/dl