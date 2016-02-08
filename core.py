import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


"""
Read in train and test as Pandas DataFrames
"""
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

df_train = pd.read_csv(os.path.join(__location__, "train.csv"))
df_test = pd.read_csv(os.path.join(__location__, "test.csv"))

print df_train.head()
