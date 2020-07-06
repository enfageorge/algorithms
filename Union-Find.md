

```python
import numpy as np
```

## The Eager Method


```python
class DynamicConnect():
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
```


```python
obj = DynamicConnect(5)
```


```python
obj.returnMatrix()
```




    array([0, 1, 2, 3, 4])




```python
obj.union(2,1)
```


```python
obj.union(1,4)
```


```python
obj.returnMatrix()
```




    array([0, 2, 2, 3, 2])




```python
obj.find(1,2)
```




    True




```python
obj.find(1,3)
```




    False


