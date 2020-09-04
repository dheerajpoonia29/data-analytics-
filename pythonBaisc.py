def main():
	# pyPrint()
	# pyDataType()    #TODO: crud on data type - https://www.programiz.com/python-programming/list
	pyIterator()
	# pyFunction()
	# pyClass()
	# pyModule()
	# pyPackage()

# PRINT
def pyPrint():
	a = 10
	print('hi', a, "hello")
	print('hi', a, "hello", sep='#', end='@\n')
	print('hi {} hello'.format(a))
	print('{0} {1} {2}'.format('hi', a, 'hello'))

# DATA TYPE  
def pyDataType():
	def numberDT():
		# Number data type : Python supports integers, floating-point numbers and complex numbers. They are defined as int, float, and complex classes in Python
		a = 5						# a is object of int class where int is data type 
		b = 5.0  				
		c = 5 + 3j 			# c is object of complex class where complex is data type 
		print(a, type(a))			
		print(b, type(b))			# type used to check datatype 
		print(c, type(c))
		print(isinstance(c, complex)) # isinstance map the typeof passed object with class and data typeof passes object map with data type of class 

	def stringDT():
		s = "dheeraj"
		print(s, type(s))

		ss = str(1)
		print(ss, type(ss))

		# ' ' and " " are same 
		sss = ''' hi this 
		is multi line string '''
		print(sss, type(sss))
	
	def listDT():
		print('\nLIST')

		lst1 = ['dheearj', 21]
		lst2 = list('dheeraj')
		print(lst1)
		print(lst2)
		
		#	delete
		d = [4, 5, 6, 7, 8, 9, 8, 8, 7]
		d.pop(3) # remove 4 element which is 7 and return back to user 7
		del d[1] # delete 2 element which is 5 
		d.remove(8) # remove first occurrence of 8
		
	
	def tupleDT():
		print('\nTUPLE')

		tp1 = ('dheeraj', 21)
		tp2 = tuple('dheeraj')
		print(tp1)
		print(tp2)

	def setDT():
		print('\nSET')

		st1 = ('dheeraj', 21)
		st2 = set('dheeraj')
		print(st1)
		print(st2)

	def dictDT():
		print('\nDICTIONARY')

		dct = {}
		print(dct, type(dct))

		# dct1 = {1: "dheeraj", 2: "age"}     # right
		# dct1 = {name: "dheeraj", age: "21"}   # wrong 
		dct1 = {"name":"dheeraj", "age":21}
		dct2 = dict()
		print(dct1)
		print(dct2)
		
# 		if dict1.has_key("age"): in python2
# 		if "age" in dict1: in python 3

	numberDT()
	stringDT()
	listDT()
	tupleDT()
	setDT()  
	dictDT()

def pyIterator():
	l = [1, 2, 3]
	# filer 
	print(list(filter(lambda x: x%2==0, l)))
	# map 
	print(list(map(str, l)))
	# reduce 
	from functools import reduce 
	print(reduce(lambda x,y: x*y, l))

# FUNCTION 
def pyFunction():
	# function definition
	def fun1(x):
		return x*x
	print(fun1(5)) 

	# anonymous or lambda 
	fun2 = lambda x: x*x 
	print(fun2(5))

	lst = [1, 5, 4, 6, 8, 11, 3, 12]
	# filter even no from list or remve odd no 
	# method1 = [x for x in lst: if x%2==0]
	method1 = [x for x in lst if x%2==0]
	print(method1)

	def myFun(x):
		if x%2==0:
			return x
	method2 = list(filter(myFun, lst))
	print(method2)

	method3 = list(filter(lambda x: x%2==0, lst))
	print(method3)

	# method4 = list(map(lambda x: x%2==0, lst))      # to know filter vs map uncomment this 
	method4 = list(map(lambda x: x*x, lst)) 					# filter reduce in list, but map operation or process on list
	print(method4)

# CLASS
def pyClass():
    #attricute are 2 type class attribute and instance attribute 
		collage = 'piet jaipur'							# class attribute

		class Student:
			def __init__(self):
				self.__name = "dheeraj"						# instance private attribute
				self.collage = "piet"
		
			def getData(self):										# class method 
				return 'hi you are in pyClass data: '
			
			def printData(self):									# instance method
				return self.getData()+self.__name+' '+self.collage

			def setter(self, newName):
				self.__name = newName
		
		obj = Student()
		# obj._name = 'neeraj'		# single underscore name should change 
		# obj.__name = 'neeraj'	  # now it is pure private 
		# obj.setter('neeraj')		# now _ _ private attribut change via method 
		print(obj.printData())

# MODULE 
def pyModule():
	# Modules refer to a file containing Python statements and definitions.
	# A file containing Python code, is called module 
	# for example: pythonBasic.py, is called a module, and its module name would be pythonBasic 
	# We use modules to break down large programs into small manageable and organized files
	# modules provide reusability of code.
	# We can define our most used functions in a module and import it, instead of copying their definitions into different programs
	import mathModule;
	print(mathModule.add(10, 20))

	from mathModule import add;
	print(add(10, 20))

	from mathModule import add as a;
	print(a(10, 20))

	# from math import *;   import all method of module 
	print(dir(mathModule))
	print(help(mathModule))
	print('name of module: ',mathModule.__name__)     # __name__ is special attribute which contain the name of module 

# PACKAGE 
def pyPackage():
	# We don't usually store all of our files on our computer in the same location. We use a well-organized hierarchy of directories for easier access
	# As our application program grows larger in size with a lot of modules, we place similar modules in one package and different modules in different packages
	# Similarly, as a directory can contain subdirectories and files, a Python package can have sub-packages and modules
	# ! A directory must contain a file named __init__.py in order for Python to consider it as a package
	# this director contain multiple file in which must on with __init__.py and other rest all are module 
	# TODO:
	pass

main()
