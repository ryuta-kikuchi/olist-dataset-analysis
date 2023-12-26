#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


orders_data = pd.read_csv('archive/olist_orders_dataset.csv')

# Basic information about the dataset
basic_info = orders_data.info()

# Descriptive statistics for the dataset
descriptive_stats = orders_data.describe(include='all')

# Counting the frequency of each order status
order_status_counts = orders_data['order_status'].value_counts()

basic_info, descriptive_stats, order_status_counts


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns


# Convert the 'order_purchase_timestamp' to datetime
orders_data['order_purchase_timestamp'] = pd.to_datetime(orders_data['order_purchase_timestamp'])

# Extracting the date from the timestamp
orders_data['order_purchase_date'] = orders_data['order_purchase_timestamp'].dt.date

# Grouping by date and counting the number of orders per day
orders_per_day = orders_data.groupby('order_purchase_date').size()

orders_per_day.describe()

# Setting the aesthetics for the plot
sns.set(style="darkgrid")

# Plotting the number of orders per day
plt.figure(figsize=(15, 6))
plt.plot(orders_per_day.index, orders_per_day.values, color='blue', linewidth=1)
plt.title('Number of Orders', fontsize=15)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()


# In[8]:


order_items_data = pd.read_csv('archive/olist_order_items_dataset.csv')
order_items_data


# In[9]:


products_data = pd.read_csv('archive/olist_products_dataset.csv')
products_data


# In[10]:


order_items_data = order_items_data.join(products_data.set_index('product_id'), how='left', on='product_id')
order_items_data.to_csv("order_items_data.csv")


# In[11]:


order_items_data = order_items_data.join(orders_data.set_index('order_id'), how='left', on='order_id')
order_items_data.to_csv("order_items_data.csv")


# In[12]:


order_items_data.drop(['seller_id', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty'], axis=1)
order_items_data.to_csv('order_items_data_trim.csv')


# In[13]:


data_normalized = order_items_data[['product_length_cm', 'product_height_cm', 'product_width_cm']].copy()
max_dimension = data_normalized.max(axis=1)
max_dimension


# In[14]:


from mpl_toolkits.mplot3d import Axes3D

# Creating a 3D plot for the original dimensions
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(order_items_data['product_width_cm'], order_items_data['product_height_cm'], order_items_data['product_length_cm'], c='blue', marker='o')
ax.set_xlabel('Width (cm)')
ax.set_ylabel('Height (cm)')
ax.set_zlabel('Length (cm)')
ax.set_title('3D Plot of Product Width, Height, and Length')

plt.show()


# In[ ]:




