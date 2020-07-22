#!/usr/bin/env python
# coding: utf-8

# In[2]:


hash_table = list([i for i in range(10)])
hash_table


# In[4]:


def hash_func(key):
    return key % 5


# In[7]:


data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

print(ord(data1[0]),ord(data2[0]),ord(data3[0]))
print (ord(data1[0]), hash_func(ord(data1[0])))


# In[9]:


def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


# In[10]:


storage_data('Andy', '0105553333')
storage_data('Dave', '0104443333')
storage_data('Trump', '0105556666')


# In[12]:


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


# In[13]:


get_data('Andy')


# In[18]:


hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value
    
def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


# In[19]:


save_data('Dave', '01020203030')
save_data('Andy', '01033332222')
read_data('Dave')


# In[20]:


hash_table


# ## 충돌(Collision) 해결 알고리즘

# In[51]:


hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]
    
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None


# In[52]:


print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)


# In[53]:


save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Dd')


# In[34]:


hash_table


# ## linear probing

# In[ ]:


hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]
        
        
        
        
         
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]
    
def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table(index) == 0:
                
            elif hash_table[index][0] ==
    else:
        return None


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




