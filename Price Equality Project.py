#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copy the first document then run this

import pyperclip
import re
# dollar sign
# numbers
# a fuul stop
# 2 digits after

# regular expresson
amount_ext = re.compile(r'\$\d+[,0-9]*(?:\.\d{2})?')

number = pyperclip.paste() # collect from clipboard
start = amount_ext.findall(number) # search for matches
print(start) # Display


# In[2]:


# Copy the second document then run this

import pyperclip
import re
# dollar sign
# numbers
# a fuul stop
# 2 digits after

# regular expresson
amount_ext = re.compile(r'\$\d+[,0-9]*(?:\.\d{2})?')

number = pyperclip.paste() # collect from clipboard
stop = amount_ext.findall(number) # search for matches
print(stop) # Display


# In[3]:


# Code to compare Stored document contents

def compare(quantity_ext, quantity_ext1):
    print(quantity_ext) # Show list
    print(quantity_ext1) # Show list
    records= [] # Empty list
    for quantity in quantity_ext: # Loop quantity
        if quantity in quantity_ext1: # Check for similarity
            records.append("True") # add to records
            print("Yes " + quantity + " is the same") # print statement
        elif quantity not in quantity_ext1:
            records.append("False") # add to records
    print(records)
    
compare(start, stop)


# In[ ]:




