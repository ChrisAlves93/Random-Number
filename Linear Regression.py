#The project encompasses data preprocessing, exploratory data analysis, model building, evaluation, and interpretation. The primary objective is to establish a robust and interpretable model that can predict a target variable based on various input features.
#Technologies Used
#Python: The primary programming language used for data analysis and modeling.
#Pandas & NumPy: For data manipulation and numerical computations.
#Matplotlib & Seaborn: For data visualization.



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
