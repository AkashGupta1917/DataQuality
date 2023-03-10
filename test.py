# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:59:53 2023

@author: Divya.Saraswat and Akash Gupta
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("C:/Users/Divya.Saraswat/DataQuality/archive/vehicles.csv",usecols=['region','price','year','manufacturer','model','odometer','condition','description','county','lat'])
print('Total rows',len(data))

df = data[data['odometer'].notna()]
print('After filter nan out', len(df))


#by default set to notebook size
sns.set()
plt.subplots(figsize=(20,30))
sns.set_color_codes("pastel")
#top 10 sentiments
ax = sns.boxplot(x = 'odometer', data =  df.head(20) , color='b')
ax.set(xlabel ='odometer' , ylabel = 'range')
fig =ax.get_figure()
fig.savefig('odometer20.png')
plt.show()