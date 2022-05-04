#!/usr/bin/env python
# coding: utf-8

# In[28]:


def count_ways(stair, step):
     
    temp = 0
    result = [1]
     
    for i in range(1, stair + 1):
        j = i - 1
        s = (i - step)- 1
        
        if (s >= 0):
            temp -= result[s]
            
        temp += result[j]
        result.append(temp)
         
    return result[stair]
 

stairs = int(input())

 
print(count_ways(stairs, 2))

