#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset (tmdb dataset investigation)

# 
# ## Introduction:-
# 

# ### This Data set contains about 10,000 movies that have collected from (TMDB) database.
# 
# ### I will provide the questions that will be answered in the conclusions.
# 
# #### 1- Analyze the runtime average to see each movie's runtime
# #### 2-Is there is a relationship between the rating of the movie and the budget?
# #### 3-what are the most frequent genres?

# In[582]:


import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties:-

# In[583]:


#reading the csv
df = pd.read_csv('tmdb-movies.csv')
#having a look of the first 5 rows in the dataset
df.head()


# In[584]:


df.shape


# In[585]:


#Exploring the dataset
df.describe()


# In[586]:


#I want to have an information about the data and check what columns I don't need
df.info() 


# ### Data Cleaning (Removing useless information from the dataset)

# In[587]:


#dropping columns that I don't need
df.drop(['id','imdb_id','homepage','tagline', 'keywords' , 'overview', 'production_companies', 'budget_adj', 'revenue_adj', 'release_date'],axis=1 , inplace=True)
df.head()


# In[588]:


#After I dropped the column that I don't need, I wan't to have an information about the column that have missing values
df.info()


# ## dropping null and zero values

# In[589]:


#dropping null values
df.dropna(inplace=True)
df.info()


# In[590]:


#Get average of budget_adj
print(df['budget'].mean())


# In[591]:


#Replace 0 values with mean.
df['budget'] = df['budget'].replace(0, 14805062.129332837)


# In[592]:


#Get average of revenue_adj
print(df['revenue'].mean())


# In[593]:


#Replace 0 values with mean
df['revenue'] = df['revenue'].replace(0, 40316220.714405514)


# In[594]:


#Get average of runtime
print(df['runtime'].mean())


# In[595]:


df['runtime'] = df['runtime'].replace(0, 102.46785314945956)


# In[596]:


#Exploring the data after i got rid of the missing values
df.describe()


# In[597]:


#representing a general idea about the data
df.hist(figsize = (15 , 15));


# 
# ## Exploratory Data Analysis
# 
# 
# ## Research question 1: Analyzing the runtime average

# just to make everything clear, the runtime measurement is by minutes.

# In[598]:


#applying a function for the column average
def avg_fun(column):
    return df[column].mean()


# In[599]:


#calling the function
avg_fun('runtime')


# In[600]:


#This will be the visualization of the runtime

#the size of the chart
plt.figure(figsize=(15,7))
#x-axis title
plt.xlabel('Movies runtime', fontsize = 18)
#y-axis title 
plt.ylabel('Total movies', fontsize=18)
#title of the graph
plt.title('Runtime of all movies', fontsize=30)
#plotting
plt.hist(df['runtime'] , bins=60)
#displaying the plot
plt.show()


# #### As we can see there are approximatley more than 4000 movies that lie between 90-110 minutes. Almost 1800 movies that lie in this period!

# ## Research Question 2: Is there is a relationship between the rating of the movie and the budget?

# In[601]:


df.plot(x='vote_average', y='budget', kind='scatter', figsize=(15,10))
#Size of the chart
plt.title('Relationship between the rating and the budget')
#title of the chart
plt.xlabel('Rating',)
#x-axis title
plt.ylabel('budget');
#y-axis title


# #### Clearly the budget doesn't affect the rating of the movie, probably thats because older movies don't need a higher budget, and also the vote count can affect the rating because it differs from one movie to another.

# ## Research Question 3: Most frequent genres:

# In[602]:


#giving a function that that take a column as an argument and keep its track
def split_multiple_values(x):
#splitting the entire string generated into separate strings
    data_plot = df[x].str.cat(sep = '|')
#putting all individual values in a pandas Series  
    data = pd.Series(data_plot.split('|'))
    count = data.value_counts()
    return count


# In[603]:


#I want to see the genres column after i splitted the strings
print( split_multiple_values('genres'))


# In[611]:


count.sort_values(inplace = True)
#ploting
bar = count.plot.barh(color = 'gray', fontsize = 12)
#title
bar.set(title = 'Frequent Used Genres')
#x-axis
bar.set_xlabel('number of movies', color = 'black', fontsize = 14)
#chart size(width, height)
bar.figure.set_size_inches(12, 9)
#displaying the plot
plt.show()


# #### As shown in the barchart, Drama category is the most frequent category. That gives us a clear understanding that many people tend to watch Drama movies.

# # Conclusions

# ## This was my investigation about the (TMDB) database I'm going to give an answers that I asked in the introduction.
# 
# ### First of all, I analyzed the movie runtime average. From the histogram It was really interresting that more than 4000 movies fall between 90-110 isn't that odd?
# 
# ### Second point, I want to know what is the relationship between the rating of the movie and the budget, From the scatter plot I saw that they are not related. I really thought that they have a strong relationship but a good movie doesn't need a high budget!
# 
# ### In the end, I wanted to know what is the most frequent genre, I figure that Drama genre is the most frequent. That's what I expected, But the Action genre didn't meet my expectations I thought it would be the second.
# 
# ## As my first dataset investigation, I found it very inspiring, because some of the questions didn't meet my expectations I understood it more when I did the visualization. When I answered the questions the dataset was understandable.
# 

# # Limitations

# ### this dataset is just a sample from a population, all the results are not generizable. I had to deal with missing values by dropping null values, and dealing with numeric data by filling zero values with the mean so it might be inaccurate, especially when filling the budget and revenue. Filling runtime with the mean can be more considerable since approximatley 75% of the movies fall around the mean.
