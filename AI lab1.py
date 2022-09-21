#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Activity 1
n=input("enter a number")
if int(n)%2==0:
      print("the give num is an even")
else:
      print("the give num ia an odd num")

#Activity2
sum=0
s=input("enter an integer")
n=int(s)
while n!=0:
      sum=sum+n
      s=input("enter an integer value")
      n=int(s)
print("sum of given value is",sum)


#Activity3
isPrime=True
i=2
n=int(input("enter num"))
while i<n:
      remainder=n%i
      if remainder==0:
            isPrime=False
            break
      else:
            i=i+1
            
if isPrime:
      print("num is prime")
else:
      print("num is not prime")



#Activity4
summ =0
i=0
while i<=4:
      s=input("enter num")
      n=int(s)
      summ=summ+n
      i=i+1
print("sum is",summ)



#Activity5
summation = 0
i=1
while i<=10:
      summation=summation+1
      i=i+1
print("sum is",summation)

#Activity6
name =input('What is your name?')
print('hello' + name )


job =input('What is your job?')
print('your job is' + job )

num =input('give me a number?')
print('you said:' + str(num))

# In[ ]:

enter a number22
the give num is an even
enter an integer1
enter an integer value2
enter an integer value3
enter an integer value4
enter an integer value7
enter an integer value0
sum of given value is 17
enter num22
num is not prime
enter num23
enter num54
enter num67
enter num12
enter num333
sum is 489
sum is 10
What is your name?m masoood anwar
hellom masoood anwar
What is your job?student
your job isstudent
give me a number?19
you said:19




