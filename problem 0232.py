'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

    insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
    sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
'''


class PrefixMapSum():
    def __init__(self):
        self.List_key=dict()
        
        
    def insert(self,key,value):
        if key in self.List_key:
            self.List_key[key]=value
        else:
            self.List_key[key]=value
        
        
    def sum_(self,prefix):
        result=0
        for i in self.List_key:
            if prefix in i:
                result+=self.List_key[i]
                
        return result
    
    
    
a=PrefixMapSum()

a.insert("columnar",3)

print(a.sum_("col"))
a.insert("column",2)

print(a.sum_("col"))
