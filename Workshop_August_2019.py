#Commenting for single 


'''
Commenting for multiple lines
'''


#How to declare variables in Python
my_age = 40 


#One variable can hold different data type
# Integer
my_var = 8
type(my_var)

# Float
my_var = 26.5
type(my_var)
  
# String
my_var = "FORSK"
type(my_var)
  
# Boolean
my_var = True
type(my_var)
  
# NoneType
my_var = None
type(my_var)



"""
Type Conversion using Global Functions  
  int()
  float()
  str()
  bool()
"""


#How to convert the data type
int (10.6)
int ("10")


float (4)
float ("10")


str (4)
str (10.6)


bool (4)        # Any integer greater than zero is True
bool (0)

bool (10.6)     # Any float greater than 0.0 is True
bool(0.0)

bool(-90)


bool ("10")
bool("")

bool (None)


#Taking Integer Input from user
age = input ( "Enter your Age > ")
print (age)
print (type(age))
  
age = int(age)
print (age)
print (type(age))


#Taking Floating Point Input from user 
temperature  = input ( "Enter your temperature of your city > ")
print (temperature)
print (type(temperature))

  
temperature = float(temperature)
print (temperature)
print (type(temperature))


#Taking String Input from user using raw_input function 
name = input ( "Enter your Name >")
print (name)
print (type(name))


#Printing Output to the screen using single quote
print ( 'FORSK TECHNOLOGIES' )

#Printing Output to the screen using double quote
print ( "FORSK TECHNOLOGIES" )

#Using Triple Quotes to print quotation marks in string
print ("""FORSK"S TECHNOLOGIES""")


# Importing Modules
 
import math

math.sqrt ( 16 )
math.log ( 16, 2 )  
math.cos ( 0 )
math.isnan(90)

# Importing Names from a Module Directly
#How to use specific functions from packages or modules in python 
from math import sqrt
sqrt ( 16 )


#How to use specific functions from packages or modules
#and also aliasing
from math import sqrt as square 
square ( 16 )

# How to find the function within the Module/Package
dir ( math )

help (math.sqrt)


 
#Slicing of strings

newstr = "Monty Python"

# Indexing using Left to Right

#START
print(newstr [ 0 ]) # 1st thing (0-indexed)
print(newstr [ -12 ])

# Indexing using Right to Left
print (newstr [ -1 ] ) # Last thing

 
#START and END
print(newstr[:3])  # First three things
print(newstr[-3:]) # Last three things

print(newstr[3:])  # Everything *except* the first three
print(newstr[:-3]) # Everything *except* the last three\


newstr [ 6:10 ]
 
newstr [ : 5 ]
newstr [ 6 : ]
newstr [ : ]
   

#Strings in python are Immutable 

newstr = "Monty Python"

newstr [ 0 ] = "m"
#or 
del newstr [ 0 ]
  
del newstr


"""
Global Inbuilt function ( len and del )
"""

newstr = "Monty Python"

len ( newstr )
print ( newstr )
del ( newstr )



# String functions 
# ( lower, upper, find, replace, strip, lstrip, rstrip, split, join) 
# creates a new copy of the string 

newstr = "    Monty Python    "
print(newstr)

newstr.lower()
print(newstr)

newstr2= newstr.lower()
print(newstr2)

newstr.upper()
   
newstr.find('r')
newstr.find('P')
newstr.replace(' ','\n')
 
newstr.lstrip()
newstr.rstrip()
newstr.strip()
  
newstr.split()
newstr.index('M')

string="Rajasthan"
" ".join( string )


#to list all the functions for an object  
dir ( str )

#to check the syntax for a specific function of the object 
help ( str.strip )


#Take the age as input from the user and print  
age = int(input("Enter your age>"))


#Take the age as input from the user and print  
age = int(input("Enter your age>"))
if ( age > 0 ):
  print ("Valid Age")
  
else:
  print ("Invalid Age")
  


"""
Looping technique using while 
""" 

n = 0
while (n < 10):
  print (n)
  n = n + 1
  #n += 1


"""
List
"""

#List Creation
my_list = [ 1, 2, 3 ]
print(my_list)

#Adding single items in the list in the last 
my_list.append( 5 ) 
print(my_list)
 
#Adding single item in the list at a specific position in the list
my_list.insert ( 0, 0 )
print(my_list)


#Remove a specific item by its value from the list 
my_list.remove ( 4 )   #( ValueError here since 4 is not in the list )


# Accessing the values of the list using index
print(my_list[0])

    
#Sorting of the list items  
print(my_list)
my_list.sort()
print (my_list)


    
# Membership Operators 
# in   ,  not in 

# Used to check if some single item is in a larger collection  
# Return True if the item is in list
# Return False if the item is not in list  

# Example
some_list = [1,2,3,5,6,2,4,3,5,6,7,8,1,2,3]

3 in some_list  # will return True

3 not in some_list # will return False

7 not in some_list  # will return True


# Hand on Challenge
while (3 in some_list):
    some_list.remove(3)
print (some_list)
    
  


"""
Looping technique using for each
"""
my_list = [0,1,2,3,4,5,6]
for number in my_list:
  print (number)
  
  

# default the range starts from 0

our_list = list(range(13))
print (type(our_list))
print (our_list)

for number in list(range (13)):
  print (number)


for number in list(range (1,13)):
  print (number)


"""
dictionary
"""

phone_book = { 'Vidhan':8504982228, 'Aayushi':8905336615, 'Vibhooti':9414701291 }
print(phone_book)
print(type(phone_book))


# Creation of dictionaries
dict1 = {'fname':'John', 'lname':'Mille', 'profession':'plumber',  'age':'32'}
print(dict1)


# Add/Update
dict1['lname'] = 'Miller'
dict1['profession'] = 'electrician'
dict1['age'] = '36'
dict1['city'] = 'NY' #add
print(dict1)

dict1['city'] = 'MA' #update
print(dict1)

dict1.update ( {'age':32, 'city':'NY' } )
print(dict1)

# Printing Values
print (dict1["lname"])
print (dict1.get('lname'))
print (dict1.get('name'))
print (dict1.get('name', 'Not Found'))



dict1 = {'fname':'John', 'lname':'Miller', 'profession':'plumber',  'age':'32'}


# To list all the keys
a  = dict1.keys()
print(a)
print(type(a)) 

# To list all the values  
print(dict1.values())

# To list all the values  
print(dict1.items())
 
# To list all values and keys  
for key in dict1:
  print ( key , dict1[key] )

for key in dict1:
  print ( key , dict1.get(key) )



"""
NumPy
"""

a = [0,1,2,3,4,5,6,7,8]
print (type(a))
print (a)  
# it always prints the values with comma seperated , thats list


# Convert your list data to NumPy arrays
import numpy as np

x = np.array( a ) 
print (type(x))

print (x)
# it always prints the values WITHOUT comma seperated , thats ndarray


# to print the data type of the elements of array 
print (x.dtype)


# to print the dimension of the array 
print (x.ndim)

# to print the shape of the array 
# returns a tuple listing the length of the array along each dimension
# For a 1D array, the shape would be (n,) 
# where n is the number of elements in your array.
print (x.shape)


# Array Indexing will always return the data type object 
print (x[0])
print (x[2])
print (x[-1])



"""
Series
"""


#Import Python Libraries

import pandas as pd

# Create an Empty Series
s = pd.Series()
print (type(s))
print (s)


# Create a Series from ndarray
import numpy as np
data = np.array(['a','b','c','d'])
print (type(data ))

s = pd.Series(data)
print (type(s))
print (s)
# We did not pass any index, so by default, 
# it assigned the indexes ranging from 0 to len(data)-1, i.e., 0 to 3.

#retrieve the first element
print (s[0])

#retrieve the first three element
print (s[:3])


#retrieve the last three element
print (s[-3:])


# Customised Index value
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)


"""
DataFrame
"""

# A Data frame is a two-dimensional data structure, i.e., 
# data is aligned in a tabular fashion in rows and columns.
# You can think of it as an SQL table or a spreadsheet data representation


import pandas as pd

#Create an Empty DataFrame
df = pd.DataFrame()
print (df)


# Create a DataFrame from Lists
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df) 

# Create a DataFrame from List of Lists
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)



"""
Exploratory Data Analysis of Salaries Data
"""

"""
1. Which Male and Female Professor has the highest and the lowest salaries.
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean salaries. 
4. Missing phd - should be mean phd.
5. How many are Male Staff and How many are Female Staff. 
6. How many are Prof, AssocProf and AsstProf. 
7. Who are the senior and junior most employees in the organization.
"""


import pandas as pd
#Read csv file
df = pd.read_csv("data/Salaries.csv")

# Not a good technique to print the Data Frame
print (df)

df.info()


#List first 5 records
df.head()


#Can you guess how to view the last few records;
df.tail(5)


# Gives the row Indexes
df.index


#list the column names / column Indexes
df.columns 


#Check types for all the columns
df.dtypes


#numpyrepresentation of the data
df.values 


# generate descriptive statistics (for numeric columns only)
# Standard Deviation is quite useful tool to figure out 
# how the data is spread above or below the mean.
# The higher the value, the less is reliable or vice versa. 
df.describe() # Numeric Columns

#return max/min values for all columns
df.max() 
df.min()

#return max/min values for all numeric columns
df.mean()
df.median()
df.std()

#returns a random sample of the data frame
df.sample(5) 



"""
Data Frames: method loc

If we need to select a range of rows, using their labels/index 
we can use method loc
"""

df.loc[:1]

df.loc[10:20,['rank','sex']]


"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""
df.iloc[:2]

df.iloc[ 10:21 , [0,4] ]



"""
Selecting a column in a Data Frame with all rows
"""

df.iloc[:,2]

df.loc[:,'phd']
 

# Read the data from a specific Series
df.phd

# Dont use this technique
df.rank

# This is the best practice 
df['phd']


#Select column rank and salary:
df[['rank','salary']]


# Find unique values in a Series / Column
df['rank'].unique()
df['discipline'].unique()
df['sex'].unique()
list1 = df['sex'].unique().tolist()


# intuition about a Rank Series
df['rank']
df['rank'].value_counts()


# to show in Percentage 
df['rank'].value_counts(normalize = True)


# To know the count of male and female candidates
df['sex'] 
df['sex'].value_counts()
df['sex'].value_counts(normalize = True)


#calculate the basic statstics on the salary column
df['salary'].mean()
df['salary'].std()
df['salary'].describe()


#Find how many values in the salary column which are non NaN (use count method);
df['salary'].count()
df['phd'].count()


# Boolean Indexing
# Find those rows which has null values in salary/phd column
df['salary'].isnull()
df[df['salary'].isnull()]

df['phd'].isnull()
df[df['phd'].isnull()]
  

"""
Data Frames groupby method
"""
#Group data using rank
df_rank= df.groupby(['rank'])

df_rank.size()
df_rank.count()
df_rank.groups
# Groups returns a dictionary object
df_rank.groups['AssocProf']
df_rank.groups['AssocProf'][0]

 
#group data using rank followed  by discipline and sex
df_rank=df.groupby(['rank', 'discipline','sex'])
df_rank.groups
df_rank.count()
 
#Calculate mean value for each numeric column per each group
df_rank.mean()


#Calculate mean salary for each type of professor rank:
df.groupby('rank')[['salary','phd']].min()
df.groupby('rank')[['salary','phd']].max()
df.groupby('rank')[['salary','phd']].mean()
        


"""
Data Frame: filtering

To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:

"""

# Boolean Indexing in Pandas
# select only those professors who has salary more than 120000
df['salary'] > 120000
df_sub= df[(df['salary'] > 120000) ]
df_sub

#or

df.loc[df['salary'] > 120000]


# to display only the selected series/column
df.loc[df['salary'] > 120000,'salary']



#filter using multiple columns

df_sub= df[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )
           ]
df_sub
# Or

df.loc[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )]



#Select only those rows that contain female professors:
df_sub = df[df['sex'] == 'Female' ][['salary','sex']]
df_sub

# Or

df.loc[df['sex'] == 'Female' ][['salary','sex']]


"""
DataFrame sorting
"""

# Create a new data frame from the original sorted by the column Salary
df_sorted= df.sort_values( by='service')
df_sorted.head()

# To find the lowest salary of the employee
df_sorted= df.sort_values( by='salary', ascending = [True])
df_sorted.head(1)


# To find the highest salary of the employee
df_sorted= df.sort_values( by='salary', ascending = [False])
df_sorted.head(1)


#We can sort the data using 2 or more columns:
df_sorted= df.sort_values( by=['service','salary'], ascending = [True,True])
df_sorted.head(10)

df_sorted= df.sort_values( by=['service','salary'], ascending = [True,False])
df_sorted.head(10)


"""
Missing Values
"""

df.info()

df[df['phd'].isnull()]

df[df['salary'].isnull()]


# mark zero values as missing or NaN
df['salary'] = df['salary'].replace(0, np.NaN)


  
#There are a number of methods to deal with missing values in the data frame:
new_df = df.dropna()
new_df.count()


new_df2 = df.fillna(0)
new_df2.count()


# Fill All columns with missing values, with mean of that column
df = df.fillna(round(df.mean(),0))
df

# fill all the records with missing values, with mean of that column
df['phd'] = df['phd'].fillna(df['phd'].mean())

# fill all the records with missing values, with mean of that column
df['salary'] = df['salary'].fillna(df['salary'].median())


# How to drop columns
df.drop('discipline',axis=1, inplace=True)

 

"""
Matplotlib
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]

y = [1,2,3,4,5,6,7,8,9,10]


# Setting the title
plt.title("A Line Graph")

# Setting the X Label 
plt.xlabel("X")

# Setting the Y Label
plt.ylabel("Y")

# Displaying the Grid
plt.grid(True)

# Changing the x axes limits of the scale
plt.xlim(0, 10)

# Changing the y axes limits of the scale
plt.ylim(0, 10)

# Or
plt.axis([0, 10, 0, 10]);


# Showing the points on the graph
plt.scatter(x, y)

# Simple Line plot
plt.plot(x, y)

plt.savefig("data/scatter.jpg")

plt.show()


# Changing the color of the line
plt.plot(x, y, color='green') # #000000

# Changing the style of the line
plt.plot(x, y, linestyle='dashed') # solid dashed  dashdot dotted

# For Plotting Scatter Plot
plt.plot(x, y, 'd', color='black'); # o  .  , x  +  v  ^  <  >  s d 

# Scatter Plot with scatter method 
plt.scatter(x, y, marker='.', color='black',label="marker='{0}'".format('.')); # o  .  , x  +  v  ^  <  >  s d 
plt.legend(numpoints=1)



"""
Pie chart, where the slices will be ordered and plotted counter-clockwise:
"""

labels = 'CSE', 'ECE', 'IT', 'EE'
sizes = [15, 30, 25, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

#plt.pie(sizes, labels=labels, autopct='%.0f%%')

# or

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)


plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

        

"""
Plotting a bar chart
"""

import matplotlib.pyplot as plt; 
 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
performance = [10,8,6,4,2,1]
 
plt.bar([0,1,2,3,4,5], performance, align='center', alpha=1.0)
plt.xticks([0,1,2,3,4,5], objects)
plt.ylabel('Usage')
plt.title('Programming Language Usage')
 
plt.show()


"""
Showing bubbles
"""

import numpy as np 
import matplotlib.pyplot as plt 

# Define the number of values
num_vals = 40

# Generate random values
x = np.random.rand(num_vals)
y = np.random.rand(num_vals)

# Define area for each bubble
# Max radius is set to a specified value
max_radius = 25
area = np.pi * (max_radius*np.random.rand(num_vals)) ** 2

# Generate colors
colors = np.random.rand(num_vals)

# Plot the points
plt.scatter(x, y, s=area, c=colors, alpha=.5)
plt.show()


rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar();  # show color scale
# In this way, the color and size of points can be used to convey information in the visualization, 
# in order to visualize multidimensional data.




"""
Now make a pie chart for all car makers
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/Automobile.csv")

series = df["make"].value_counts()

print (series.index[0:11])
print (series.values[0:11])

explode = (0.5,0,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11], autopct='%2.2f%%')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

plt.show()


for x,y in zip(series.index, series.values):
    print (x,y)
    

''' Feedback Form'''
