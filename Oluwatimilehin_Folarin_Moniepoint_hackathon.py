#!/usr/bin/env python
# coding: utf-8

# ## Author: Oluwatimilehin Folarin
# 
# ### Moniepoint hackathon
# 
# ### Date: 22-02-2025
# 
# ### Intended Programming Language of Choice: Python
# 
# ### Steps: First, I would be building the model using Jupyter Notebook, convert to Python file, and then deploy using FastAPI
# 
# Run the API file on command prompt using: uvicorn moniepoint_api:app --reload. 
# Afterwards, use this link to open the API on your web browser: http://127.0.0.1:8000/docs
# 
# ### Task: To build analytics software that reads through transactions’ files and reports the following metrics:
# 
# <li> Highest sales volume in a day
# 
# <li> Highest sales value in a day
# 
# <li> Most sold product ID by volume
# 
# <li> Highest sales staff ID for each month.
# 
# <li> Highest hour of the day by average transaction volume '''
#     
#     
#     
#  
#     
# 

# In[1]:


#Importing required libraries

import pandas as pd
import re
import os
import csv
from collections import defaultdict
from datetime import datetime


# In[2]:


def trans_files_processing(directory):
    daily_sales_volume = defaultdict(int)
    daily_sales_value = defaultdict(float)
    product_sales = defaultdict(int)
    staff_sales = defaultdict(int)
    hourly_transaction_volume = defaultdict(list)
    
    for f in os.listdir(directory):
        if f.endswith(".txt"):
            with open(os.path.join(directory, f), 'r') as file:
                for l in file:
                    p = l.strip().split(',')
                    if len(p)< 4:
                        continue
                        
                    staff_id = p[0]
                    time = p[1]
                    products_sold = p[2]
                    sales_amount= p[3]
                    
                    d = datetime.fromisoformat(time)
                    d_string = d.date().isoformat()
                    d_in_hour = d.hour
                    
                    daily_sales_volume[d_string]+=1
                    sales_amount = float(sales_amount)
                    daily_sales_value[d_string]+=sales_amount
                    staff_sales[staff_id] += sales_amount
                    hourly_transaction_volume[d_in_hour].append(sales_amount)
                    
                    matching_products = re.findall(r'\[(\d+):(\d+)\]', products_sold)
                    for product_id, quantity in matching_products:
                        product_sales[product_id]+=int(quantity)
                                                   
                                                   
    #Asigning variables for all the outcomes expected
    highest_daily_sales_volume = max(daily_sales_volume, key=daily_sales_volume.get)
    highest_daily_sales_value = max(daily_sales_value, key= daily_sales_value.get)
    Most_sold_productid_volume = max(product_sales, key=product_sales.get)
    Highest_monthly_sales_staff_id = max(staff_sales, key=staff_sales.get) 
    highest_daily_hour_transaction_volume = max(hourly_transaction_volume, key=lambda h: sum(hourly_transaction_volume[h])/len(hourly_transaction_volume[h]))           
                    
    return {
        "Highest sales volume in a day": highest_daily_sales_volume, 
    
        "Highest sales value in a day":highest_daily_sales_value,

        "Most sold product ID by volume":Most_sold_productid_volume,

        "Highest sales staff ID for each month":Highest_monthly_sales_staff_id,

        "Highest hour of the day by average transaction volume":highest_daily_hour_transaction_volume
    }                
            
    


# In[3]:


#The file directory for each test cases
dir_path_1 = r"C:\Users\Oluwatimilehin F\Downloads\Moniepoint\test-case-1"
dir_path_2 = r"C:\Users\Oluwatimilehin F\Downloads\Moniepoint\test-case-2"
dir_path_3= r"C:\Users\Oluwatimilehin F\Downloads\Moniepoint\test-case-3"
dir_path_4 = r"C:\Users\Oluwatimilehin F\Downloads\Moniepoint\test-case-4"
dir_path_5 = r"C:\Users\Oluwatimilehin F\Downloads\Moniepoint\test-case-5"

#The outcomes for each test cases
result_1 = trans_files_processing(dir_path_1)
result_2 = trans_files_processing(dir_path_2)
result_3 = trans_files_processing(dir_path_3)
result_4 = trans_files_processing(dir_path_4)
result_5 = trans_files_processing(dir_path_5)

#Saving the outcomes in a dictionary 
dic = {"Test case 1": result_1, "Test case 2": result_2, "Test case 3": result_3, "Test case 4": result_4, "Test case 5": result_5}

#Converting the dictionary to pandas DataFrame
df = pd.DataFrame(dic)

#Display final outcome
print(df)


# In[ ]:




