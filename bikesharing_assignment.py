import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loads dataset
data_path = 'Bike-Sharing-Dataset/hour.csv'
rides = pd.read_csv(data_path)

#Shows first rows of the dataset
print(rides.head())


