'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Implement the singleton pattern with a twist. 
First, instead of storing one instance, store two instances. 
And in every even call of getInstance(), return the first instance and 
in every odd call of getInstance(), return the second instance.
'''

class Singleton:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
        self.compteur=1
        
    def getInstance(self):
        if self.compteur==1:
            self.compteur=2
            return self.val1
        else:
            self.compteur=1
            return self.val2



