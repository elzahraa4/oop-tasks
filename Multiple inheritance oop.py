#!/usr/bin/env python
# coding: utf-8

# In[1]:


#case 1: execute the method of class4 just create an object and call the method


class Class1:
    
    def m(self):
        print("Class1")

        
class Class2(Class1):
    
    def m(self):
        print("Class2")
        
        
class Class3(Class1):
    
    def m(self):
        print("Class3")
        
        
class Class4(Class2, Class3):
    
    def m(self):
        print("Class4")

        
o = Class4()
o.m()


# In[2]:


# case 2: when method is overriden in one of 2 inherited classes, it skip overriden one and print next parameter

class Class1:
	def m(self):
		print("In Class1")
	
class Class2(Class1):
	pass

class Class3(Class1):
	def m(self):
		print("In Class3")
	
class Class4(Class2, Class3):
	pass	

obj = Class4()
obj.m()


# In[3]:


# case 3 : when method is overridden in both classes, it skip inherited class and print  first parameter

class Class1:
	def m(self):
		print("In Class1")
	
class Class2(Class1):
	def m(self):
		print("In Class2")

class Class3(Class1):
	def m(self):
		print("In Class3")
		
class Class4(Class2, Class3):
	pass
	
obj = Class4()
obj.m()


# In[ ]:


# case 4 : when every class defines the same method, you can use each class name to call its method

class Class1:
	def m(self):
		print("In Class1")
	
class Class2(Class1):
	def m(self):
		print("In Class2")

class Class3(Class1):
	def m(self):
		print("In Class3")	
	
class Class4(Class2, Class3):
	def m(self):
		print("In Class4")

obj = Class4()
obj.m()

Class2.m(obj)
Class3.m(obj)
Class1.m(obj)


# In[4]:


#case 5: to call all methods by call the method of last inherited class (class4)

class Class1:
    def m(self):
        print("In Class1") 
      
class Class2(Class1):
    def m(self):
        print("In Class2")
 
class Class3(Class1):
    def m(self):
        print("In Class3")    
     
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")  
        Class2.m(self)
        Class3.m(self)
        Class1.m(self)
 
obj = Class4()
obj.m()


# In[ ]:





# In[ ]:




