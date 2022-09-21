#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random

# In[8]:


n=str(input("enter the integers"))
i=len(n)
k=i-1
while k>=0:
    print(n[k],end='')
    k=k-1


# In[11]:


setOfIntegers=[]
n=int(input("enter the number of integers you want to enter"))
i=0
while n-1>=i:
    integer=int(input())
    setOfIntegers.append(integer)
    i=i+1
k=0
sumEven=0
sumOdd=0
while n-1>=k:
    if setOfIntegers[k]%2==0:
        sumEven=sumEven+setOfIntegers[k]
    else:
        sumOdd=sumOdd+setOfIntegers[k]
    k=k+1
print("The sum of even numbers is :",sumEven)
print("The sum of odd numbers is :",sumOdd)




# In[13]:


i=0
k=1
sum=0
l=1
while l<=10:
    sum=i+k
    print(sum,end=' ')
    i=k
    k=sum
    l=l+1



# In[16]:


n=int(input("Enter a number"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print("The factorial of the number is",fact)


# In[21]:


marks=int(input("Enter your marks"))
if marks<50:
    print("YOUR GRADE IS F")
if marks>50 and marks<60:
    print("YOUR GRADE IS E")
if marks>61 and marks<70:
    print("YOUR GRADE IS D")
if marks>71 and marks<80:
    print("YOUR GRADE IS C")
if marks>81 and marks<90:
    print("YOUR GRADE IS B")
if marks>91 and marks<=100:
    print("YOUR GRADE IS A")


# In[ ]:





# In[ ]:




