import pandas as pd
import numpy as np

"""LOAD THE DATASET"""
try:
    df=pd.read_csv("titanic_dataset.csv")
except FileNotFoundError:
    print("Dataset not found.Download it from kaggle and place it in the same directory as the script.")

# This returns a list of columns and the count of missing values in each
print(df.isnull().sum())

#Initial Data Preview
print(df[['Name',  'Age', 'Cabin', 'Embarked', 'Fare']].head())
print(df.info())
#CLEANING THE DATA

"""AGE: Fill the missing values with the median age
Using the median age instead of the mean ensures that the distribution of ages is preserved, avoiding skewness."""
df['Age']=df['Age'].fillna(df['Age'].median())

"""CABIN: Create a new category "Unknown" for missing values"""
df['Cabin']=df['Cabin'].fillna('Unknown')

"""EMBARKED: Fill the missing values with the most frequent value
The most frequent value is the mode of the column."""
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])

"""Cleaning currency/special characters from the Fare column"""
df['Fare']=df['Fare'].astype(str).str.replace('[$,₹]','').astype(float)

"""Extract Titles into a NEW column
This pattern finds the word followed by a period (e.g., "Mr.")"""
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)

"""REMOVE Titles from the Name column
use regex to find the title + period and replace it with an empty string
The pattern covers almost all Titanic titles: Mr, Mrs, Miss, Master, Dr,
 Rev, Col, Major, Mlle, Mme, Ms, Capt, Sir, Don, Jonkheer, Countess, Lady."""
title_pattern = r' (Mr|Mrs|Miss|Master|Dr|Rev|Col|Major|Mlle|Mme|Ms|Capt|Sir|Don|Jonkheer|Countess|Lady)\.'
df['Name'] = df['Name'].str.replace(title_pattern, '', regex=True)

r"""Clean up trailing spaces and commas
After removing the title, names might look like 'Braund,  Owen
'\s+' means 'one or more whitespace characters(including hidden ones)'
The 'r' tells Python the \s is for Regex, not a string escape."""
df['Name']=df['Name'].str.replace(r'\s+', ' ', regex=True).str.strip()

#FINAL CHECK AND EXPORT THE DATA

print("\n--Missing values check after cleaning--")
print(df.isnull().sum())
print("\n--- Final Cleaned Data Preview ---")
print(df[['Name', 'Title', 'Age', 'Cabin', 'Embarked', 'Fare']].head())
print(df.info())
# Save the cleaned data for your portfolio
df.to_csv('Titanic_Cleaned_Project.csv', index=False)
print("\n Cleaned dataset saved as 'Titanic_Cleaned_Project.csv'")