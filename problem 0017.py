'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2
 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. 
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) 
absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is 
"dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''


string_ = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

def longest(string_):
    s=string_.split()
    s_level=[]
    lenn=len(s)
    list_=[]
    list_len_string=[]
#    list_string2=[]
    for i in range(lenn):
        if '.' in s[i]:
            list_.append(s[i])
            
        position=string_.find(s[i])-1
        level=0
#        while position>0 and (string_[position]=='\n' or string_[position]=='\t'):
        while position>0 and string_[position]=='\t':
            level+=1
            position-=1
        s_level.append(level)
        
    nbr=len(list_)
    
    for i in range(nbr):
        indexa=s.index(list_[i])
        current_list=[0]*lenn
        current_level=s_level[indexa]
        current_list[indexa]=1
        current_list_len=''
        while indexa>0:
            indexa-=1
            if s_level[indexa]<current_level:
                current_level=s_level[indexa]
                current_list[indexa]=1
        for j in range(lenn):
            if current_list[j]:
                if current_list_len!='':
                    current_list_len+='/'
                current_list_len=current_list_len+s[j]
        list_len_string.append(current_list_len)
        
    who_longest=0
    val_longest=0
        
    for i in range(0,nbr):
        long=len(list_len_string[i])
        if long>val_longest:
            who_longest=i
            val_longest=long
    
    return list_len_string[who_longest]


print(longest(string_))
        

    
        

        
    
                
            
            
        
        
        

#    for i in range(nbr):
#        len_courante=len(list_[i])
#        position=string_.find(list_[i])
#        list_string.append(string_[:position+len_courante])
        
        
        

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        