#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn import model_selection

import requests
import io


# In[3]:


# a personal access token used to access CSV from private GitHub repo
username = 'christiecngo'
token = '5d8f328a166fa215b26ce44be820468924d3cbb0'
github_session = requests.Session()
github_session.auth = (username, token)

url = "https://raw.githubusercontent.com/ALDUCHWE/prop21/master/datachallenge-crime.csv?token=ARABRMAEAIML6MXFTNDASLS7NK5AC" 
download = github_session.get(url).content

# crime csv read into pandas
crime_numbers = pd.read_csv(io.StringIO(download.decode('utf-8')))


# In[4]:


url2 = "https://raw.githubusercontent.com/ALDUCHWE/prop21/master/datachallenge-homelessness.csv?token=ARABRMGKQG3KQWJHIIEME427NK5F2"
download2 = github_session.get(url2).content

homeless_numbers = pd.read_csv(io.StringIO(download2.decode('utf-8')))
homeless_numbers.head(10)


# In[5]:


# reading SF and SD features from excel files
sd_unemployment = pd.read_excel("SD Unemployment.xls")
sf_unemployment = pd.read_excel("SF Unemployment.xls")


# In[6]:


sd_population = pd.read_excel("datachallenge-populationSD.xlsx")
sf_population = pd.read_excel("datachallenge-populationSF.xlsx")


# In[7]:


url4 = "https://raw.githubusercontent.com/ALDUCHWE/prop21/master/SF%20MEDIAN%20INCOME%20csv.csv?token=ARABRMC5P3T3AM6QATHE4OS7NK7J6"
download4 = github_session.get(url4).content

sf_income = pd.read_csv(io.StringIO(download4.decode('utf-8')))

url5 = "https://raw.githubusercontent.com/ALDUCHWE/prop21/master/sd%20median%20income%20csv.csv?token=ARABRMC5XS7IGHU6LD7DSLK7NK7PW"
download5 = github_session.get(url5).content

sd_income = pd.read_csv(io.StringIO(download5.decode('utf-8')))


# In[8]:


# created one dataframe with data from all files for SF and SD
df_x_raw = pd.concat([crime_numbers, sf_unemployment, sd_unemployment, sf_income, sd_income, sf_population, sd_population], axis=1)
# dependent variable data is homeless count in cities
df_y = pd.DataFrame(homeless_numbers)


# In[9]:


# changed crime number data from strings to float by removing commas
df_y["TotalSF"] = df_y.iloc[:,1].str.replace(',', '').astype(float)
df_y["TotalSD"] = df_y.iloc[:,2].str.replace(',', '').astype(float)


# In[10]:


# refined dataframe to remove repeated column names (year) and extra year - 2019
df_x = df_x_raw.iloc[:, [0,1,2,4,6,8,10,12,14]]
df_x.drop(df_x.tail(1).index,inplace=True);

# renamed columns of data frame
df_x.columns = ["Year", "SF-Crime", "SD-Crime", "SF-UNEMP", "SD-UNEMP", "SF-Income", "SD-Income", "SF-Pop", "SD-Pop"]
df_x;


# In[11]:


df_x["SF-Crime"]=df_x.iloc[:,1].str.replace(',', '').astype(float)
df_x["SD-Crime"]=df_x.iloc[:,2].str.replace(',', '').astype(float)


# In[12]:


# created separate dataframes using data only for each city 
sf_y = df_y.iloc[:-1, 1]
sd_y = df_y.iloc[:-1, 2]


# In[13]:


df_sf = df_x.iloc[:, [1,3,5,7]]
df_sd = df_x.iloc[:, [2,4,6,8]]


# In[14]:


df_sd2 = df_sd.iloc[:, [0,1,2]]
sd_y2 = sd_y.iloc[:,]


# In[16]:


df_sf2 = df_sf.iloc[:, [0,1,2]]
sf_y2 = sf_y.iloc[:,]


# In[17]:


xsd_train2, xsd_test2, ysd_train2, ysd_test2 = model_selection.train_test_split(df_sd2, sd_y2, test_size = 0.2, random_state = 0)
xsf_train2, xsf_test2, ysf_train2, ysf_test2 = model_selection.train_test_split(df_sf2, sf_y2, test_size = 0.2, random_state = 0)


# In[19]:


import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

xsd_train2 = sm.add_constant(xsd_train2)
modelsd2 = sm.OLS(ysd_train2, xsd_train2)
resultsd2 = modelsd2.fit()


# In[20]:


xsf_train2 = sm.add_constant(xsf_train2)
modelsf2 = sm.OLS(ysf_train2, xsf_train2)
resultsf2 = modelsf2.fit()


# In[42]:


# using a rent control city (SF) to predict the homelessness in San Jose (tried without population as a feature)
sanjose_2 = predicting_sj.iloc[:, [0,1,2,3]]
sanjose_preds2 = resultsd2.predict(sanjose_2)
plt.figure(dpi = 75)
plt.scatter(homeless_sj, sanjose_preds2)
plt.plot(homeless_sj, homeless_sj, color="red")
plt.ylabel("Predicted # of Homeless Persons Based on Rent Controlled City")
plt.xlabel("Actual # SJ Homeless Persons")
plt.title("Actual vs Predicted Homeless Persons Count")
plt.show()


# In[43]:


# using a non-rent control city (SD) to predict the homelessness in Fresno (tried without population as a feature)
fresno_2 = predicting_fresno.iloc[:, [0,1,2,3]]
fresno_preds2 = resultsd2.predict(fresno_2)
plt.figure(dpi = 75)
plt.scatter(homeless_fresno, fresno_preds2)
plt.plot(homeless_fresno, homeless_fresno, color="red")
plt.ylabel("Predicted # of Homeless Persons Based on Rent Controlled City")
plt.xlabel("Actual # Fresno Homeless Persons")
plt.title("Actual vs Predicted Homeless Persons Count")
plt.show()


# In[22]:


# split data into training and testing sets for SF features

xsf_train, xsf_test, ysf_train, ysf_test = model_selection.train_test_split(df_sf, sf_y, test_size = 0.2, random_state = 0)
xsf_train.head(5)


# In[23]:


# checked for collinearity between each independent variabel in SF
corr_sf = xsf_train.corr(method = 'pearson')
mask = np.zeros_like(corr_sf)
mask[np.triu_indices_from(mask)] = True
seaborn.heatmap(corr_sf, cmap= 'CMRmap', vmax = 1.0, vmin = -1.0, mask = mask, linewidths = 2.5)
plt.yticks(rotation = 0)
plt.xticks(rotation = 90)
plt.show()


# In[24]:


# repeated heatmap for SD to check collinearity
xsd_train, xsd_test, ysd_train, ysd_test = model_selection.train_test_split(df_sd, sd_y, test_size = 0.2, random_state = 0)


# In[25]:


corr_sd = xsd_train.corr(method = 'pearson')
mask1 = np.zeros_like(corr_sd)
mask1[np.triu_indices_from(mask1)] = True
seaborn.heatmap(corr_sd, cmap= 'CMRmap', vmax = 1.0, vmin = -1.0, mask = mask1, linewidths = 2.5)
plt.yticks(rotation = 0)
plt.xticks(rotation = 90)
plt.show()


# In[26]:


regressionsf = linear_model.LinearRegression(fit_intercept = True, normalize = False,  copy_X= True , n_jobs = 1)
regressionsf.fit(xsf_train, ysf_train)


# In[27]:


regressionsf.intercept_


# In[28]:


regressionsd = linear_model.LinearRegression(fit_intercept = True, normalize = False,  copy_X= True , n_jobs = 1)
regressionsd.fit(xsd_train, ysd_train)
regressionsd.intercept_


# In[246]:


print('SF Coefficients:', regressionsf.coef_)


# In[247]:


print('SD Coefficients:', regressionsd.coef_)


# In[29]:


regressionsf.coef_.tolist()


# In[30]:


columnnames = ["SF-Crime", "SF-UMEMP", "SF-Income", "SF-Pop"]
sf_eq = pd.DataFrame(zip(columnnames, regressionsf.coef_.tolist()), columns = ["Feature", "Coefficient"])

sf_eq


# In[31]:


columnnames1 = ["SD-Crime", "SD-UMEMP", "SD-Income", "SD-Pop"]
sd_eq = pd.DataFrame(zip(columnnames1, regressionsd.coef_.tolist()), columns = ["Feature", "Coefficient"])

sd_eq


# In[32]:


style.use('bmh')
plt.scatter(regressionsf.predict(xsf_test), ysf_test)
plt.show()


# In[33]:


style.use('bmh')
plt.scatter(regressionsd.predict(xsd_test), ysd_test)
plt.show()


# In[34]:


xsf_train = sm.add_constant(xsf_train)
modelsf = sm.OLS(ysf_train, xsf_train)


# In[35]:


resultsf = modelsf.fit()
print(resultsf.summary())


# In[36]:


xsd_train = sm.add_constant(xsd_train)
modelsd = sm.OLS(ysd_train, xsd_train)
resultsd = modelsd.fit()
print(resultsd.summary())


# In[37]:


predicting_cities = pd.read_excel("predictionsjfresno.xlsx")


# In[38]:


predicting_cities


# In[39]:


predicting_sj = predicting_cities.iloc[:, [1,2,3,5]]
predicting_fresno = predicting_cities.iloc[:, [7,8,9,10]]


# In[54]:


homeless_sj = predicting_cities.iloc[:, 4]
homeless_fresno = predicting_cities.iloc[:, 11]


# In[41]:


# using a rent control city (SF) to predict the homelessness in San Jose
predicting_sj = sm.add_constant(predicting_sj)
sj_preds = resultsf.predict(predicting_sj)
plt.figure(dpi = 75)
plt.scatter(homeless_sj, sj_preds)
plt.plot(homeless_sj, homeless_sj, color="red")
plt.ylabel("Predicted # of Homeless Persons Based on Rent Controlled City")
plt.xlabel("Actual # SJ Homeless Persons")
plt.title("Actual vs Predicted Homeless Persons Count")
plt.show()


# In[44]:


predicting_fresno = sm.add_constant(predicting_fresno)
fresno_preds = resultsd.predict(predicting_fresno)
plt.figure(dpi = 75)
plt.scatter(homeless_fresno, fresno_preds)
plt.plot(homeless_fresno, homeless_fresno, color="red")
plt.ylabel("Predicted # of Homeless Persons Based on City Without Rent Control")
plt.xlabel("Actual # Fresno Homeless Persons")
plt.title("Actual vs Predicted Homeless Persons Count")
plt.show()


# In[45]:


# predicting SF test set from SF training set
xsf_test1 = sm.add_constant(xsf_test)
xsf_test1 = resultsd.predict(xsf_test1)
plt.figure(dpi = 75)
plt.scatter(ysf_test, xsf_test1)
plt.plot(ysf_test, ysf_test, color="red")
plt.ylabel("Predicted # of Homeless Persons Based on SD")
plt.xlabel("Actual # SF Homeless Persons")
plt.title("Actual vs Predicted Homeless Persons Count")
plt.show()


# In[46]:


# predicting SD test set from training set

xsd_test1 = sm.add_constant(xsd_test)
xsd_test1 = resultsd.predict(xsd_test1)
plt.figure(dpi = 75)
plt.scatter(ysd_test, xsd_test1)
plt.plot(ysd_test, ysd_test, color="red")
plt.ylabel("Predicted # of Homeless Persons Based on SD")
plt.xlabel("Actual # SF Homeless Persons")
plt.title("Actual vs Predicted Homeless Persons Count")
plt.show()

