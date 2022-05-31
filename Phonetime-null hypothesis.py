#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the important packages
import pandas as pd  # Library used for data manipulation and analysis

import numpy as np  # Library used for working with arrays

import matplotlib.pyplot as plt  # Library for visualization

import seaborn as sns  # Library for visualization

get_ipython().run_line_magic('matplotlib', 'inline')

import scipy.stats as stats  # This library contains a large number of probability distributions as well as a growing library of statistical functions


# In[3]:


mydata = pd.read_csv('/Users/yutaoyan/Desktop/Phonetime/Phonetime.csv')

mydata.head()


# In[4]:


mydata.shape


# In[5]:


#Steps of Hypothesis Testing
#Step 1: Define the null and the alternate hypotheses
#Null hypothesis states that the mean Internet usage time, μ
 #is equal to 144. Alternative hypothesis states that the mean Internet usage time, μ
# is not equal to 144.

# H0: μ = 144
# Ha: μ ≠ 144


# In[6]:


#Step 2: Decide the significance level
# Here, we are given that α = 0.05.


# In[7]:


print("The sample size for this problem is", len(mydata))


# In[8]:


#Step 3: Identify the test statistic
# The population is normally distributed and the population standard deviation is known to be equal to 110. 
# So, we can use the Z-test statistic.


# In[9]:


#Step 4: Calculate the p-value using z-statistic


# In[10]:


sample_mean = mydata["Minutes"].mean()


# In[11]:


# Calculating the z-stat

n = 30
mu = 144  
sigma = 110

test_stat =  (sample_mean - mu) / (sigma / np.sqrt(n)) 


# In[12]:


test_stat


# In[13]:


from scipy.stats import norm

# The p-value for one-tailed test
p_value1 = 1 - norm.cdf(test_stat)

# We can find the p_value for the the two-tailed test from the one-tailed test
p_value_ztest = p_value1 * 2


# In[14]:


print('The p-value is: {0} '.format(p_value_ztest))


# In[16]:


# Step 5: Decide to reject or fail to reject the null hypothesis based on the z-statistic


# In[17]:


alpha_value = 0.05 # Level of significance

print('Level of significance: %.2f' %alpha_value)

if p_value_ztest < alpha_value: 
    print('We have the evidence to reject the null hypothesis as the p-value is less than the level of significance'.format(p_value_ztest))
else:
    print('We do not have sufficient evidence to reject the null hypothesis as the p-value is greater than the level of significance'.format(p_value_ztest)) 


# In[18]:


#Step 6: Calculate the p-value using t-statistic


# In[19]:


t_statistic, p_value_ttest = stats.ttest_1samp(mydata, popmean = 144)
print('One sample t-test \nt statistic: {0} p value: {1} '.format(t_statistic, p_value_ttest))


# In[20]:


#Step 7: Decide to reject or not to reject the null hypothesis based on t-statistic


# In[21]:


alpha_value = 0.05 # Level of significance

print('Level of significance: %.2f' %alpha_value)

if p_value_ttest < alpha_value: 
    print('We have the evidence to reject the null hypothesis as the p-value is less than the level of significance'.format(p_value_ttest))
else:
    print('We do not have sufficient evidence to reject the null hypothesis as the p-value is greater than the level of significance'.format(p_value_ttest)) 


# In[ ]:


#CONCLUSION: At a 5% significance level, we do not have enough statistical evidence to prove that the mean time spent on the Internet 
#is not equal to 144 minutes.

