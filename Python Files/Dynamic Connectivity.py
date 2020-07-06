#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ## The Eager Method - Union Find

# We start off by creating an array of N elements where N is your number of nodes. We intialise these array with it's index values. The values in the array can be taken as value of the tree number. So intially everyone is their own unique tree.
# 
# To do the union or merge operation between two nodes, we take the first nodes label and replace all places where the second node label appears with this value. 
# 
# To check if two nodes are connected, we check if the values in the array indexs match.
# 
# The operation is too slow. The union operation is too expensive. You have a worst case time complexity of n2

# In[2]:


class DynamicConnectEager():
    def __init__(self,NumberOfElements):
        self.connectivityMatrix = np.array(range(NumberOfElements)) #You could use arrays too.But for very large numbers, 
                                                                    #the numpy operations would be faster
        
    def union(self,firstNode,secondNode):
        firstNodeLabel = self.returnLabel(firstNode)
        secondNodeLabel = self.returnLabel(secondNode)
        
        self.connectivityMatrix[self.connectivityMatrix==secondNodeLabel] = firstNodeLabel   
        
    def find(self,firstNode,secondNode):
        if (self.returnLabel(firstNode) == self.returnLabel(secondNode)):
            return True
        return False
        
    def returnMatrix(self):
        return self.connectivityMatrix
    
    def returnLabel(self,node):
        return self.connectivityMatrix[node]


# In[3]:


eagerObj = DynamicConnectEager(5)


# In[4]:


print(eagerObj.returnMatrix())


# In[5]:


eagerObj.union(2,1)
eagerObj.union(1,4)


# In[6]:


print(eagerObj.returnMatrix())


# In[7]:


print(eagerObj.find(1,2))


# In[8]:


print(eagerObj.find(1,3))


# ## The Lazy Method - Quick Union 

# We start off by creating an array of N elements where N is your number of nodes. We intialise these array with it's index values. The values in the array can be taken as value of the root of the node.
# 
# To do the union or merge operation between two nodes, we find the root of the child node and set that to the parent.
# 
# To check for connectivity, simply check if the root of nodes are equal.
# 
# This algorithm performs better than Eager with a time complexity of n.

# In[9]:


class DynamicConnectLazy():
    def __init__(self,NumberOfElements):
        self.connectivityMatrix = np.array(range(NumberOfElements)) #You could use arrays too.But for very large numbers, 
                                                                    #the numpy operations would be faster
        
    def union(self,child,parent):
        childRoot = self.findroot(child)
        self.connectivityMatrix[childRoot] = parent 
        
    def findroot(self,node):
        while ( node != self.connectivityMatrix[node]):
            node = self.connectivityMatrix[node]
        return node
    
    def checkConnect(self,firstNode,secondNode):
        firstNodeRoot = self.findroot(firstNode)
        secondNodeRoot = self.findroot(secondNode)
        if firstNodeRoot == secondNodeRoot:
            return True
        return False
        
    def returnMatrix(self):
        return self.connectivityMatrix


# In[10]:


lazyObj = DynamicConnectLazy(10)


# In[11]:


lazyObj.union(3,4)
lazyObj.union(3,8)
lazyObj.union(6,5)
lazyObj.union(9,4)


# In[12]:


print(lazyObj.checkConnect(3,9))


# In[13]:


print(lazyObj.checkConnect(0,9))

