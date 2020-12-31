############ FINAL LAB - SECTION 1 (EXTERNAL RESOURCE) ########
###############################################################
# Question 1
###############################################################
# Import pandas 
import pandas as pd

# Use pandas to read in recent_grads_url
recent_grads = pd.read_csv(recent_grads_url)

# Print the shape
print(recent_grads.shape)

###############################################################
# Question 2
###############################################################
# Print .dtypes
print(recent_grads.dtypes)

# Output summary statistics
print(recent_grads.describe())

# Exclude data of type object
print(recent_grads.describe(exclude=["object"]))

###############################################################
# Question 3
###############################################################
# Names of the columns we're searching for missing values 
columns = ['median', 'p25th', 'p75th']

# Take a look at the dtypes
print(recent_grads[columns].dtypes)

# Find how missing values are represented
print(recent_grads["median"].unique())

# Replace missing values with NaN
for column in columns:
    recent_grads.loc[recent_grads[column] == 'UN', column] = np.nan
    
###############################################################
# Question 4
###############################################################
# Select sharewomen column
df = pd.DataFrame(recent_grads)
sw_col = df['sharewomen']

# Output first five rows
print(sw_col.head(5))

###############################################################
# Question 5
###############################################################
# Import numpy
import numpy as np

# Use max to output maximum values
max_sw = np.max(sw_col)

# Print column max
print(max_sw)

###############################################################
# Question 6
###############################################################
# Output the row containing the maximum percentage of women
print(recent_grads[sw_col == max_sw])

###############################################################
# Question 7
###############################################################
# Convert to numpy array
recent_grads_np = recent_grads[["unemployed", "low_wage_jobs"]].values

# Print the type of recent_grads_np
print(type(recent_grads_np))

###############################################################
# Question 8
###############################################################
# Calculate correlation matrix
print(np.corrcoef(recent_grads_np[:,0], recent_grads_np[:,1]))


############ FINAL LAB - SECTION 2 (EXTERNAL RESOURCE) ########
###############################################################
# Question 1
###############################################################
# Add sharemen column
recent_grads['sharemen'] = recent_grads['men'] / recent_grads['total']

# Confirm colum was added
# print(recent_grads.dtypes)

###############################################################
# Question 2
###############################################################
# Find the maximum percentage value of men
max_men = np.max(recent_grads['sharemen'])
 
# Output the row with the highest percentage of men
print(recent_grads[recent_grads['sharemen'] == max_men])

###############################################################
# Question 3
###############################################################
# Add gender_diff column
recent_grads['gender_diff'] = recent_grads['sharewomen'] - recent_grads['sharemen']

###############################################################
# Question 4
###############################################################
# Make all gender difference values positive
recent_grads['gender_diff'] = np.abs(recent_grads['gender_diff'])

# Find the 5 rows with lowest gender rate difference
print(recent_grads.nsmallest(5, 'gender_diff'))

###############################################################
# Question 5
###############################################################
# Rows where gender rate difference is greater than .30 
diff_30 = recent_grads['gender_diff'] > .30

# Rows with more men
more_men = recent_grads['sharemen'] > recent_grads['sharewomen']

# Combine more_men and diff_30
more_men_and_diff_30 = np.logical_and(more_men, diff_30)

# Find rows with more men and and gender rate difference greater than .30
fewer_women = recent_grads[more_men_and_diff_30]

###############################################################
# Question 6
###############################################################
# Group by major category and count
print(recent_grads.groupby(['major_category']).major_category.count())

###############################################################
# Question 7
###############################################################
# Group departments that have less women by category and count
print(fewer_women.groupby(['major_category']).major_category.count())

###############################################################
# Question 8
###############################################################
# Report average gender difference by major category
print(recent_grads.groupby(['major_category']).gender_diff.mean())

###############################################################
# Question 9
###############################################################
# Find average number of low wage jobs and unemployment rate of each major category
dept_stats = recent_grads.groupby(['major_category'])['low_wage_jobs', 'unemployment_rate'].mean()
print(dept_stats)


############ FINAL LAB - SECTION 2 (EXTERNAL RESOURCE) ########
###############################################################
# Question 1
###############################################################
# Import matplotlib
import matplotlib.pyplot as plt

# Create scatter plot
plt.scatter(unemployment_rate, low_wage_jobs)

# Label x axis
plt.xlabel('Unemployment rate')

# Label y axis
plt.ylabel('Low pay jobs')

# Display the graph 
plt.show()

###############################################################
# Question 2
###############################################################
# Plot the red and triangle shaped scatter plot  
plt.scatter(unemployment_rate, low_wage_jobs, color = "r", marker = "^")

# Display the visualization
plt.show()

###############################################################
# Question 3
###############################################################
# Plot a histogram of sharewomen
plt.hist(sharewomen)

# Show the plot
plt.show()

###############################################################
# Question 4
###############################################################
# Import matplotlib and pandas
import matplotlib.pyplot as plt
import pandas as pd

# Create scatter plot
dept_stats.plot(kind='scatter', x='unemployment_rate', y='low_wage_jobs')
plt.show()

# Create histogram plot
recent_grads.sharewomen.plot(kind='hist')
plt.show()

###############################################################
# Question 5
###############################################################
# DataFrame of non-college job sums
df = recent_grads.groupby(['major_category']).non_college_jobs.sum()

# Plot bar chart
df.plot(kind="bar")

# Show graph
plt.show()

###############################################################
# Question 6
###############################################################
# DataFrame of college and non-college job sums
df1 = recent_grads.groupby(['major_category'])['college_jobs','non_college_jobs'].sum()

# Plot bar chart
df1.plot(kind="bar")

# Show graph
plt.show()

###############################################################
# Question 7
###############################################################
# Print the size of the DataFrame
print(recent_grads.size)

# Drop all rows with a missing value
recent_grads.dropna(axis = 0, inplace = True)

# Print the size of the DataFrame
print(recent_grads.size)

###############################################################
# Question 8
###############################################################
# Convert to numeric and divide by 1000
recent_grads['median'] = pd.to_numeric(recent_grads['median'])/ 1000
recent_grads['p25th'] = pd.to_numeric(recent_grads['p25th'])/ 1000
recent_grads['p75th'] = pd.to_numeric(recent_grads['p75th'])/ 1000

# Select averages by major category
columns = ['median', 'p25th', 'p75th']
sal_quantiles = recent_grads.groupby(['major_category'])['median', 'p25th', 'p75th'].mean()

###############################################################
# Question 9
###############################################################
# Plot the data
sal_quantiles.plot()

# Set xticks
plt.xticks(
    np.arange(len(sal_quantiles.index)),
    sal_quantiles.index, 
    rotation='vertical')

# Show the plot
plt.show()

# Plot with subplots
sal_quantiles.plot(subplots=True)

# Show the plot
plt.show()
###############################################################
