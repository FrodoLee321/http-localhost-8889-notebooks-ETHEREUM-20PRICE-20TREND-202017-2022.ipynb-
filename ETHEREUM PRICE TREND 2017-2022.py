#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt 
import pandas as pd 


# In[2]:


df = pd.read_csv('ethereumdata.csv')


# In[3]:


print(df.shape)
df.info()


# In[4]:


df.head()


# In[38]:


df.describe()


# In[44]:


from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook


# In[58]:


output_notebook()


# In[52]:


import matplotlib.pyplot as plt


# In[66]:


xvalues = ('11/9/2017','11/10/2017','11/11/2017','11/12/2017','11/13/2017')
yvalues = ('309','321','299','315','307')
zvalues = ('321','299','315','308','317')
plt.plot(xvalues,yvalues,zvalues)
plt.title('ETH OPENING PRICE 2017')
plt.show()


# In[76]:


xvalues = ('11/9/2017','11/10/2017','11/11/2017','11/12/2017','11/13/2017')
zvalues = ('321','299','315','308','317')
yvalues = ('307','295','298','299','307')
plt.plot(xvalues,zvalues,yvalues)
plt.title('ETH CLOSING PRICE 2017')
plt.show()


# In[74]:


xvalues = ('11/9/2017','11/10/2017','11/11/2017','11/12/2017','11/13/2017')
yvalues = ('893249984','885985984','842300992','1613479936','1041889984')
plt.bar(xvalues,yvalues, color = 'red')
plt.title('ETH PRICE VOLUME 2017')
plt.show()


# In[77]:


df.tail()


# In[79]:


xvalues= ('3/21/2022','3/22/2022','3/23/2022','3/24/2022','3/25/2022')
yvalues= ('2860','2898','2973','3031','3110')
zvalues= ('2955','3040','3037','3118','3183')
plt.plot(xvalues,yvalues,zvalues)
plt.title ("ETH OPENING PRICE 2022")
plt.show()


# In[85]:


xvalues= ('3/21/2022','3/22/2022','3/23/2022','3/24/2022','3/25/2022')
yvalues= ('2898','2973','3031','3108','3123')
zvalues= ('2838','2893','2933','3012','3098')
plt.plot(xvalues,yvalues,zvalues)
plt.title ("ETH CLOSING PRICE 2022")
plt.show()


# In[86]:


xvalues= ('3/21/2022','3/22/2022','3/23/2022','3/24/2022','3/25/2022')
yvalues= ('15206116098','16830539230','16008767658','18070503166','16882068480')
plt.bar(xvalues,yvalues, color = 'red')
plt.title('ETH PRICE VOLUME 2022')
plt.show()


# In[ ]:




