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
from IncorrectData import IncorrectData
from IdentifyOutliersUsingStats import IdentifyOutliersUsingStats

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
sns.set()
plt.subplots(figsize=(50,60))
sns.set_color_codes("pastel")

#A Seaborn Box Plot

ax = sns.boxplot(x = 'odometer', data =  df, color='b')
ax.set(xlabel ='odometer' , ylabel = 'range')
fig =ax.get_figure()
fig.savefig('SeabornBoxplt.jpg')
#plt.show()


print("min no", df['odometer'].min())
print("min no: index", df['odometer'].idxmin())
print("max no", df['odometer'].max())
print("max no: index",df['odometer'].idxmax())


# Z score from scipy stats

#use z score for all columns in the new data frame 
df_Zscore = df[(np.abs(stats.zscore(df[['odometer']]))<=2).all(axis=1)]


ax = sns.distplot(df['odometer'], color='lime')
ax.set(xlabel ='odometer' , ylabel = 'range')
fig =ax.get_figure()
fig.savefig('normaldistribution.jpg')
plt.show()


#############################################Using Statistical method########################################################

# calling iqr method to calculate inter qauartile to detect outliers in column
#Note: As of now works on structured data
IdentifyOutliersUsingStats.IQR(df)


#################################################### Incorrect Data #############################################################

#####Step 1 - Spell corrrect #######################################

#TODO: pass column in case of structured data, corpus in case of unstructured, semi-structured still need to think
correctsent = IncorrectData.correct_sentence_spelling(df['description'])

