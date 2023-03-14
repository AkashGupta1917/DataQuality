import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import OLSInfluence
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = pd.read_csv("vehicles.csv", usecols=['region','price','year','manufacturer','model','odometer','condition','description','county','lat'])

data = data.sample(n=1000)

# fit the regression model using statsmodels library 
f = 'price ~ manufacturer'
model = ols(formula=f, data=data).fit()

# calculate the cooks_distance - the OLSInfluence object contains multiple influence measurements
cook_distance = OLSInfluence(model).cooks_distance
(distance, p_value) = cook_distance

# scatter plot - x axis (independent variable price), y-axis (dependent variable odometer), size and color of the marks according to its cook's distance
sns.scatterplot(x= data.manufacturer, y= data.price, hue=distance, size=distance, sizes=(50, 200), edgecolor='black', linewidth=1)

# ticks
plt.xticks(fontsize=14,rotation=90)
plt.yticks(fontsize=14)

# labels and title
plt.xlabel('manufacturer', fontsize=14)
plt.ylabel('price', fontsize=14)
plt.title('Cook\'s distance', fontsize=20);

# plt.show()
plt.savefig('cooks.jpg')
