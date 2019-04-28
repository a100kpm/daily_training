'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass

'''

class Stack:
    def __init__(self):
        self.list = []
        
    def pop(self, stack_number):
        lenn=len(self.list)
        
        for i in range(stack_number,lenn-1):
            self.list[i]=self.list[i+1]
            
        self.list=self.list[:-1]
    
    def push(self, item, stack_number):
        lenn=len(self.list)
        
           
        if stack_number==lenn:
            self.list.append(item)
        elif stack_number<lenn:
            var = self.list[stack_number]
            self.list[stack_number]=item
            for i in range(stack_number+1,lenn):
                var2=self.list[i]
                self.list[i]=var
                var = var2
            self.list.append(var)
        else:
            print("cann't push this")
            
        print(self.list)
