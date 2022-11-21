#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel(r"C:\Users\DELL\Desktop\BDCOE ADDRESS PROJECT\Admit SLU Rest world.xlsx")


# In[3]:


df


# In[201]:


geolocator=Nominatim(user_agent="ketan123@gmail.com",timeout=5)


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.tail()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df['MailingStreet']


# In[10]:


df['MailingCity']


# In[11]:


df['MailingCountry']


# In[12]:


df['MailingCountry'].value_counts()


# In[13]:


df


# In[14]:


new=df.drop(['Application: Application ID', 'Applicant First Name','Applicant Last Name', 'Applicant: Major', 'Primary Phone Number', 'Applicant: Date Application Started', 'Major','Scholarship Value','Applicant: Date Deferred','Admissions Status','Term'], axis=1)


# In[15]:


new


# In[16]:


new['MailingCountry'].value_counts()


# In[17]:


new


# In[18]:


new.head()


# In[19]:


new.tail()


# In[20]:


new.shape


# In[21]:


new.head(10)


# In[22]:


new['Applicant: Mailing Zip/Postal Code'].describe()


# In[23]:


new['MailingStreet']


# In[24]:


new['Mailing Street 2']


# In[25]:


new['MailingCountry']


# In[ ]:





# In[26]:


new


# In[68]:


valid=new.dropna(subset="Applicant: Mailing Zip/Postal Code")


# In[69]:


valid


# In[71]:


valid.rename(columns={"Applicant: Mailing Zip/Postal Code":"Pincode"}, inplace=True)


# In[85]:


valid
valid.drop(valid[(valid.Pincode==0)].index, inplace=True)


# In[87]:


valid


# In[84]:


#val['Applicant: Mailing Zip/Postal Code'].head(50)
valid.shape


# In[135]:


valid=valid.loc[valid["Pincode"].map(type)==int]


# In[142]:


valid.head(51)


# In[141]:


valid.tail(50)


# In[250]:


valid.shape


# In[140]:


valid.reset_index(drop=True,inplace=True)


# In[251]:


valid.isna().sum()


# In[ ]:





# In[ ]:





# In[197]:


valid.drop(columns=['Validity'],inplace=True)


# In[254]:


valid1=valid.copy()


# In[255]:


valid1.head()


# In[256]:


valid1['Predicted']=valid['MailingStreet'].apply(lambda x: geolocator.geocode(x))


# In[257]:


valid1['Predicted'].isnull().sum()


# In[258]:


valid1.dropna(subset='Predicted',inplace=True)


# In[259]:


valid1.head(25)


# In[260]:


valid1.reset_index(drop=True,inplace=True)


# In[261]:


valid1.shape


# In[ ]:





# In[ ]:





# In[ ]:





# In[262]:


valid2=valid1[valid1['Predicted'].isna()]


# In[263]:


valid2.shape


# In[264]:


valid2.head(20)


# In[222]:


invalid_1=valid2[valid2['Mailing Street 2'].isna()]


# In[225]:


valid2.dropna(subset='Mailing Street 2', inplace= True)


# In[224]:


invalid_1.drop(columns=['Predicted'])


# In[227]:


invalid_1.shape #mailing street 2 value is null


# In[273]:


invalid_1.drop(columns=['Predicted'],inplace=True)


# In[275]:


invalid_1.to_csv('Invalid(no mailing street2).csv')


# In[ ]:





# In[ ]:





# In[267]:


valid2['Predicted']=valid2['Mailing Street 2'].apply(lambda x: geolocator.geocode(x))


# In[268]:


valid2.isna().sum()


# In[269]:


valid2.dropna(subset='Predicted',inplace=True)


# In[270]:


valid2.reset_index(drop=True,inplace=True)


# In[241]:


valid2.head(20)


# In[242]:


valid_1=valid1.copy()


# In[243]:


valid_2=valid2.copy()


# In[246]:


validd=valid_1.append(valid_2)


# In[248]:


validd.head(37)


# In[276]:


invalidd=validd.copy()


# In[277]:


validd=validd.loc[validd["MailingStreet"].map(type)!=int]


# In[278]:


validd


# In[279]:


invalidd=invalidd.loc[invalidd["MailingStreet"].map(type)==int]


# In[291]:


invalidd.reset_index(drop=True,inplace=True)


# In[293]:


invalidd.head()


# In[294]:


invalid=invalid_1.append(invalidd)


# In[297]:


invalid.drop(columns=['Predicted'],inplace=True)


# In[299]:


invalid.reset_index(drop=True,inplace=True)


# In[301]:


invalid.head(50)


# In[300]:


invalid.shape


# In[306]:


invalid.to_csv('Invalid Files 1.csv',index_label=False)


# In[307]:


dff=pd.read_csv('./Invalid Files 1.csv')


# In[308]:


dff.head(35)


# In[ ]:





# In[ ]:





# In[292]:


invalidd.to_csv('Invalid with mailing street int.csv')


# In[285]:


validd.drop(2,inplace=True)


# In[284]:





# In[286]:


validd.reset_index(drop=True,inplace=True)


# In[287]:


validd.head(40)


# In[309]:


validd.to_csv('Valid Address.csv',index_label=False)


# In[ ]:





# In[ ]:





# In[ ]:


#Invalid Part


# In[ ]:





# In[310]:


new.shape


# In[311]:


new.isna().sum()


# In[312]:


valid=new.dropna(subset="Applicant: Mailing Zip/Postal Code")


# In[313]:


valid.rename(columns={"Applicant: Mailing Zip/Postal Code":"Pincode"}, inplace=True)


# In[314]:


valid


# In[315]:


invalid=valid.drop(valid[(valid.Pincode!=0)].index)


# In[316]:


invalid.to_csv('Invalid(zero).csv')


# In[317]:


invalid1=valid.loc[valid["Pincode"].map(type)==str]


# In[318]:


invalid1.to_csv('Invalid(str).csv')


# In[319]:


invalidd=invalid.append(invalid1)


# In[320]:


invalidd.shape


# In[321]:


invalidd.head(18)


# In[322]:


invalid = new[new['Applicant: Mailing Zip/Postal Code'].isna()]


# In[323]:


invalid.shape


# In[324]:


invalid.head(30)


# In[325]:


df1=pd.read_csv('./Invalid Files 1.csv')


# In[326]:


df1.shape


# In[327]:


invalid=invalid.append(df1)


# In[328]:


invalid.drop(columns=['Applicant: Mailing Zip/Postal Code'],inplace=True)


# In[329]:


invalid.shape


# In[330]:


invalid=invalid.append(invalidd)


# In[331]:


invalid.shape


# In[332]:


invalid.reset_index(drop=True,inplace=True)


# In[333]:


invalid.to_csv('Invalid Addresses.csv',index_label=False)


# In[334]:


invalid.head(34)


# In[ ]:




