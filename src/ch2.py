import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
# Problem 8c

college_data = pd.read_csv('datasets/College.csv')

college_data[['Outstate', 'Private']]

fig1, ax1 = plt.subplots()
ax1.set_title('Outstate and Private')
ax1.boxplot(college_data['Outstate'])

fixed_college_data = college_data['Private'].map({'Yes': 1, 'No': 0})

ax1.boxplot(fixed_college_data)

# %%
