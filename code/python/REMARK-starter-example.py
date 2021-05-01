#!/usr/bin/env python
# coding: utf-8

# In[1]:



# ## A Sample Notebook in a Sample REMARK
# 
# An example notebook which has some basic content which a REMARK may include.
# 
# The REMARK notebook shouldn't just contain the code, use the markdown cells to explain the code and models.


# In[2]:


# required imports
from HARK.ConsumptionSaving.ConsPrefShockModel import KinkyPrefConsumerType
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


# Make and solve a preference shock consumer
PrefShockExample = KinkyPrefConsumerType()
PrefShockExample.cycles = 0  # Infinite horizon
PrefShockExample.solve()


# In[4]:


# Unpack the consumption function for easier access.
PrefShockExample.unpack('cFunc')
PrefShockExample.unpack('mNrmMin')


# In[5]:


# Plot the consumption function at each discrete shock
m = np.linspace(PrefShockExample.mNrmMin[0], 5, 200)
for j in range(PrefShockExample.PrefShkDstn[0].pmf.size):
    PrefShk = PrefShockExample.PrefShkDstn[0].X[j]
    c = PrefShockExample.cFunc[0](m, PrefShk * np.ones_like(m))
    plt.plot(m, c)
plt.xlim([-1.0, None])
plt.ylim([0.0, None])
plt.savefig('../../figures/cFunc.pdf')
plt.ion() # Necessary so that when executed from the command line it does not wait for user input
plt.show()


# In[6]:


# Import custom code and plot the figure.

from custom_code import plot_distribution
# Save this figure in the figures directory.
path = '../../figures/dist.pdf'
plot_distribution(100, 15, path)

