#!/usr/bin/env python
# coding: utf-8

# # Exercise 6: Weather data calculation
# 
# ### Part 1 
# 
# You should start by reading the data file.
# 
# - Read the data file into variable the variable `data`
#     - Skip the second row
#     - Convert the no-data values (`-9999`) into `NaN`

import pandas as pd
import numpy as np

data = None

# YOUR CODE HERE 1
# Read the data from 'data/1091402.txt'
# Specify the path to the file of the data
fp = r'data.txt'
# Read the data by using pd.read_csv
# -9999 is NaN and 1st row is skipped
data = pd.read_csv(fp, delim_whitespace=True, header=0, na_values=-9999, skiprows=[1])

# ### Part 2 
# 
# In this section, you will calculate simple statistics based on the input data:
# 
# - Calculate how many no-data (NaN) values there are in the `TAVG` column
#     - Assign your answer to a variable called `tavg_nodata_count`.

tavg_nodata_count = None
# YOUR CODE HERE 2
# Count the number of NaN in 'TAVG' by using isna().sum()
# This a function of pandas 
tavg_nodata_count = data['TAVG'].isna().sum()

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Number of no-data values in column "TAVG":',tavg_nodata_count)
#CAUTION!!! DON'T EDIT THIS PART END


# - Calculate how many no-data (NaN) values there are for the `TMIN` column
#     - Assign your answer into a variable called `tmin_nodata_count`

tmin_nodata_count = None
# YOUR CODE HERE 3
# Same as above
# Count the number of NaN in 'TMIN'
tmin_nodata_count = data['TMIN'].isna().sum()

# CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Number of no-data values in column "TMIN":', tmin_nodata_count)
#CAUTION!!! DON'T EDIT THIS PART END


# - Calculate the total number of days covered by this data file
#     - Assign your answer into a variable called day_count

day_count = None 
#YOUR CODE HERE 4
# The total number of days is equal to the length of data 
day_count = len(data)

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print("Number of days:", day_count)
#CAUTION!!! DON'T EDIT THIS PART END

# - Find the date of the oldest (first) observation
#     - Assign your answer into a variable called `first_obs`

first_obs = None 
# YOUR CODE HERE 5
# The value of 'DATE' of the first observation day is the less than others
# Set the default value
first_obs = 99999999
# When we find less value of date, update the value
for i in range(len(data)):
  if data['DATE'][i] < first_obs:
    first_obs = data['DATE'][i]

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Date of the first observation:',first_obs)
#CAUTION!!! DON'T EDIT THIS PART END

# - Find the date of the most recent (last) observation
#     - Assign your answer into a variable called `last_obs`

last_obs = None

# YOUR CODE HERE 6
# The value of 'DATE' of the latest observation day is the bigger than others
# Set the default value
last_obs = 00000000
# When we find bigger value of date, update the value
for i in range(len(data)):
  if data['DATE'][i] > last_obs:
    last_obs = data['DATE'][i]

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Date of the last observation:', last_obs)
#CAUTION!!! DON'T EDIT THIS PART END


# - Find the average temperature for the whole data file (all observtions) from column `TAVG`
#     - Assign your answer into a variable called `avg_temp`

avg_temp = None

# YOUR CODE HERE 7
# Average temperature can be found by using np.mean()
avg_temp = np.mean(data['TAVG'])

#CAUTION!!! DON'T EDIT THIS PART START
# Print out the solution:
print('Average temperature (F) for the whole dataset:', round(avg_temp, 2))
#CAUTION!!! DON'T EDIT THIS PART END


# - Find the average `TMAX` temperature over the Summer of 1969 (months May, June, July, and August of the year 1969)
#     - Assign your answer into a variable called `avg_temp_1969`

avg_temp_1969 = None

# YOUR CODE HERE 8
# Make a column which has str type of data['DATE']
data['DATE_STR'] = data['DATE'].astype(str)

# Make a column which has the date data of year and month
data['YEAR_MONTH'] = data['DATE_STR'].str.slice(start=0, stop=6)

# Make a group by groupby
# We want to use 'YEAR_MONTH' as the key
grouped = data.groupby('YEAR_MONTH')

# Specify monthes (as character string)
# This time, we have 4 monthes
monthes = ["196905", "196906", "196907", "196908"]
# Make a list to store mean value of each month
summer_1969_means = []

# For each month, calculate the mean value and append the value to the list, summer_1969_means
for i in range(len(monthes)):
  group = grouped.get_group(monthes[i])
  summer_1969_means.append(group['TMAX'].mean())

# Make sum which will use to calculate total mean
sum = 0
# Add the all value in the list
for i in range(len(summer_1969_means)):
  sum += summer_1969_means[i]
# Calculate avg_temp
avg_temp_1969 = sum / len(summer_1969_means)

#CAUTION!!! DON'T EDIT THIS PART START
# This test print should print a number
print('Average temperature (F) for the Summer of 69:', round(avg_temp_1969, 2))
#CAUTION!!! DON'T EDIT THIS PART END


# ## Problem 2 - Calculating monthly average temperatures (*3 points*)
# 

monthly_data = None

# YOUR CODE HERE 9
# Define a function which convert temp F to temp C
def fahr_to_celsius(temp_fahrenheit):
  """
  Function for converting temperature in Fahrenheit to Celsius.

  Parameters
  ----------
  temp_fahrenheit: <numerical>
      Temperature in Fahrenheit

  Returns
  -------
  <float>
      Converted temperature in Celsius.
  """
  # Calculate converted temperature from temp_fahrenheit
  converted_temp = (temp_fahrenheit - 32) / 1.8
  # Return the result
  return converted_temp

# Convert the TAVG value in Fahrenheit into Celsius
# Make new column, 'temp_celsius' with the calculated value
data['temp_celsius'] = data['TAVG'].apply(fahr_to_celsius)

# I could not solve the problem any more
# I learnt how to find the average temperature for each month by using a key of "MONTH"
# but not sure how to find the average temperature for each month each year
# I have no idea to distinguish between 196904 and 196504

#CAUTION!!! DON'T EDIT THIS PART START
# This test print should print the length of variable monthly_data
print(len(monthly_data))

# This test print should print the column names of monthly_data
print(monthly_data.columns.values)

# This test print should print the mean of temp_celsius
print(round(monthly_data['temp_celsius'].mean(),2))

# This test print should print the median of temp_celsius
print(round(monthly_data['temp_celsius'].median(), 2))
#CAUTION!!! DON'T EDIT THIS PART END

def func1():
    return tavg_nodata_count
def func2():
    return tmin_nodata_count
def func3():
    return day_count
def func4():
    return first_obs
def func5():
    return last_obs
def func6():
    return round(avg_temp,2)
def func7():
    return round(avg_temp_1969,2)
def func8():
    return len(monthly_data)
def func9():
    return monthly_data.columns.values
def func10():
    return round(monthly_data['temp_celsius'].mean(),2)
def func11():
    return round(monthly_data['temp_celsius'].median(),2)