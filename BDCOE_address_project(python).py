#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import os


# In[2]:


geolocator = Nominatim(user_agent="bdcoeproject@gmail.com", timeout=3)


# In[3]:


df = pd.read_excel(r".\Admit SLU Rest world.xlsx" )
df


# In[4]:


print(df.shape)


# In[5]:


print(df.describe())


# In[6]:


print(df['MailingStreet'])


# In[7]:


print(df['MailingCity'])


# In[8]:


print(df['MailingCountry'])


# In[9]:


print(df['MailingCountry'].value_counts())


# In[10]:


print(df.count())


# In[11]:


new=df.drop(['Application: Application ID', 'Applicant First Name','Applicant Last Name', 'Applicant: Major', 'Primary Phone Number', 'Applicant: Date Application Started', 'Major','Scholarship Value','Applicant: Date Deferred','Admissions Status','Term'], axis=1)
print(new)


# In[12]:


print("No. of addresses where ZIP codes are not present")
new['Applicant: Mailing Zip/Postal Code'].isna().sum()


# In[13]:


print("No. of addresses where Mailing City is not present")
new['MailingCity'].isna().sum()


# In[14]:


print("No. of addresses where Mailing street is not present")
new['MailingStreet'].isna().sum()


# In[ ]:





# In[15]:


invalid = df[new['Applicant: Mailing Zip/Postal Code'].isna()]


# In[16]:


#print(invalid)


# In[17]:


invalid['Valid/InValid'] = 'Invalid'
print(invalid)


# In[18]:


invalid['predicted_area'] = invalid['MailingCity'].apply(lambda x: geolocator.geocode(x))


# In[19]:


invalid['predicted_address'] = invalid['MailingStreet'].apply(lambda x: geolocator.geocode(x))


# In[20]:


print(invalid)


# In[49]:


invalid.to_csv("InValid_Address_csv")


# In[21]:


new = new.dropna(axis=0, subset=['Applicant: Mailing Zip/Postal Code'])


# In[22]:


print(new)


# In[23]:


# new['predicted_area'] = new['MailingCity'].apply(lambda x: geolocator.geocode(x))


# In[24]:


#new


# In[25]:


# new['predicted_address'] = new['MailingStreet'].apply(lambda x: geolocator.geocode(x))


# In[26]:


new.info()
new.reset_index(drop=True, inplace=True)


# In[ ]:





# In[27]:


print(new.shape)


# In[28]:


new.to_csv("New Updated Address1")


# In[29]:


import csv


# In[30]:


with open(r"./New Updated Address1") as file_obj:
    reader_obj=csv.reader(file_obj)
    for row in reader_obj:
        print(row)


# In[43]:


df=pd.read_csv(r"./new Updated Address1")
df.dropna(subset=["Mailing Street 2"],inplace=True)
df.drop_duplicates()
df.isnull().sum()
print(df)


# In[41]:


# df["MailingStreet"]=df["MailingStreet"]+ "," + df["MailingCity"] + "," + df["MailingCountry"]
# df["MailingStreet"]


# In[44]:


df["Validity"]=df["Mailing Street 2"]+"," +df["MailingCity"]
print(df["Validity"])


# In[45]:


df["Address"]=df["Validity"].apply(lambda x: geolocator.geocode(x))
FinalAddress=df[["Address"]]


# In[ ]:





# In[46]:


print(FinalAddress.head(30))


# In[47]:


FinalAddress.to_csv("Valid_Address_csv")


# In[ ]:




