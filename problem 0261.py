'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Huffman coding is a method of encoding characters based on their frequency. 
Each letter is assigned a variable-length binary string, such as 0101 or 111110, 
where shorter lengths correspond to more common letters. To accomplish this, 
a binary tree is built such that the path from the root to any leaf uniquely maps 
to a character. When traversing the path, descending to a left child corresponds 
to a 0 in the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s

With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, 
and use it to determine a mapping between characters and their encoded binary strings.
'''


class Tree():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
    def __repr__(self):
        node=[self]
        result = '['
        while len(node)!=0:
            node_cur=node[0]
            if node_cur.left:
                node.append(node_cur.left)
            if node_cur.right:
                node.append(node_cur.right)
                
            result+=node_cur.val
            result+=', '
            node=node[1:]
            
        result=result[:-2]
        result+=']'
        return result
    
def find_pos(tree,letter,path=""):
    if tree.val!='*':
        if tree.val!=letter:
            return None
        else:
            return path
        
    val_l=None
    val_r=None
    if tree.left:
        val_l=find_pos(tree.left,letter,path+'0')
    if tree.right:
        val_r=find_pos(tree.right,letter,path+'1')
        
    if val_l!=None:
        return val_l
    if val_r!=None:
        return val_r
    if path=='':
        print('error')
    
a=Tree('*')
b=Tree('*')
c=Tree('*')
d=Tree('*')
e=Tree('a')
f=Tree('t')
g=Tree('*')
h=Tree('c')
i=Tree('s')

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
d.left=h
g.right=i

def encodeur(word,huffman_tree):
    val=""
    for i in word:
        val+=find_pos(huffman_tree,i)
        
    return val

print(encodeur('cats',a))

dict_=dict()
dict_['c']=5
dict_['a']=4
dict_['t']=2
dict_['s']=1

def place_etoile(Huffman):
    if len(Huffman.val)>1:
        Huffman.val='*'
    if Huffman.left:
        place_etoile(Huffman.left)
    if Huffman.right:
        place_etoile(Huffman.right)
        
    return Huffman
        
def create_huffman(dict_):
    List_tree=[]
    while len(dict_)>1:
        letter1=min(dict_,key=dict_.get)
        val=dict_[letter1]
        item=letter1
        del(dict_[letter1])
        letter2=min(dict_,key=dict_.get)
#        del(dict_[letter2])
        dict_[item]=val
        
        new_node=Tree(letter1+letter2)
        compteur=0
        who=None
        for i,j in List_tree:
            if letter1 == i and compteur==0:
                new_node.left=j
                List_tree.remove([i,j])
                compteur=1
                who='1'
            elif letter2 == i and compteur==0:
                new_node.left=j
                List_tree.remove([i,j])
                compteur=1
                who='2'
            elif letter1 == i:
                new_node.right=j
                List_tree.remove([i,j])
            elif letter2== i:
                new_node.right=j
                List_tree.remove([i,j])
                
        if new_node.left==None and new_node.right==None:
            new_node.left=Tree(letter1)
            new_node.right=Tree(letter2)
        elif new_node.right==None:
            if who=='1':
                new_node.right=Tree(letter2)
            elif who=='2':
                new_node.right=Tree(letter1)
                

        dict_[letter1+letter2]=dict_[letter1]+dict_[letter2]
        del(dict_[letter1])
        del(dict_[letter2])
        List_tree.append([letter1+letter2,new_node])

    Huffman=List_tree[0][1]
    place_etoile(Huffman)
    
    return Huffman      
        

aaa=create_huffman(dict_)
print(encodeur('cats',aaa))

