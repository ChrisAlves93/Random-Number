# import necessary libraries
import numpy as np
import scipy.stats as sc
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# load dataset
fb_df = pd.read_excel("dataset_Facebook2.xlsx")

fb_df.head()

x = fb_df["Lifetime Post reach by people who like your Page"]
y = fb_df["Lifetime People who have liked your Page and engaged with your post"]

plt.scatter(x, y)
plt.xlabel("Lifetime Post reach by people who like your Page")
plt.ylabel("Lifetime People who have liked your Page and engaged with your post")