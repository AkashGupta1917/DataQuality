# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 19:13:49 2023

@author: Divya.Saraswat and Akash Gupta
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

class IdentifyOutliersUsingStats():
    
    def IQR(df):
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

        # ax = sns.boxplot(x = 'odometer', data =  data, color='b')
        # ax.set(xlabel ='odometer' , ylabel = 'range')
        # fig =ax.get_figure()
        # fig.savefig('iqr.jpg')
        # plt.show()

        fig = plt.figure(figsize=(10,8))
        bp = plt.boxplot(data)
        plt.show()