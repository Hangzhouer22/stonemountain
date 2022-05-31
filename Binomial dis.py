#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the important libraries

import pandas as pd  # Library used for data manipulation and analysis

import numpy as np  # LIbrary used for working with arrays

import matplotlib.pyplot as plt  # Library for visualization

import seaborn as sns  # Library for visualization


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

import scipy.stats as stats  # This library contains a large number of probability distributions as well as a growing library of statistical functions


# In[3]:


# Declare the sample size in variable n that represents the number of doses given to the volunteers 
n = 100


# In[7]:


# Declare p that represents the probability of success, i.e., the probability that a dose will not do a satisfactory job
p = 0.09


# In[5]:


# Declare p that represents the probability of success, i.e., the probability that a dose will not do a satisfactory job
p = 0.09


# In[6]:


# Declare the different number of doses selected in a NumPy array
k = np.arange(0, 101)

k


# In[8]:


# Import the binom function from the scipy library
from scipy.stats import binom

# Use the binom.pmf() function to generate the probability distribution
binomial = binom.pmf(k = k, n = n, p = p)


# In[9]:


binomial


# In[10]:


#plot the probaility distribution


# In[11]:


# Plot the distribution
plt.bar(k, binomial)

plt.xlim(-10, 50)

plt.title('Binomial: n = %i, p = %.2f' % (n, p), fontsize = 15)

plt.xlabel('Number of Doses')

plt.ylabel('Probability that doses will not do a satisfactory job')

plt.show()


# In[12]:


binomial[3]


# In[13]:


#What is the probability that at most 3 doses will not do a satisfactory job out of 100 selected?


# In[14]:


# Plot the probability distribution
# We are plotting the distributions here to better visualize the calculations
# Ofcourse, you do not 'need' to create the following visualization to answer the question above 
# You can directly use the cdf function for probability calculations

barl = plt.bar(k, binomial)

plt.xlim(-10, 50)

plt.title('Binomial: n = %i, p = %.2f' % (n, p), fontsize = 15)

plt.xlabel('Number of Doses')

plt.ylabel('Probability that doses will not do a satisfactory job')

for i in range(0, 4):
    barl[i].set_color('r')
plt.show()


# In[16]:


#Let's calculate the probability that out of 100 randomly selected doses, at most 3 will not do a satisfactory job. We will use binom.cdf() for this.


# In[15]:


# Calculate the cdf
from scipy.stats import binom

prob_atmost3 = binom.cdf(k = 3, n = n, p = p)

print(prob_atmost3)


# In[17]:


# Declare the sample size in variable n which represents the number of doses selected randomly
n = 200

# Declare p which represents the probability of success, i.e., the probability that a dose will not do a satisfactory job
p = 0.09

# Declare the different number of doses selected in a NumPy array
k = np.arange(0, 201)


# In[18]:


k


# In[19]:


# Import the required function
from scipy.stats import binom

# Use the binom.pmf() function to generate the probability distribution
binomial = binom.pmf(k = k, n = n, p = p)


# In[20]:


# Plot the probability distribution
# We are plotting the distributions here to better visualize the calculations
# Ofcourse, you do not 'need' to create the following visualization to answer the question above
# You can directly use the cdf function for probability calculations

barl = plt.bar(k, binomial, width = 0.7)

plt.xlim(-10, 50)

plt.title('Binomial: n = %i, p = %.2f' % (n, p), fontsize = 15)

plt.xlabel('Number of Doses')

plt.ylabel('Probability that doses will not do a satisfactory job')

for i in range(30, 201):
   barl[i].set_color('r')

plt.show()


# In[21]:


# Calculate cdf
prob_atleast30 = 1 - binom.cdf(k = 29, n = 200, p = 0.09)

print(prob_atleast30)


# In[ ]:





# In[23]:


drug = pd.read_csv('/Users/yutaoyan/Desktop/Medicon/doses.csv')

drug.head()


# In[24]:


drug.info()


# In[25]:


# Import the required function
from scipy.stats import norm 

# Estimate the mean and standard deviation of the time of effect for the doses
mu = drug['time_of_effect'].mean() 

sigma = drug['time_of_effect'].std()

print('The estimated mean is', round(mu, 2))
# Import the required function
from scipy.stats import norm 

# Estimate the mean and standard deviation of the time of effect for the doses
mu = drug['time_of_effect'].mean() 

sigma = drug['time_of_effect'].std()

print('The estimated mean is', round(mu, 2))

print('The estimated standard deviation is', round(sigma, 2))


# In[26]:


#Plotting the Distribution
#It will help us analyze the shape of the distribution of time of effect for doses. 


# In[27]:


import seaborn as sns

sns.displot(drug['time_of_effect'], kind = "kde")


# In[28]:


#We can observe from the above plot that the shape of the distribution is not
#perfectly normal because we have just 50 observations in the sample. But, we 
#can assume this data distribution to 
#be normal and perform our calculations based on the normality assumption.


# In[29]:


#What is the probability that the time of effect is less than 11.5 hours?


# In[30]:


# Find the cumulative probability
# norm.cdf() calculates the cumulative probability
prob = norm.cdf(11.5, mu, sigma)

print('The probability that a dose will take less than 11.5 hours is', round(prob, 4))


# In[31]:


#b) What is the 90th percentile of the time of effect for doses?


# In[32]:


perc_90th = norm.ppf(0.90, mu, sigma)


# In[33]:


print('The 90th percentile of the time of effect for doses is', round(perc_90th, 2))


# In[34]:


#For the effectiveness test of the vaccine, estimate the range which will contain the population mean 
#(time of effect) with a 95% confidence level.

#The population standard deviation is not known here. Therefore, we will calculate the confidence 
#interval using the t-distribution.


# In[35]:


# Import the required function
from scipy.stats import t

# Set the values of sample mean and sample standard deviation
x_bar, s = mu, sigma

# Set the value of sample size and degrees of freedom
n = 50
k = n - 1
# Construct the confidence interval
np.round(t.interval(0.95, df = k, loc = x_bar, scale = s/np.sqrt(n)), 2)


# In[ ]:


#With a 95% confidence level, we can say that the interval [12.09, 14.79] will contain the population mean of the effective time for doses.

