#import the libraries

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
import seaborn as sns
%matplotlib inline

#read the data into dataframe

df = []
df = pd.read_csv('IT_motives_2013.csv')
df.head()

#remove unnecessary characters from the column headers

df.columns = df.columns.str.replace('\/','') 
df.head()

#drop the unnecessary rows 

df = df.drop(df[df.StateUTs == 'Total (UTs)'].index)
df = df.drop(df[df.StateUTs == 'Total (States)'].index)
df = df.drop(df[df.StateUTs == 'Total (All India)'].index)

#highest cyber crime rate report of states 

plt.figure(figsize=(70,30))
sns.set(font_scale=6)
sns.barplot(x='StateUTs', y='Total', data = df)
plt.title('Cyber Crimes - Total')
plt.ylabel('Total')
plt.xticks(rotation=90)

#states in which cyber crimes are related to 'Revenge Settling Scores'
plt.figure(figsize=(70,30))
sns.set(font_scale=6)
yCol = 'Revenge Settling scores'
sns.barplot(x='StateUTs', y = yCol, data = df)
plt.title('Cyber Crimes - ' + yCol)
plt.ylabel('Total')
plt.xticks(rotation=90)


#states in which cyber crimes are related to 'Greed of Money'
plt.figure(figsize=(70,30))
sns.set(font_scale=6)
yCol = 'Greed Money'
sns.barplot(x='StateUTs', y = yCol, data = df)
plt.title('Cyber Crimes - ' + yCol)
plt.ylabel('Total')
plt.xticks(rotation=90)

#states in which cyber crimes are related to 'Extortion'
plt.figure(figsize=(70,30))
sns.set(font_scale=6)
yCol = 'Extortion'
sns.barplot(x='StateUTs', y = yCol, data = df)
plt.title('Cyber Crimes - ' + yCol)
plt.ylabel('Total')
plt.xticks(rotation=90)

#states in which cyber crimes are related to 'Cause Disrepute'
plt.figure(figsize=(70,30))
sns.set(font_scale=6)
yCol = 'Cause Disrepute'
sns.barplot(x='StateUTs', y = yCol, data = df)
plt.title('Cyber Crimes - ' + yCol)
plt.ylabel('Total')
plt.xticks(rotation=90)

#states in which cyber crimes are related to 'Prank or Satisfaction of gaining control'
plt.figure(figsize=(70,30))
sns.set(font_scale=6)
yCol = 'Prank Satisfaction of Gaining Control '
sns.barplot(x='StateUTs', y = yCol, data = df)
plt.title('Cyber Crimes - ' + yCol)
plt.ylabel('Total')
plt.xticks(rotation=90)

#states in which cyber crimes are related to 'Fraud or Illegal Gain'
plt.figure(figsize=(70,30))
sns.set(font_scale=6)
yCol = 'Fraud Illegal Gain'
sns.barplot(x='StateUTs', y = yCol, data = df)
plt.title('Cyber Crimes - ' + yCol)
plt.ylabel('Total')
plt.xticks(rotation=90)

#states in which cyber crimes are related to 'Eve Teasing and Harassment'
plt.figure(figsize=(70,30))
sns.set(font_scale=6)
yCol = 'Eve teasing Harassment'
sns.barplot(x='StateUTs', y = yCol, data = df)
plt.title('Cyber Crimes - ' + yCol)
plt.ylabel('Total')
plt.xticks(rotation=90)

#using melt() function of pandas library to create a new dataframe
df_new = df
df_new = df_new.drop(['Crime Head','Total'], axis = 1)
df_new = pd.melt(df_new, id_vars=['StateUTs','Year'], var_name = 'CrimeType')
df_new.head()

#Create a new dataframe which holds the total count of each cyber crime types. 
#This would make our life easy to plot based on the total occurance of each cyber crime type.
df_totalCrimeType = pd.DataFrame({'TotalCrimes' : df_new.groupby(['CrimeType']).value.sum()}).reset_index()
df_totalCrimeType

#to see which type of cyber crimes are occuring more...
plt.figure(figsize=(70,30))
sns.set(font_scale=6)
sns.barplot(x='CrimeType', y='TotalCrimes', data=df_totalCrimeType)
plt.title('Cyber Crimes - Overall')
plt.xlabel('Type of Crime')
plt.ylabel('Total Crimes')
plt.xticks(rotation=90)



