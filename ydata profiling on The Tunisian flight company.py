# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:33:13 2023

@author: busola
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("Tunisair_flights_dataset.csv")

data.info()
data.describe(include = 'all')
missing = data.isnull().sum()
data.head()
data.tail()
coree = data.corr()
from ydata_profiling import ProfileReport

profiledata = ProfileReport(data,title = 'tunisian flight data')
profiledata.to_widgets
profiledata.to_file("tunisian flight data.html")


# OBSERVATIONS
# Number of variables are 9
# Number of observations are 107833
# Missing cells	are 0
# Missing cells (%)	are 0.0% of the given data
# Duplicate rows are 0
# Duplicate rows (%) are 0.0% of the data set
# Total size in memory is 7.4 MiB
# Average record size in memory is 72.0 B
# DateTime columns are 2
# Text columns are 5
# Categorical columns are 1
# Numeric column is 1
# STATUS column is highly imbalanced with ATA having 73.4% of the data	and the distribution in the following:
# ATA	93679 
# SCH	13242 
# DEP	 467
# RTR	 294
# DEL	 151
# Arrival delay has 38168 zeros which is 35.4% of the data set
# There were no missing values 
