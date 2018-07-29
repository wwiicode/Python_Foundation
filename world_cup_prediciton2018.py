# Objective definition
# Data collection, Exploratory Data Analysis
# Data visualization, statistic summary, domain knowledge analysis
# Feature Engineering
# Model Building
# Prediction for all possible games with 32 teams
# Tournament simulation for 2018 world cup


import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = (12, 8)


from collection import Counter
import operator
from itertools import combinations, permutations

#machine learning algorithms using sklearn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_sqaured_error, mean_absolute_error
from sklearn.model_selection import train_test_split, GridSearchCV

#https://github.com/neaorin/PredictTheWorldCup/tree/master/input


matches = pd.read_csv("./world_cup/matches.csv")
confederations = pd.read_csv("./world_cup/confederations.csv")

#raw data
matches.head(2)
