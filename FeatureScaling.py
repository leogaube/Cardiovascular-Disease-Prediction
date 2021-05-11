import pandas as pd
from sklearn import preprocessing, linear_model
import numpy as np
import statistics
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

### LOAD DATA ###
print('-'*30); print("IMPORTING DATA");print('-'*30)
df = pd.read_csv('cardio_train.csv', sep=';', index_col='id')

### Feature Scaling ###

# Min/Max Scaling on I=[0,1]: x_scaled = (x - min(x)) / (max(x) - min(x))
df['age_scaled'] = ((df['age'])-min(df['age']))/(max(df['age'])-min(df['age']))
df['height_scaled'] = ((df['height'])-min(df['height']))/(max(df['height'])-min(df['height']))
df['weight_scaled'] = ((df['weight'])-min(df['weight']))/(max(df['weight'])-min(df['weight']))
# Standardization: x_standardized = (x - µ) / sigma
df['age_standardized'] = (df['age']-statistics.mean(df['age'])) / statistics.stdev(df['age'])
df['height_standardized'] = (df['height']-statistics.mean(df['height'])) / statistics.stdev(df['height'])
df['weight_standardized'] = (df['weight']-statistics.mean(df['weight'])) / statistics.stdev(df['weight'])

df['bmi'] = (df['weight'] / ((df['height'] / 100) ** 2)).round(decimals=2)
df['bmi_high'] = (df['bmi'] >= 30).astype(int)

# eliminate corrupted Data
df['ap_lo_fixed'] = [df['ap_lo'] if 50 < x < 150 else -1 for x in df['ap_lo']]
df['ap_hi_fixed'] = [df['ap_hi'] if 100 < x < 190 else -1 for x in df['ap_hi']]

#profile = ProfileReport(df, title="Pandas Profiling Report after Feature Scaling", explorative=True)
#profile.to_file("CardioVascular-Disease-Prediction with Feature Scaling.html")

plt.figure(figsize=(18, 8))
sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True, cmap='vlag') # cmap='BrBG'
plt.title('Correlation Map', fontdict={'fontsize':12}, pad=12)
plt.show()

#sns.lmplot(x='age_standardized', y='bmi', hue='cardio', data=df, fit_reg=False)
#plt.show()
#print(df['height_scaled'])

