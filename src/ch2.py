import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# %%
# Problem 8c

college_data = pd.read_csv('datasets/College.csv')
college_data['Private'] = college_data['Private'].map({'Yes': 1, 'No': 0})

# %%

# iv: Create new qualitative variable, called Elite, by binning Top10perc by > 50%
college_data['Elite'] = np.where(college_data['Top10perc'] > 50, 1, 0)

fig, ax = plt.subplots(1, 1)
sns.boxplot(data=college_data, x="Elite", y="Outstate", ax=ax)

# %%

sns.distplot(college_data['Elite'], kde=False)

# %%

auto_data = pd.read_csv("datasets/Auto.csv")
quan_auto_data = auto_data.select_dtypes(include=np.number)

# %%
# Problem 9c

for (name, data) in quan_auto_data.iteritems():
    print(name)
    print("RANGE: (" + str(data.min()) + ", " + str(data.max()) + ")")
    print("STD: " + str(data.std()))
    print("MEAN: " + str(data.mean()))

# %%
# Problem 9d

for (name, data) in quan_auto_data.drop(quan_auto_data.index[[10, 85]]).iteritems():
    name)
    print("RANGE: (" + str(data.min()) + ", " + str(data.max()) + ")")
    print("STD: " + str(data.std()))
    print("MEAN: " + str(data.mean()))

# %%
# Problem 9e

fig, ax = plt.subplots(2, 2)

sns.scatterplot(x=quan_auto_data['cylinders'], y=quan_auto_data['mpg'],  ax=ax[0, 0])
sns.scatterplot(x=quan_auto_data['displacement'], y=quan_auto_data['mpg'], ax=ax[0, 1])
sns.scatterplot(x=quan_auto_data['weight'], y=quan_auto_data['mpg'], ax=ax[1, 0])
sns.scatterplot(x=quan_auto_data['year'], y=quan_auto_data['mpg'], ax=ax[1, 1])

plt.show()

# %%
