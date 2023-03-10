# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:53:58 2023

@author: Divya.Saraswat and Akash Gupta
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("C:/Users/Divya.Saraswat/DataQuality/archive/vehicles.csv",usecols=['region','price','year','manufacturer','model','odometer','condition','description','county','lat'])
print('Total rows',len(data))

# working with not null values in odometer column

# filter
df = data[data['odometer'].notna()]
print('After filter nan out', len(df))
#print(df.head())


# Using pandas describe() to figure out few stats for odometer column
print(df.describe()[['odometer']])

# Visualize outliers

#A Seaborn Box Plot
sns.boxplot(x = df['odometer'], color='lime')
plt.xlabel('Odometer range', fontsize=20)
plt.savefig('SeabornBoxplt.jpg')



print("min no", df['odometer'].min())
print("min no: index", df['odometer'].idxmin())
print("max no", df['odometer'].max())
print("max no: index",df['odometer'].idxmax())


# Z score from scipy stats

#use z score for all columns in the new data frame 
df_Zscore = df[(np.abs(stats.zscore(df[['odometer']]))<=2).all(axis=1)]

fig = plt.figure(figsize=(12,8))
plt.subplot(1,2,1)
sns.boxplot(x=df['odometer'], color='lime')
plt.xlabel('(After Using Z Score)', fontsize=14)
plt.subplot(1,2,2)
sns.distplot(df['odometer'], color='lime')
plt.tight_layout()
plt.savefig('normaldistribution.jpg')


# fig = plt.figure(figsize=(12,8))
# plt.subplot(1,2,1)
# sns.boxplot(x=df_Zscore['odometer'], color='lime')
# plt.xlabel('(After Using Z Score)', fontsize=14)
# plt.subplot(1,2,2)
# sns.distplot(df_Zscore['odometer'], color='lime')
# plt.tight_layout()
# plt.savefig('normaldistribution.jpg')


# Finding outliers using statistical methods - iqr, hampel

# iqr - Inter Quartile Range

medianQ2 = df['odometer'].median()
q2 = np.percentile(df['odometer'],50)
q1 , q3 = np.percentile(df['odometer'],[25,75])

print(q1,q2,q3)

iqr = q3 - q1
lower_range = q1 - (1.5*iqr)
upper_range = q3 + (1.5*iqr)

print(lower_range,",",upper_range)

upper_outliers = df['odometer'][df['odometer']>upper_range]
print(upper_outliers.count())

d1 = []
d2 = []
d3 = []

# binning 
for i in df['odometer']:
    if(i<q2):
        d1.append(i)
    elif(i<q3):
        d2.append(i)
    else:
        d3.append(i)
        
data = [d1,d2,d3]

fig = plt.figure(figsize=(10,8))
bp = plt.boxplot(data)
plt.savefig('iqr.jpg')


