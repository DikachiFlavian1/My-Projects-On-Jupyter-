#!/usr/bin/env python
# coding: utf-8

# Data Setup

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


sns.set_style('whitegrid')


# In[4]:


df = pd.read_csv('911.csv')


# In[5]:


df.info()


# In[6]:


df.head()
#** Check the head of df **


# ** What are the top 5 zipcodes for 911 calls? **

# In[7]:


df['zip'].value_counts().head(5)


# ** What are the top 5 townships (twp) for 911 calls? **

# In[8]:


df['twp'].value_counts().head(5)


# In[9]:


df['title'].nunique()
#checking the  number of unique titles in the title columns 


# ** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.**
# 
# **For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. **

# In[10]:


df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# ** What is the most common Reason for a 911 call based off of this new column? **

# In[11]:


df['Reason'].value_counts()


# ** Now use seaborn to create a countplot of 911 calls by Reason. **

# In[12]:


sns.countplot(x='Reason',data = df)


# ** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **

# In[32]:


type(df['timeStamp'].iloc[0])


# ** You should have seen that these timestamps are still strings. Use pd.to_datetime to convert the column from strings to DateTime objects. **

# In[33]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])


# ** You can now grab specific attributes from a Datetime object by calling them. For example:**
# 
# time = df['timeStamp'].iloc[0]
# time.hour
# You can use Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.

# In[34]:


df['Hour']=df['timeStamp'].apply(lambda time:time.hour)
df['Month']=df['timeStamp'].apply(lambda time:time.month)
df['Day of Week']=df['timeStamp'].apply(lambda time:time.dayofweek)


# In[35]:


time = df['timeStamp'].iloc[0]
time.hour


# In[36]:


time = df['timeStamp'].iloc[0]
time.month


# In[19]:


#df.drop('month',axis =1)


# ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **
# 
# dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

# In[37]:


dmap={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[38]:


df['Day of Week']=df['Day of Week'].map(dmap)


# use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.

# In[39]:


sns.countplot(x = 'Day of Week', data =df,hue ='Reason')


# Now do the same for Month:

# In[27]:


sns.countplot(x='Month',data =df,hue='Reason')


# Did you notice something strange about the Plot?
# 
# ** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **
# 
# ** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **

# In[40]:


byMonth= df.groupby('Month').count()
byMonth.head()


# * Now create a simple plot off of the dataframe indicating the count of calls per month. *

# In[43]:


df['Month'].plot()


# In[45]:


byMonth['title'].plot()


# In[52]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# *Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method.*

# In[56]:


df['Date']=df['timeStamp'].apply(lambda t:t.date())


#  Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

# In[57]:


df.groupby('Date').count()['twp'].plot()
plt.title('Count of Traffic calls')


# In[55]:


df.groupby('Date').count()['twp'].plot()
plt.tight_layout


# * Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call

# In[60]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[61]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout


# In[62]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire ')
plt.tight_layout


#  Now let's move on to creating heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an unstack method. Reference the solutions if you get stuck on this!**

# In[63]:


dayHour =df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()


# * Now create a HeatMap using this new DataFrame. **

# In[64]:


plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')


# In[65]:


sns.clustermap(dayHour,cmap='viridis')


#  Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **

# In[66]:


dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()


# In[67]:


plt.figure(figsize=(14,6))
sns.heatmap(dayMonth,cmap='viridis')


# In[68]:


sns.clustermap(dayMonth,cmap='viridis')


# In[ ]:





# In[ ]:





# In[ ]:




