
# coding: utf-8

# In[28]:



def div():
    return 5/0
    
try:
	div()
except ZeroDivisionError:
	print ("division by zero!")
except Exceptionerror:
	print('there is an exception')
finally:
	print('execution done')

