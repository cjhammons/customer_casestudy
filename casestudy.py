# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('data/casestudy.csv')
df.head()

# %% [markdown]
# # Total Revenue for current year (2017)

# %%
revenue_2017 = df[df['year'] == 2017]['net_revenue'].sum()
print('Total revenue for 2017:', revenue_2017)

# %% [markdown]
# # New Customer Revenue
# 
# Revenue from customers who joined in 2017.

# %%
# create 2 new dataframes for current year and previous year
df_2017 = df[df['year'] == 2017]
df_2016 = df[df['year'] == 2016]

# Take the difference between the two dataframes by concating and dropping duplicates
new_customers = pd.concat([df_2017, df_2016], axis=0).drop_duplicates(keep=False)
# sum the revenue for new customers
new_customer_revenue = new_customers['net_revenue'].sum()

print('Revenue from new customers in 2017:', new_customer_revenue)

# %% [markdown]
# # Existing Customer Growth
# 
# Difference in revenue for all customers in the current year and previous year.

# %%
growth = df_2017['net_revenue'].sum() - df_2016['net_revenue'].sum()
print('Growth in revenue:', growth)

# %% [markdown]
# # Revenue lost from attrition

# %%
churn_df = df_2016[~df_2016['customer_email'].isin(df_2017['customer_email'])]
print('Revenue lost from attrition:', churn_df['net_revenue'].sum())

# %% [markdown]
# # Existing customer revenue Current year (2017)

# %%
revenue_2017 = df_2017['net_revenue'].sum()
print('Total revenue for 2017:', revenue_2017)

# %% [markdown]
# # Existing Customer Revenue prior year (2016)

# %%
revenue_2016 = df_2016['net_revenue'].sum()
print('Total revenue for 2016:', revenue_2016)

# %% [markdown]
# # Total Customers current year (2017)

# %%
customers_2017 = df_2017['customer_email'].nunique()
print('Number of customers in 2017:', customers_2017)

# %% [markdown]
# # Total Customers Prior year (2016)

# %%
customers_2016 = df_2016['customer_email'].nunique()
print('Number of customers in 2016:', customers_2016)

# %% [markdown]
# # New Customers

# %%
new_customers_df = pd.concat([df_2017, df_2016], axis=0).drop_duplicates(keep=False)
new_customers = new_customers['customer_email'].nunique()
print('Number of new customers:', new_customers)

# %% [markdown]
# # Lost Customers

# %%
churn_df = df_2016[~df_2016['customer_email'].isin(df_2017['customer_email'])]
churn_df['customer_email'].nunique()

print('Lost Customers:', churn_df['customer_email'].nunique())

# %% [markdown]
# # Visualizations
# 
# ## Revenue by year

# %%
sns.set_theme(style='whitegrid')

# create new dataframe with revenue by year
df_revenue = df.groupby('year')['net_revenue'].sum().reset_index()

# plot
f, ax = plt.subplots(figsize=(15, 10))
sns.barplot(data = df_revenue, x='year', y='net_revenue')
plt.xlabel('Year')
plt.ylabel('Revenue (Millions)')
plt.title('Revenue by Year')
plt.show()

# %% [markdown]
# ## Customer change by year

# %%
df_customers = df.groupby('year')['customer_email'].nunique().reset_index()

f, ax = plt.subplots(figsize=(15, 10))
sns.barplot(data = df_customers, x='year', y='customer_email')
plt.xlabel('Year')
plt.ylabel('Number of Customers')
plt.title('Number of Customers by Year')
plt.show()

# %% [markdown]
# 


