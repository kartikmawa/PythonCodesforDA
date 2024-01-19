#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[ ]:


#BMI =(weight in pound *703)/(height in inches *height in inches)


# In[12]:


Name=input("Enter your name: ")
Weight=input("Enter your weight in pounds: ")
Height=input("Enter your height in inches: ")
BMI =(int(Weight)*703)/(int(Height)*int(Height))
print('Your BMI is: ',BMI)


# In[21]:


if BMI>0:
    if(BMI<18.5):
        print(Name, 'you are underweight')
    elif(BMI<=24.9):
        print(Name, 'you are normal weight')
    elif(BMI<=29.9):
        print(Name, 'you are overweight')
    elif(BMI<=34.9):
        print(Name, 'you are obese')
    elif(BMI<=39.9):
        print(Name, 'you are severely obese')
    else:
        print(Name, 'Morbidly obese')
else:
    print('Enter Valid data')


# In[ ]:





# In[ ]:





# In[ ]:


Under 18.5	Underweight	Minimal
18.5 - 24.9	Normal Weight	Minimal
25 - 29.9	Overweight	Increased
30 - 34.9	Obese	High
35 - 39.9	Severely Obese	Very High
40 and over	Morbidly Obese	Extremely High


# In[ ]:





# In[ ]:





# In[ ]:


print(weight)


# In[ ]:





# In[ ]:





# In[ ]:




