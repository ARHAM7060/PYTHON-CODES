#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''Write a function that takes a list of numbers as input and returns
a new list containing only the even numbers from the input list.
Use list comprehension to solve this problem.'''

a=int(input('enter the number of elements to be in the list : '))
temp=0
list=[]
new_list=[]

for i in range(a):
    temp=input()
    list.append(int(temp))
print(f'list is : {list}')

new_list=  [i for i in list if i%2==0 and i!=0] 
print(f'list containing odd elements of the input list : {new_list}')


# In[ ]:




