#!/usr/bin/env python
# coding: utf-8

# In[1]:


grade = 85 

if grade >= 60:
    print('passed')


# In[2]:


if 1:
    print('Nonzeri vakyes are true, so this will print')


# In[3]:


if 0:
    print('zero value is false, so this will not print')


# In[4]:


if """""":
    print('zero value is false, so this will not print')


# In[7]:


grade = 55 

if grade >= 60:
    print('passed')


# In[8]:


grade = 85

if grade >= 60:
    print('passed')
else:
    print('failed')


# In[9]:


grade = 57

if grade >= 60:
    print('passed')
else:
    print('failed')


# In[10]:


grade = 87
if grade >= 60:
    result = 'passed'
else:
    result = 'failed'
print(result)


# In[11]:


result = ('passed' if grade >= 60 else 'failed')
result


# In[12]:


grade = 49

if grade >= 60:
    print('passed')
else:
    print('failed')
    print('you must take the course again')


# In[13]:


grade = 77

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')


# In[14]:


product = 3

while product <= 50:
    product = product * 3

product


# In[15]:


product = 7

while product <= 1000:
    product = product * 7
    
product


# In[16]:


for character in 'Programming':
    print(character, end=' ')


# In[20]:


print(10, 20, 30, sep=',')


# In[21]:


total = 0

for number in [2, -3, 0, 17, 9]:
    total = total + number 

total


# In[26]:


for counter in range(10):
    print(counter, end=' ')


# In[28]:


total = 0 

for number in range(1000001):
    total = total + number
    
total


# In[30]:


total = 0

for number in [1, 2, 3, 4, 5]:
    total += number

total


# In[31]:


x = 12

x **= 2
x


# In[33]:


total = 0 # sum of grades
grade_counter = 0 
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94] # list of 10 grades

for grade in grades:
    total += grade # add current grdae to the running total
    grade_counter += 1 # indicates that one more grade was processed
    
average = total / grade_counter
print(f'Class average is {average}')


# In[34]:


number1 = 7
number2 = 5

print(f'{number1} times {number2} is {number1 * number2}')


# In[35]:


total = 0 # sum of grades
grade_counter = 0 # number of grades entered

grade = int(input('Enter grade, -1 to end: ')) # get one grade

while grade != -1: 
    total += grade
    grade_counter += 1
    grade = int(input('Enter grade, -1 to end: '))
    
if grade_counter != 0:
    average = total / grade_counter
    print(f'Class grade average is {average:.2f}')
else:
    print('No grades entered')


# In[40]:


for count in range(2):
    value = int(input('Enter value'))
    if value % 2 == 0:
        print(f'{value} is even')
    else:
        print(f'{value} is odd')


# In[ ]:


for number in range(5, 10):
    print(number, end=' ')


# In[45]:


for number in range(0, 10, 2):
    print(number, end=' ')


# In[47]:


for number in range(10, 0, -2):
    print(number, end=' ')


# In[50]:


for number in range(99, -1, -11):
    print(number, end=' ')


# In[53]:


total = 0

for number in range(2, 101, 2):
    total += number

total


# In[57]:


principal = 1000
rate = .02


for year in range (1, 11):
    amount = principal * (1 + rate) ** year
    print(f'{year:>2}{amount:>10.2f}')


# In[61]:


for number in range(100):
    if number == 10:
        break
    print(number, end=' ')


# In[64]:


gender = 'Female'
age = 70

if gender == 'Female' and age >= 65:
    print('senior female')


# In[65]:


semester_average = 83

final_exam = 95

if semester_average >= 90 or final_exam >= 90:
    print('Student gets an A')


# In[66]:


grade = 87

if not grade == -1:
    print('next grade is', grade)


# In[67]:


if grade != -1:
    print('next grade is', grade)


# In[71]:


i = 1
j = 2
k = 3
m = 2


# In[72]:


(i >= 1) and (j < 4)


# In[73]:


(m <= 99) and (k < m)


# In[74]:


(j >= i) or (k == m)


# In[75]:


(k + m < j) or (3 - j >= k)


# In[76]:


not (k > m)


# In[77]:


grades = [85, 93, 45, 89, 85]
sum(grades) / len(grades)


# In[78]:


import statistics


# In[79]:


statistics.mean(grades)


# In[80]:


statistics.median(grades)


# In[81]:


statistics.mode(grades)


# In[82]:


sorted(grades)


# In[83]:


values = [47, 95, 88, 73, 88, 84]


# In[84]:


statistics.mean(values)


# In[85]:


statistics.median(values)


# In[86]:


statistics.mode(values)


# In[ ]:




