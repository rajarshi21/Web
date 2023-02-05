# What is Pandas?
# Pandas is a Python library used for working with data sets.
#
# It has functions for analyzing, cleaning, exploring, and manipulating data.
#
# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created
# by Wes McKinney in 2008.
#
# Why Use Pandas?
# Pandas allows us to analyze big data and make conclusions based on statistical theories.
#
# Pandas can clean messy data sets, and make them readable and relevant.
#
# Relevant data is very important in data science.
#
# :}
# Data Science: is a branch of computer science where we study how to store, use and analyze data for
# deriving information from it.
#
# What Can Pandas Do?
# Pandas gives you answers about the data. Like:
#
# Is there a correlation between two or more columns?
# What is average value?
# Max value?
# Min value?
# Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values.
# This is called cleaning the data.

import pandas as pd

df = pd.read_csv('Tests/data.csv')
print(df)
print(df.to_string())

# Interpreting a dataset
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

# Pandas Series
# A Pandas Series is like a column in a table.#
# It is a one-dimensional array holding data of any type.
a = [1, 7, 2]
myvar = pd.Series(a)
# Printing a series
print('Printing series')
print(myvar)
# Labels: If nothing else is specified, then values are labelled with their index number
print(myvar[0])
# Create labels
print('Creating labels')
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])
# Key/Value objects as series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
# Create a Series using only data from "day1" and "day2"
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
# Create a dataframe from 2 series
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

# Pandas dataframe
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
# Locate a row
# Use the row index
print(df.loc[0])
# Get more than one row
print(df.loc[[0, 1]])

# Named indices
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df.to_string())
# refer to the named index
print(df.loc["day2"])
# Load files into a dataframe
# df = pd.read_csv('data.csv')
# print(df)

# Pandas read CSV
# Can get the max rows defined in pandas options
print(pd.options.display.max_rows)
# Can also set the pandas max rows (ie we can override this as well)
pd.options.display.max_rows = 9999
print(pd.options.display.max_rows)

# Read json
# df = pd.read_json('data.json')
# print(df.to_string())

# Load a python dictionary to a dataframe
data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}
df = pd.DataFrame(data)
print(df)

# Pandas analyzing dataframes
print(df.tail())   # Gives the last 5 rows of the dataframe
print(df.info())  # Gives info about the data

# Result Explained
# The result tells us there are 169 rows and 4 columns:
#
#
#   RangeIndex: 169 entries, 0 to 168
#   Data columns (total 4 columns):
#
# And the name of each column, with the data type:
#
#
#    #   Column    Non-Null Count  Dtype
#   ---  ------    --------------  -----
#    0   Duration  169 non-null    int64
#    1   Pulse     169 non-null    int64
#    2   Maxpulse  169 non-null    int64
#    3   Calories  164 non-null    float64
#
# Null Values
# The info() method also tells us how many Non-Null values there are present in each column, and in our data
# set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
#
# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.
#
# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values.
# This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.
