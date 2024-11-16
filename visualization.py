import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt

# Merging WHO and Word Bank datasets
who_data = pd.read_csv('path.csv')
worldbank_data = pd.read_csv('path.csv')

merged_data = pd.merge(who_data, worldbank_data, on=['Year'])

# Scatter plot of Prevalence of underweight among adults vs. Agriculture, forestry, and fishing, value added
sns.scatterplot(data=merged_data, x='Underweight_adults', y='Annual_growth')
plt.title('Prevalence of underweight among adults vs. Agriculture, forestry, and fishing, value added')
plt.show()
