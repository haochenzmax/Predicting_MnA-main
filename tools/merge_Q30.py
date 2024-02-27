#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load each of the CSV files to examine their structure.
q16_df = pd.read_csv('data/entities/Q16.csv')
q30_1_df = pd.read_csv('data/entities_US/Q30_1.csv')
q30_2_df = pd.read_csv('data/entities_US/Q30_2.csv')
q30_3_df = pd.read_csv('data/entities_US/Q30_3.csv')


# In[3]:


business_label_key = 'businessLabel.value'
merged_q30_df = q30_1_df.merge(q30_2_df, on=business_label_key, how='outer')
merged_q30_df = merged_q30_df.merge(q30_3_df, on=business_label_key, how='outer')


# In[6]:


# Compare the columns of the merged Q30 dataframe with those of Q16
q16_columns = set(q16_df.columns)
merged_q30_columns = set(merged_q30_df.columns)

# Find the common columns and the columns that are unique to each dataframe
common_columns = q16_columns.intersection(merged_q30_columns)
unique_to_q16 = q16_columns.difference(merged_q30_columns)
unique_to_merged_q30 = merged_q30_columns.difference(q16_columns)


merged_q30_df_filtered = merged_q30_df.drop(columns=list(unique_to_merged_q30))

# Rename columns to match q16 column names if needed
# For this demonstration, we'll assume the columns match and do not need renaming
# In practice, you would check and rename as necessary

# Reorder columns to match the order in q16
merged_q30_df_final = merged_q30_df_filtered.reindex(columns=q16_df.columns)


# In[7]:


merged_q30_final_csv_path = 'data/entities/Q30.csv'
merged_q30_df_final.to_csv(merged_q30_final_csv_path, index=False)

