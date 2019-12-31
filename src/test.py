import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
income1_data = pd.read_csv("datasets/Income1.csv", index_col=0)
income1_data.plot(kind='scatter', x='Education', y='Income', color='blue')

#%%

income2_data = pd.read_csv("datasets/Income2.csv")
income2_data.plot(kind='scatter', x='Seniority', y='Income', color='blue')

# %%

s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

# %%

college_data = pd.read_csv("datasets/College.csv")

# %%

college_data.plot(kind='scatter', x='Outstate', y='Top10perc')

# %%
