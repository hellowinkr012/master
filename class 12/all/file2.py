#  Python program to create 
# a module 
    
# Defining a function 
def rpvv(): 
    print("C Sc students rock!") 
  
# Defining a variable 
location = "Raj Niwas Marg"
----------------------------------
# Python program to demonstrate 
# modules 
  
import module_1
  
# Use the function created 
module_1.rpvv() 
  
# Print the variable declared 
print(module_1.location) 

-------------------------------------
Run:
python main_prog1.py
OUTPUT:
C Sc students rock!
Raj Niwas Marg
#  Python program to create 
# a module 
    
# Defining a function 
def rpvv(): 
    print("C Sc students rock!") 
  
# Defining a variable 
location = "Raj Niwas Marg"
----------------------------------
# main_prog1.py :  Python program to demonstrate 
# modules 
  
import module_1 as m
  
# Use the function created 
m.rpvv() 
  
# Print the variable declared 
print(m.location) 

-------------------------------------
Run:
python main_prog1.py
OUTPUT:
C Sc students rock!
Raj Niwas Marg
import math

def circle_area(radius):
    return math.pi * radius ** 2

def square_area(side):
    return side ** 2

def rect_area(length, breadth):
    return length * breadth


def tri_area(a, b, c):
    s = (a + b + c) / 2
    return  math.sqrt(s * (s -a ) * (s - b) * (s -c))
-----------------------------
# main_prog2.py

import area

r = float(input("Enter radius of the circle: "))
print("Area of the circle (in sq. units) %.2f\n" %area.circle_area(r))

side = float(input("Enter the side of the square: "))
print("Area of the square (in sq. units) %.2f\n" %area.square_area(side))

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print("Area of the rectangle (in sq. units) %.2f\n" %area.rect_area(length, breadth))

print("Enter the sides of the triangle")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
print("Area of the triangle(in sq. units) %.2f\n" %area.tri_area(a, b, c))
------------------
run:
python main_prog2.py

OUTPUT:
Enter radius of the circle: 7
Area of the circle (in sq. units) 153.94

Enter the side of the square: 4
Area of the square (in sq. units) 16.00

Enter the length of the rectangle: 4
Enter the breadth of the rectangle: 3
Area of the rectangle (in sq. units) 12.00

Enter the sides of the triangle
First side: 4
Second side: 3
Third side: 5
Area of the triangle(in sq. units) 6.00
In your browser go to  https://ide.cs50.io/ continue with your github account. If you don’t have one. You can make a new one at www.github.com .
Continue with your account and run your python scripts.
If you want you can run multiple languages on it like C, Java, Ruby etc.
(For this we can analyse CBSE papers of last years
 and CBSE Sample paper to be released in November or December)
So, work hard continuously.
*  Functions: scope, parameter passing, mutable/immutable properties
of data objects, passing strings, lists, tuples, dictionaries to functions,default parameters, positional parameters, return values, functions using libraries: mathematical and string functions.
*  File handling: Need for a data file, Types of file: Text files, Binary files and CSV (Comma separated values) files.

*  Text File: Basic operations on a text file: Open (filename – absolute
or relative path, mode) / Close a text file, Reading and Manipulation
of data from a text file, Appending data into a text file, standard input /output and error streams, relative and absolute paths.
*  Binary File: Basic operations on a binary file: Open (filename –
absolute or relative path, mode) / Close a binary file, Pickle Module –
methods load and dump; Read, Write/Create, Search, Append and
Update operations in a binary file.
*  CSV File: Import csv module, functions – Open / Close a csv file,
Read from a csv file and Write into a csv file using csv.reader ( ) and
csv.writerow( ).
*  Using Python libraries: create and import Python libraries.
*  Recursion: simple algorithms with recursion: print a message forever,
sum of first n natural numbers, factorial, Fibonacci numbers;
recursion on arrays: binary search.
*  Idea of efficiency: performance measurement in terms of the number
of operations.
*  Data-structures: Lists as covered in Class XI, Stacks – Push, Pop
using a list, Queues – Insert, Delete using a list.
import math

def circle_area(radius):
    return math.pi * radius ** 2

def square_area(side):
    return side ** 2

def rect_area(length, breadth):
    return length * breadth

def tri_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s -a) * (s - b) * (s -c))
# import area module
import area

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f\n" %area.circle_area(r))

side = float(input("Enter the side of the square: "))
print("Area of the square (in sq. units) %.2f\n" %area.square_area(side))

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print("Area of the rectangle (in sq. units) %.2f\n" %area.rect_area(length, breadth))

print("Enter the sides of the triangle")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
print("Area of the triangle(in sq. units) %.2f\n" %area.tri_area(a, b, c))
# import area module
from area import *

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f\n" %circle_area(r))

side = float(input("Enter the side of the square: "))
print("Area of the square (in sq. units) %.2f\n" %square_area(side))

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print("Area of the rectangle (in sq. units) %.2f\n" %rect_area(length, breadth))

print("Enter the sides of the triangle")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
print("Area of the triangle(in sq. units) %.2f\n" %tri_area(a, b, c))
# import area module
from area import circle_area, tri_area

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f\n" %circle_area(r))



print("Enter the sides of the triangle")
a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))
print("Area of the triangle(in sq. units) %.2f\n" %tri_area(a, b, c))

import math

#### LIBRARY TO FIND AREA OF * CIRCLE , * CYLINDER , * CONE ####

##AREA OF CIRCLE 

def circle(radius) :
    area=math.pi*(radius**2)
    return area

##AREA OF CONE 
        
def cone(radius,height) :
    area=1/3*(math.pi*(height*(radius**2)))
    return area

##AREA OF CYLINDER    
            
def cylinder(radius,height) :
    area=math.pi*(height*(radius**2))
    return area

#### SINGLE AREA ACCESSING MODULE ####
                
def area_show(argument) :
    argument2=argument.lower()
    if argument2.strip()=="circle" :
        rads=int(input("Enter Radius of Circle : "))
        print("%.4f"%circle(rads))
       
    elif argument2.strip()=="cone" :
        rads=int(input("Enter Radius of Cone : "))
        heis=int(input("Enter Height of Cone :"))
        print("%.4f"%circle(rads,heis))
       
    elif argument2.strip()=="cylinder" :
        rads=int(input("Enter Radius of Cylinder : "))
        heis=int(input("Enter Height of Cylinder :"))     
        print("%.4f"%cylinder(rads,heis))
        
    else :
        print(f"ERROR OCCURED : THIS MODULE {argument} IS NOT IN <Xarea> MODULE .")
import Xarea

Xarea.area_show("circle")
print()

Xarea.area_show("cone")
print()

Xarea.area_show("cylinder")
print()


#### Output ####

Enter Radius of Circle : 6
AREA OF circle in sq.units 113.0973

Enter Radius of Cone : 6
Enter Height of Cone :6
AREA OF cone in sq.units 226.1947

Enter Radius of Cylinder : 6
Enter Height of Cylinder :6
AREA OF cylinder in sq.units 678.5840


[Program finished]
Time:11:15-12:00 pm(Wed, Thurs,Fri,Sat)
Copy down the link Meeting URL: https://meet.google.com/xhb-rsyo-caa
from math import pi

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2
# import module circle
import circle

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f" %circle.area(r))
print("Circumference of the circle = %.2f" %circle.circumference(r))
# import module circle
from circle import *

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f" %area(r))
print("Circumference of the circle = %.2f" %circumference(r))
# import module circle
from circle import area

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f" %area(r))
Time:11:15-12:00 pm(Mon,Tues,Wed, Thurs,Fri)
Copy down the link Meeting URL: https://meet.google.com/xhb-rsyo-caa
Modules may be useful for more than one programming project, and in that case it makes less sense to keep a module in a particular directory that’s tied to a specific project.
If you want to use a Python module from a location other than the same directory where your main program is, you have a few options.
One option is to invoke the path of the module via the programming files that use that module. This should be considered more of a temporary solution that can be done during the development process as it does not make the module available system-wide.
The sys module is part of the Python Standard Library and provides system-specific parameters and functions that you can use in your program to set the path of the module you wish to implement.
For example, let’s say we moved the circle.py file and it is now on the path c:\PythonProgs\modules while the main_v4.py file is in another directory.
In our main_v4.py file, we can still import the hello module by importing the sys module and then appending c:\PythonProgs\modules to the path that Python checks for files:      sys.path.append('C:\PythonProgs\modules')
import sys
sys.path.append('C:\PythonProgs\modules')

# import module circle
import circle

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f" %circle.area(r))
print("Circumference of the circle = %.2f" %circle.circumference(r))

Run:
python main_v4.py

OUTPUT:
Enter the radius of the circle: 8.4
Area of the circle(in sq. units) = 221.67
Circumference of the circle = 52.78
A second option that you have is to add the module to the path where Python checks for modules and packages. This is a more permanent solution that makes the module available environment-wide or system-wide, making this method more portable.
python

Next, import the sys module:
import sys

Then have Python print out the system path:
print(sys.path)
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print(sys.path)
['', 'C:\\Users\\Vinod Nayak\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\Vinod Nayak\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\Vinod Nayak\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\Vinod Nayak\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\Vinod Nayak\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Users\\Vinod Nayak\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']
>>>
'C:\\Users\\Vinod Nayak\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages’
(Note: it will be different on different installation)
# import module circle
import circle

r = float(input("Enter the radius of the circle: "))
print("Area of the circle(in sq. units) = %.2f" %circle.area(r))
print("Circumference of the circle = %.2f" %circle.circumference(r))


When you run your program, it should complete without error.
$ python main_v4.py
Enter the radius of the circle: 7
Area of the circle(in sq. units) = 153.94
Circumference of the circle = 43.98
In Android system .

My no : 8700621420
And mark your Attendance within 3 minutes (till 8:03am)

अब मौका आ गया है एक और Entrepreneur के साथ interact करने का जो *Primero Skills & Training Pvt Ltd* के *Managing Director* के तौर पर देशभर में युवाओं को jobs से जुड़ी skills & training provide कर रहे हैं।

*बुधवार, 8 जुलाई 2020, 11:00 am* बजे- मिलिए एक अनुभवी Entrepreneur, *Mr Jayanta Das* से, उनकी Professional Journey के बारे में जानिए और अपने मन में आ रहे सवाल पूछकर अपनी समझ बढ़ाइए।

साथ ही इस interaction में हमारे साथ जुड़ेंगे- 
*Chief Guest : Shri Manish Sisodia (Deputy Chief Minister, Delhi)* 

*Guest of Honour : Mrs Manisha Saxena | IAS, Secretary (Education) , Delhi*

इसके लिए https://bit.ly/SCERTDelhiYT पर क्लिक करके SCERT Delhi के Youtube Channel को Subscribe करिए। यह Live Entrepreneur Interaction इसी YouTube channel पर Live प्रसारित होगा।
● Functions: scope, parameter passing, mutable/immutable properties
of data objects, passing strings, lists, tuples, dictionaries to functions,
default parameters, positional parameters, return values, functions
using libraries: mathematical and string functions.
● File handling: Need for a data file, Types of file: Text files, Binary files
and CSV (Comma separated values) files.
● Text File: Basic operations on a text file: Open (filename – absolute
or relative path, mode), Close a text file, Reading and Manipulation of
data from a text file, Appending data into a text file, standard input /
output and error streams, relative and absolute paths.
● Binary File: Basic operations on a binary file: Open (filename –
absolute or relative path, mode), Close a binary file, Pickle Module –
methods load and dump; Read, Write/Create, Search, Append and
Update operations in a binary file.
● CSV File: Import csv module, functions – Open, Close a csv file, Read
from a csv file and Write into a csv file using csv.reader ( ) and
csv.writerow( ).
● Using Python libraries: Import Python libraries.
● Data-structures: Lists as covered in Class XI, Stacks – Push, Pop using
a list.
 ●    Idea of efficiency : performance measurement in terms of the number of operations.
 ●    Data-structures: Lists as covered in Class XI, Stacks – Push, Pop using a list, Queues – Insert, Delete using a list. (One of the data structure Stack or Queue.  Note : While setting the question paper a students will have an option between Stack and Queue.)
from math import pi

def cal_csa(radius, height):
    return 2 * pi * radius * height

def cal_tsa(radius, height):
    return 2 * pi * radius * height + 2 * pi * radius ** 2

def cal_vol(radius, height):
    return pi * ( radius ** 2 ) * height
from math import pi, sqrt

def cal_csa(radius, height):
    l = sqrt(radius ** 2  + height ** 2)
    return  pi * radius * l

def cal_tsa(radius, height):
    l = sqrt(radius ** 2  + height ** 2)
    return pi * radius * l + pi * radius ** 2

def cal_vol(radius, height):
    return  (1 / 3) * pi * ( radius ** 2 ) * height
import cylinder, cone

print("Enter the dimensions of the cylinder:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %cylinder.cal_csa(r, h))
print("Total surface area(in sq. units): %.2f" %cylinder.cal_tsa(r, h))
print("Volume(in cu. units): %.2f" %cylinder.cal_vol(r, h))

print()

print("Enter the dimensions of the cone:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %cone.cal_csa(r, h))
print("Total surface area(in sq. units): %.2f" %cone.cal_tsa(r, h))
print("Volume(in cu. units): %.2f" %cone.cal_vol(r, h))
python main_prog7.py

Output:
Enter the dimensions of the cylinder:
Radius: 7
Height: 5
Curved surface area(in sq. units): 219.91
Total surface area(in sq. units): 527.79
Volume(in cu. units): 769.69

Enter the dimensions of the cone:
Radius: 8
Height: 7
Curved surface area(in sq. units): 267.16
Total surface area(in sq. units): 468.23
Volume(in cu. units): 469.14

You can create an alias (second name) when you import a module by using the as keyword.
Examples:
import test as t
import math as Mathematics, sys as system

Like module aliasing member aliasing is also supported in Python.
Example:
from cylinder import cal_csa as csa, cal_tsa as tsa
from math import pi

def cal_csa(radius, height):
    elif argument2.strip()=="cone" :
        rads=int(input("Enter Radius of Cone : "))
        heis=int(input("Enter Height of Cone :"))
        print("%.4f"%circle(rads,heis))
       
    elif argument2.strip()=="cylinder" :
        rads=int(input("Enter Radius of Cylinder : "))
        heis=int(input("Enter Height of Cylinder :"))     
        print("%.4f"%cylinder(rads,heis))
        
    else :
        print(f"ERROR OCCURED : THIS MODULE {argument} IS NOT IN <Xarea> MODULE .")
import Xarea
    return 2 * pi * radius * height

def cal_tsa(radius, height):
    return 2 * pi * radius * height + 2 * pi * radius ** 2

def cal_vol(radius, height):
    return pi * ( radius ** 2 ) * height
from math import pi, sqrt

def cal_csa(radius, height):
    l = sqrt(radius ** 2  + height ** 2)
    return  pi * radius * l

def cal_tsa(radius, height):
    l = sqrt(radius ** 2  + height ** 2)
    return pi * radius * l + pi * radius ** 2

def cal_vol(radius, height):
    return  (1 / 3) * pi * ( radius ** 2 ) * height
# module aliasing

import cylinder as cy, cone as cn

print("Enter the dimensions of the cylinder:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %cy.cal_csa(r, h))
print("Total surface area(in sq. units): %.2f" %cy.cal_tsa(r, h))
print("Volume(in cu. units): %.2f" %cy.cal_vol(r, h))

print()

print("Enter the dimensions of the cone:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %cn.cal_csa(r, h))
print("Total surface area(in sq. units): %.2f" %cn.cal_tsa(r, h))
print("Volume(in cu. units): %.2f" %cn.cal_vol(r, h))
# member aliasing

from cylinder import cal_csa as csa, cal_tsa as tsa, cal_vol

print("Enter the dimensions of the cylinder:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %csa(r, h))
print("Total surface area(in sq. units): %.2f" %tsa(r, h))
print("Volume(in cu. units): %.2f" %cal_vol(r, h))


ketan anand	
kunal sharma	
vikas 210	
suraj shukla	
vaibhav tiwari	
samrat chhabra	
himanshi sharma	
pawan joshi	
himanshu jha	
vishal kumar	
shivam kumar	
nitesh gupta	
aman sharma	
vaishnavi sharma	
mayank tiwari	
rahul kumar	
sahzad hussain	
dipsikha jha	
kirti bisht	
vivek kumar	
Akshay Sharma

Modular programming is a software design technique to split your 
code into separate parts. These parts are called modules.
 The focus for this separation should be to have modules 
 with no or just few dependencies upon other modules. 
 In other words: Minimization of dependencies is the goal.

 Package = group of related modules
 Library = group of related modules/packages

 User Created Library  User = Programmer
 Standard Library = Library provided by Language 
 math module
 os package 
 sys package
from math import pi, sqrt

def cylinder_csa(radius, height):
    return 2 * pi * radius * height

def cone_csa(radius, height):
    l = sqrt(height ** 2 + radius ** 2)
    return pi * radius * l
from math import pi, sqrt

def cylinder_tsa(radius, height):
    return 2 * pi * radius * height + 2 * pi * radius ** 2

def cone_tsa(radius, height):
    l = sqrt(height ** 2 + radius ** 2)
    return pi * radius * l + pi * radius ** 2
from math import pi

def cylinder_vol(radius, height):
    return pi * (radius ** 2) * height

def cone_vol(radius, height):
    return (1 / 3) * pi * (radius ** 2) * height
# import package
from mensuration import csa, tsa, vol

print("Enter the dimensions of the cylinder:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %csa.cylinder_csa(r, h))
print("Total surface area(in sq. units): %.2f" %tsa.cylinder_tsa(r, h))
print("Volume(in cu. units): %.2f" %vol.cylinder_vol(r, h))

print()

print("Enter the dimensions of the cone:")
r = float(input("Radius: "))
h = float(input("Height: "))

print("Curved surface area(in sq. units): %.2f" %csa.cone_csa(r, h))
print("Total surface area(in sq. units): %.2f" %tsa.cone_tsa(r, h))
print("Volume(in cu. units): %.2f" %vol.cone_vol(r, h))
Rollno 12529
Roll no 12520
I am unable to join

We are proud to announce EMC's 6th Digital *Live Entrepreneur Interaction (Digital LEI)*.

 *Ms Sujata and Ms Taniya*, *(Founders- Suta)* will be interacting live with our students and teachers through the SCERT Delhi youtube channel.

*Chief Guest : Shri Manish Sisodia (Deputy Chief Minister, Delhi)* 

*Guest of Honour* : Mrs Manisha Saxena | IAS, Secretary (Education) , Delhi
Date : 15th July (Wednesday), 2020
Time : 12:00 pm
YouTube channel:
https://bit.ly/SCERTDelhiYT


Thank you !

Dr. Sapna Yadav
SCERT Delhi
Also attended
#  (or a tuple containing 9 elements corresponding to struct_time)
#  as an argument and returns the seconds passed since epoch in local time.
#  Basically, it's the inverse function of localtime().
import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

local_time = time.mktime(t)
print("Local time:", local_time)
#  how mktime() and localtime() are related.
import time

seconds = 1594788463

# returns struct_time
t = time.localtime(seconds)
print("t1: ", t)

# returns seconds from struct_time
s = time.mktime(t)
print("\ns:", seconds)
#  (or a tuple containing 9 elements corresponding to struct_time)
#  as an argument and returns a string representing it. Here's an example:
import time

t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)
# (or tuple corresponding to it) as an argument 
# and returns a string representing it based on the format code used.
import time

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)
# a string representing time and returns struct_time.
import time

time_string = "21 June, 2020"
result = time.strptime(time_string, "%d %B, %Y")

print(result)
import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result)
  time.sleep(1)
#  better version of the digital clock program.

import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=True)
  print("\r", end="", flush=True)
  time.sleep(1)

import threading 
  
def print_hello_three_times():
  for i in range(3):
    print("Hello")
  
def print_hi_three_times(): 
    for i in range(3): 
      print("Hi") 

t1 = threading.Thread(target=print_hello_three_times)  
t2 = threading.Thread(target=print_hi_three_times)  

t1.start()
t2.start()
import threading 
import time
  
def print_hello():
  for i in range(4):
    time.sleep(0.5)
    print("Hello")
  
def print_hi(): 
    for i in range(4): 
      time.sleep(0.7)
      print("Hi") 

t1 = threading.Thread(target=print_hello)  
t2 = threading.Thread(target=print_hi)  
t1.start()
t2.start()
# Time intervals are floating-point numbers in units of seconds.
#  Particular instants in time are expressed in seconds
#  since 12:00am, January 1, 1970(epoch).
import time  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
import calendar

cal = calendar.month(2003, 5)
print ("Here is the calendar:")
print (cal)
import time
seconds = time.time()
print("Seconds since epoch =", seconds)
import time

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

local_time = time.ctime()
print("Local time:", local_time)
# execution of the current thread 
# for the given number of seconds.
import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")
# the number of seconds passed since
#  epoch as an argument and returns struct_time in local time.
import time

result = time.localtime(1594788221)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
#  passed since epoch as an argument 
# and returns struct_time in UTC.
import time

result = time.gmtime(1594876197)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_min:", result.tm_min)

result = time.localtime(1594876197)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_min:", result.tm_min)
import datetime

date_object = datetime.date.today()
print(date_object)

import datetime

d = datetime.date(2019, 4, 13)
print(d)
from datetime import date

today = date.today()

print("Current date =", today)
# We can also create date objects 
# from a timestamp. 
# A Unix timestamp is the number of seconds
#  between a particular date and January 1, 1970 at UTC.
#  You can convert a timestamp to date 
# using fromtimestamp() method.
from datetime import date

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)
from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
# A time object instantiated 
# from the time class represents the local time.

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

from datetime import datetime

# datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

from datetime import datetime, date

t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))
roll no. 12515

Hello everyone.....here's the video on CBSE DELETED TOPICS Class XII ENGLISH CORE - and RATIONALISED CURRICULUM 2020-21.....
Kindly add the following no to this grp

Bio Pdf
📷https://drive.google.com/drive/folders/1JDD1ARp5uoGorRO4qFQoqM6W99Lr4YSx?usp=sharing
Chemistry pdf
📷https://drive.google.com/drive/folders/1T1kymbqE4BD5mHiMkZMb3e-cy8qqRwFs?usp=sharing
maths pdf
📷https://drive.google.com/drive/folders/1zBnVb9V0L1dg-TiM03fOWzEOFKA2ayOt?usp=sharing
physics pdf
📷https://drive.google.com/drive/folders/1B5iTE0jGnxZRcEocpZSr3b2aQyxYu3a8?usp=sharing
Himanshi Sharma
Till yesterday(21-7-20) record

https://youtu.be/6YwCVXqMsl8
Get DIKSHA app from: https://play.google.com/store/apps/details?id=in.gov.diksha.app&referrer=utm_source%3D8f6547678728c5b075b54c3a62eaadec2dd02cf2%26utm_campaign%3Dshare_app
Study and Download from anywhere.
#LEADDELHI

Roll no. : 12508

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']

print(sea_creatures[1])
print(sea_creatures[-3])
print(sea_creatures[10])

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)

# concatenate string items in a list 
# with other strings using the + operator
print('Sammy is a ' + sea_creatures[0])

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)

sea_creatures[1] = 'octopus'
print(sea_creatures)

sea_creatures[-3] = 'blobfish'
print(sea_creatures)

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)



# When creating a slice, as in [1:4], 
# the first index number is where the slice starts (inclusive), 
# and the second index number is where the slice ends (exclusive), 
print(sea_creatures[1:4])

# If we want to include either end of the list,
#  we can omit one of the numbers in the list[x:y] syntax
print(sea_creatures[:3])
print(sea_creatures[2:])

# We can also use negative index numbers
#  when slicing lists, just like with positive index numbers:
print(sea_creatures[-4:-2])
print(sea_creatures[-3:])
#  is called stride, which refers to how many 
# items to move forward after the first item 
# is retrieved from the list.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(numbers)
print(numbers[1:11:2])
print(numbers[::3])

sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']

print(sea_creatures + oceans)
# it can be used to add an item (or several) 
# in list form to the end of another list.
#  Remember to place the item in square brackets:

sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
sea_creatures = sea_creatures + ['yeti crab']
print (sea_creatures)

sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']


# By using the * operator we can replicate 
# our lists by the number of times we specify.

# Let’s multiply the sea_creatures list by 2 
# and the oceans list by 3:

print(sea_creatures * 2)
print(oceans * 3)
sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']

# The += and *= compound operators can be used to 
# populate lists in a quick and automated way

for x in range(1,4):
    sea_creatures += ['fish']
    print(sea_creatures)

# The *= operator behaves in a similar way:
sharks = ['shark']

for x in range(1,4):
    sharks *= 2
    print(sharks)
# it can have elements of different data types

#  Create list
list1 = [14, 'March', 1879, 'Ulm', 'Germany']
print(list1)

sea_creatures =['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone', 'yeti crab']

del sea_creatures[1]
print(sea_creatures)

sea_creatures =['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone', 'yeti crab']

del sea_creatures[1:4]
print(sea_creatures)

sea_names = [['shark', 'octopus', 'squid', 'mantis shrimp'],['Sammy', 'Jesse', 'Drew', 'Jamie']]

print(sea_names[1][0])
print(sea_names[0][0])
print(sea_names[1][2])
#  list.append()

fish = ['barracuda','cod','devil ray','eel']
fish.append('flounder')
print(fish)
#  list.insert()
fish = ['barracuda','cod','devil ray','eel', 'flounder']

fish.insert(0,'anchovy')
print(fish)

fish.insert(3,'damselfish')
print(fish)
# list.extend()
fish = ['barracuda','cod','devil ray','eel', 'flounder']

more_fish = ['goby','herring','ide','kissing gourami']

fish.extend(more_fish)
print(fish)
I have been observing that they are not attending the chemistry classes too on regular basis.

Deepanshu
Supreet Singh
MD Sayeed Irfan
Sahzad Hussain
Kaushal Kumar
Aman (11)
Hemlata
Samrat 
Gaurav Sharma
Dipsikha 
Manish

Lockdown will not remain for infinite time....

Do not try to invite an inevitable disciplinary action against you by not submitting the homework on time and not attending the classes.
This is for the last time to all of u....
It was told to share the homework on comma group ...

Today's attendance link👆🏻
# list.sort()

fish = ['anchovy', 'barracuda', 'cod', 'eel', 'flounder']
fish.sort(reverse=True)
print(fish)

Bio Pdf
📷https://drive.google.com/drive/folders/1JDD1ARp5uoGorRO4qFQoqM6W99Lr4YSx?usp=sharing
Chemistry pdf
📷https://drive.google.com/drive/folders/1T1kymbqE4BD5mHiMkZMb3e-cy8qqRwFs?usp=sharing
maths pdf
📷https://drive.google.com/drive/folders/1zBnVb9V0L1dg-TiM03fOWzEOFKA2ayOt?usp=sharing
physics pdf
📷https://drive.google.com/drive/folders/1B5iTE0jGnxZRcEocpZSr3b2aQyxYu3a8?usp=sharing
# demonstrate stack implementation 
# using list 
  
  
stack = [] 
  
# append() function to push 
# element in the stack 
stack.append('a') 
stack.append('b') 
stack.append('c') 
  
print('Initial stack') 
for x in range(len(stack)):
    print(stack[len(stack) - x - 1 ])


  
# pop() fucntion to pop 
# element from stack in  
# LIFO order 
print('\nElements poped from stack:') 
print(stack.pop()) 

print('\nStack after some elements are poped:') 
for x in range(len(stack)):
    print(stack[len(stack) - x - 1 ])
print()
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are poped:') 
for x in range(len(stack)):
    print(stack[len(stack) - x - 1 ])
  
# uncommenting 
print(stack.pop())   
# will cause an IndexError  
# as the stack is now empty
# using list

# Check whether the stack is empty
def isStackEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

# Push item on to the stack   
def push(stack, item):
    stack.append(item)

# Pop itemfrom the stack
def pop(stack):
    if isStackEmpty(stack):
        print("Stack is empty")
    else:
        item = stack.pop()
        print("The element popped: " + str(item))

# Display the contents of the stack
def display(stack):
    if isStackEmpty(stack):
        print("Stack is empty")
    else:
        top = len(stack) - 1
        for i in range(top, -1, -1):
            print(stack[i])
# Display the element of the top of the stack
def top(stack):
    if isStackEmpty(stack):
        print("Stack is empty")
    else:
        print("The element of the top of the stack: " + str(stack[-1]))

# Executable code
if __name__ == "__main__":
    s = []
    display(s)

    push(s, 11)
    push(s, 22)
    push(s, 33)
    push(s, 44)
    top(s)
    display(s)

    pop(s)
    pop(s)
    display(s)

    pop(s)
    top(s)
    pop(s)
    pop(s)


Run and Output:
$ python stack.py
Stack is empty
The element of the top of the stack: 44
The element popped: 44
The element popped: 33
The element popped: 22
The element of the top of the stack: 11
The element popped: 11
Stack is empty
# demonstrate queue implementation 
# using list 
  
# Initializing a queue 
queue = [] 
  
# Adding elements to the queue 
queue.append('a') 
queue.append('b') 
queue.append('c') 
  
print("Initial queue") 
print(queue) 
  
# Removing elements from the queue 
print("\nElements dequeued from queue") 
print(queue.pop(0)) 
print(queue.pop(0)) 
print(queue.pop(0)) 
  
print("\nQueue after removing elements") 
print(queue) 
  
# Uncommenting print(queue.pop(0)) 
# will raise and IndexError 
# as the queue is now empty 


Run and Output:
$ python queue1.py
Initial queue
['a', 'b', 'c']

Elements dequeued from queue
a
b
c

Queue after removing elements
[]
# using list and functions

# Check whether the queue is empty
def isQueueEmpty(queue):
    if len(queue) == 0:
        return True
    else:
        return False

# Insert an element at the rear end of the queue
def enqueue(queue, item):
    queue.append(item)

# Delete an element from the front of the queue
def dequeue(queue):
    if isQueueEmpty(queue):
        print("Queue is empty")
    else:
        item = queue.pop(0)
        print("The element deleted from the queue: " + str(item))
    
# Display the contents of the queue
def display(queue):
    if isQueueEmpty(queue):
        print("Queue is empty")
    else:
        front = 0
        rear = len(queue) - 1

        for i in range(front, rear + 1):
            print(queue[i], end = ' ')
        print()

# Executable code
if __name__ == "__main__":
    Q = []
    display(Q)

    enqueue(Q, 9)
    enqueue(Q, 18)
    enqueue(Q, 27)
    enqueue(Q, 36)
    enqueue(Q, 45)

    display(Q)

    dequeue(Q)
    dequeue(Q)

    display(Q)

    dequeue(Q)
    dequeue(Q)
    dequeue(Q)
    dequeue(Q)

Run and Output:
$ python queue.py
Queue is empty
The element deleted from the queue: 9
The element deleted from the queue: 18
The element deleted from the queue: 27
The element deleted from the queue: 36
The element deleted from the queue: 45
Queue is empty
enqueue(queue, item), dequeue(queue) and display(queue)
The item contains the following fields:
member_no	integer
member_name	string
age		integer
(a) 32/ 3 V	(b) 32 / 5 V 	(c) 16 / 3 V	(d) 20/ 3 V
T  = 2π.  √L/g 
where g is a constant.
By what per cent should the length of the pendulum should be changed in order to correct a loss of 2 minutes per day?
(Hint: use differentiation)
(Hint; First Law of Thermodynamics)
# check whether a queue is empty
    def IsQueueEmpty(self):
        if len(self)==0:
            return "IsEmpty"

        else:
            return "IsNotEmpty"
    
    #Insert a value at rear end of the queue
    def Enqueue(self,item):
        #if the item  is dict type
        if type(item)==dict:

            #checking the keys of input data
            if str(item.keys())!="dict_keys(['member_no', 'member_name', 'age'])":
                raise KeyError("only member_no  , member_name , age are allowed")

            #checking the data type of values
            elif type(item["member_no"])!=int or type(item["member_name"])!=str or type(item["age"])!=int:
                raise TypeError("you have enetered wrong data type")

            #appending new input data into the queue instance
            else:
                self.append(item)
            
        #if the item is list then converting it into dict data type 
        elif type(item)==list and len(item)==3:
            #checking the  data types of input values
            if type(item[0])!=int and  str(item[0]).isdigit()==False or type(item[2])!=int or str(item[2]).isdigit()==False:
                raise TypeError("only int is allowed")

            elif type(item[1])!=str:
                raise TypeError("only string is allowed")

            #appending the new data type into the  queue instance
            else:
                dict_item={
                    "member_no":int(item[0]),
                    "member_name":str(item[1]),
                    "age":int(item[2])
                }
                self.append(dict_item)
        else:
            raise TypeError("You have entered wrong data type")

    #delete a value from the top end of the queue
    def Dequeue(self):
        if self.IsQueueEmpty()=="IsEmpty":
            raise ValueError("Empty queue")
        else:
            return self.pop(0)
    
    #display the items of the queue
    def display(self):
        if self.IsQueueEmpty()=="IsEmpty":
            print("EmptyQueueInstance")
        else:
            front=0                #index of front end of the instance
            rear=len(self)-1       #index of rear end of the instance
            
            print("---------------------------front end----------------------------")

            for item in range(front,rear+1):

                print(f'''member no:{self[item]["member_no"]}
member name :{self[item]["member_name"]}
age:{self[item]["age"]}''')

                print()
                print()

            print("---------------------------rear end----------------------------")
            print()
            print()
 
    #Prevention of insertion of the item in the middle of the queue
    def insert(self,item):
        raise AttributeError("you can't insert any item in the middle of a queue instance")


#driver's code
if __name__=="__main__":

    q1=Queue()
    q1.Enqueue([6,"kuldeep",16])
    q1.Enqueue([5,"surajshukla",18])
    q1.display()

    q1.Dequeue()
    q1.display()
    
    q1.Enqueue({"member_no":4,"member_name":"suraj","age":4})
    q1.display()
member no:6
member name :kuldeep
age:16


member no:5
member name :surajshukla
age:18


---------------------------rear end----------------------------


---------------------------front end----------------------------
member no:5
member name :surajshukla
age:18


---------------------------rear end----------------------------


---------------------------front end----------------------------
member no:5
member name :surajshukla
age:18


member no:4
member name :suraj
age:4


---------------------------rear end----------------------------

def enqueue(queue : list , item):
    queue.append(item) #concating the item

def dequeue(queue: list):
    return queue.pop(0) #popping and returning the element at index 0 

def display(queue : list):
    print(queue)


class Queue():
    __slots__ = ['data']
    def __init__(self , *args):
        if args:
            self.data = list(args)
        else:
            self.data = []

    def enqueue(self,item):
        self.data.append(item)
    
    def dequeue(self):
        return self.data.pop(0)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for i in self.data:
            yield i
    def toList(self):
        return self.data

class Queue3(collections.UserList):
    # another method to implement queueu
    def __init__(self, *args):
        if args:
            self.data = list(args)
        else:
            self.data = []


    def enqueue(self,item):
        self.data += item

    def dequeue(self):
        return self.data.pop(0) 

if __name__ =='__main__':
    ourqueue = [1,2,3]
    print('Our queue is ',ourqueue)
    enqueue(ourqueue,24)
    print('after appending 24')
    display(ourqueue)
    print(dequeue(ourqueue))



    l = Queue(1,2,3)
    print('The lenght of our queue',len(l))
    print('Queue is',l)
    for i in l:
        print(i) #iterating over the queue

    l.enqueue(123) # appending in the queue
    print('The queue after enqueue :',l) 
    print('The type of queue',type(l))
    print('After converting our queue in list',l.toList())
    print(l.dequeue())
    print(l)
    m = Queue3(1,2,3)
    print(len(m))
    print(m)
Our queue is  [1, 2, 3]
after appending 24
[1, 2, 3, 24]
The lenght of our queue 3
Queue is [1, 2, 3]
The queue after enqueue : [1, 2, 3, 123]
The type of queue <class '__main__.Queue'>
After converting our queue in list [1, 2, 3, 123]
[2, 3, 123]
[1, 2, 3]
#
# enqueue(queue, item), dequeue(queue) and display(queue)
# The item contains the following fields:
# member_no    :    integer
# member_name    :    string
# age	:	integer


# Checks If Queue Is Empty
def isQueueEmpty(queue) :
	
	if len(queue) == 0 :
	    return True
	    
	else :
	    return False


# Enqueue The Item At Last Of Queue
def enqueue(queue, item) :
    
    if (not (isinstance(item , (list , tuple , dict)))) :
        
        print("Only List And Tuple Are Allowed As Item To Be Enqueue")
        print()
    
    
    
    elif (len(item) != 3) :
        
        print("Only Member_no , Member_name , Age Are Allowed As Fields Of Item")
        print()
    
    
    
    elif (not (isinstance(item[0] , int) and isinstance(item[1] , str) and isinstance(item[2] , int))) :
        
        print("""Fields In Item Should Be As Per :
        
        member_no    :    integer
        member_name    :    string
        age	:	integer

        """)
      
       
    else :
        
        item = tuple(item)
        queue.append(item)
    

# Dequeue The Item From Starting Of Queue
def dequeue(queue) :
    
    if isQueueEmpty(queue) :
        
        print("Queue is empty")
        
    else :
        
        print(f"{queue.pop(0)} is dequeued from the Queue")
        

# Display The Queue
def display(queue) :
    
    print("_" * 45)
    print("member_no\tmember_name\t\tage")
    print("_" * 45)
    
    for member in queue :
        
        for i in range(len(member)) :
            
            print(member[i] , end = "\t\t")
            
        print()
    
    print("_" * 45)    
    print()
        
        
if __name__ == "__main__" :
    
    Q = []
    
    display(Q)
    dequeue(Q)
    
    enqueue(Q , (12501 , "Kunal Sharma" , 17))
    enqueue(Q , [12516 , "Aman Sharma" , 17])
    enqueue(Q , (12508 , "Vikas Kumar" , 17))
    enqueue(Q , (12519 , "Vaibhav Tiwari" , 17))
    enqueue(Q , [12521 , "Ketan Anand" , 17])
    enqueue(Q , (12522 , "Himanshu Jha" , 17))
    # etc .......
    
    
    display(Q)
    
    dequeue(Q)
    dequeue(Q)
    
    display(Q)
    
    dequeue(Q)
    dequeue(Q)
    dequeue(Q)
    dequeue(Q)
    
    
    display(Q)
    
    dequeue(Q)
_____________________________________________
member_no       member_name             age
_____________________________________________
_____________________________________________

Queue is empty
_____________________________________________
member_no       member_name             age
_____________________________________________
_____________________________________________

(12501, 'Kunal Sharma', 17) is dequeued from the Queue
(12516, 'Aman Sharma', 17) is dequeued from the Queue
_____________________________________________
member_no       member_name             age
_____________________________________________
_____________________________________________

(12508, 'Vikas Kumar', 17) is dequeued from the Queue
(12519, 'Vaibhav Tiwari', 17) is dequeued from the Queue
(12521, 'Ketan Anand', 17) is dequeued from the Queue
(12522, 'Himanshu Jha', 17) is dequeued from the Queue
_____________________________________________
member_no       member_name             age
_____________________________________________
_____________________________________________

Queue is empty
def IsQueueEmpty(queue):
    if len(queue) == 0:
       return True
    else:
     return False


# Puting an element at the rear end 
def Enqueue(queue, member_no, member_namestring, age):
    queue.append(member_no)
    queue.append(member_namestring)
    queue.append(age)

# deleting an element from the front end

def Dequeue(queue):
  if IsQueueEmpty (queue):
        print("Queue is Empty")

  else: 
   item = queue.pop(0)
   print(f" The elements deleted from the queue:{item}")
   print()  
#Displaying queue
def Display(queue):
     if IsQueueEmpty(queue):
          print("Queue is empty")

     else: 
         front = 0 
         rear = len(queue) -1
         for i in range(front, rear +1):
             print(queue[i],end = ' ')
          
#Executable code
if __name__ ==  "__main__":
 
    q = []
    Display(q)

    Enqueue(q,121, "abc", 17 )
    Enqueue(q,202, "adc",18)
    Enqueue(q,103, "ghg",19)
    Enqueue(q,204, "ghj",20)

    Display(q)

    Dequeue(q)
    Dequeue(q)

    Display(q)

    Dequeue(q)
    Dequeue(q)
def IsQueueEmpty(queue):
    if len(queue) == 0:
       return True
    else:
     return False


# Puting an element at the rear end 
def Enqueue(queue, member_no, member_namestring, age):
    queue.append(member_no)
    queue.append(member_namestring)
    queue.append(age)

# deleting an element from the front end

def Dequeue(queue):
  if IsQueueEmpty (queue):
        print("Queue is Empty")

  else: 
   item = queue.pop(0)
   item = queue.pop(0)
   item = queue.pop(0)
   print(f" The elements deleted from the queue:{item}")
   print()  
#Displaying queue
def Display(queue):
     if IsQueueEmpty(queue):
          print("Queue is empty")

     else: 
         front = 0 
         rear = len(queue) -1
         for i in range(front, rear +1):
             print(queue[i],end = ' ')
          
#Executable code
if __name__ ==  "__main__":
 
    q = []
    Display(q)

    Enqueue(q,121, "abc", 17 )
    Enqueue(q,202, "adc",18)
    Enqueue(q,103, "ghg",19)
    Enqueue(q,204, "ghj",20)

    Display(q)

    Dequeue(q)
    Dequeue(q)

    Display(q)

    Dequeue(q)
    Dequeue(q)
DISPLAY(stack)
The emp_data contains the following fields:
emp_no 	integer
emp_name	string
emp_post	string
emp_salary	float
# using list

# Check whether the Queue is empty
def isqueueEmpty(queue):
    if len(queue) == 0:
        return True
    else:
        return False

# Adding elements to the queue   
def enqueue(queue,member_no,member_namestring,age):
    queue.append(member_no)
    queue.append(member_namestring)
    queue.append(age)

# removing item from the queue
def dequeue(queue):
    if isqueueEmpty(queue):
        print("queue is empty")
    else:
        item = queue.pop(0)
        print("The element popped: " + str(item))

# Display the contents of the queue
def display(queue):
    if isqueueEmpty(queue):
        print("queue is empty")
    else:
        front = 0
        rear = len(queue)-1
        for i in range(front,rear + 1):
            print(queue[i],end=' ')
            print()
        


# Executable code
if name == "main" :
    a =[]
    display(a)

    enqueue(a,12501,"Kunal sharma",17)
    enqueue(a,12516,"Aman sharma",17)
    enqueue(a,12519,"Vaibhav sharma",17)
    enqueue(a,12521,"Ketan Anand",17)
    enqueue(a,12522,"Himanshu Jha",17)
    display(a)
    
    dequeue(a)
    dequeue(a)
    dequeue(a)
    

    display(a)
    

    dequeue(a)
    dequeue(a)
    dequeue(a)

    display(a)
## code after execution::                                                                                                                       queue is empty
Kunal sharma 
Aman sharma 
Vaibhav sharma 
Ketan Anand 
Himanshu Jha 
The element popped: 12501
The element popped: Kunal sharma
The element popped: 17
Aman sharma 
Vaibhav sharma 
Ketan Anand 
Himanshu Jha 
The element popped: 12516
The element popped: Aman sharma
The element popped: 17
Vaibhav sharma 
Ketan Anand 
Himanshu Jha 
C (graphite)    + 1/2 O2    ⇌   CO
at 25° C and 1 atm, ΔH  = -110525 J. What is ΔE, if the molar volume of graphite is 0.0053 L?

class PyQueue :
    
    def __init__(self,fields) :
        if type(fields)==list :
            self.queue=[]
            self.queuefields=[]
            if len(fields)!=0 :                
                for field in fields :
                    self.queuefields.append(field)
            else :
                self.queuefields=["Test1"]
        else :
            raise NameError(f"{fields} :  __Invalid Fields type__ Entered in PyQueue Implementation .")
    
    def isPyQueue(collection) :
        result=None
        if type(collection)==PyQueue :
            result=True
        else :
            result=False
        
        return result
    
    def QueueSize(self) :
        return len(self.queue)
        
    
    def isQueueEmpty(self) :
        result=None 
        if self.QueueSize()==0 :
            result=True
        else :
            result=False
            
        return result
    
    def QueueFields(self) :
        return self.queuefields
        
    def Enqueue(self,item) :
        if type(item)==list :
            if len(self.queuefields)==len(item) :
                entry={}
                for i in range(1,len(self.queuefields)+1) :
                    entry[self.queuefields[i-1]]=item[i-1]
                self.queue.insert(0,entry)
            else :
                raise InputError(f":: 2 :: {item} Items are {len(items)} More than {self.Queue} Items {self.QueueSize()}")
        else :
            raise InputError(f":: 1 :: {item} type {type(item)} : Invalid Input .")
            
    def Dequeue(self) :
        if self.isQueueEmpty()==False :
            self.queue.pop(0)
        else :
            print(f"EmptyQueueError : {self.queue} Empty Queue .")
    
    def QueueCopy(self) :
        result=self.queue[:]
        return Queue(result)
        
    def QueueDisplayVertical(self) :
        print()
        print("•|•|"*8)
        print()
        
        print(f"\t\t  ____CONSUMER 🚀 END____ ")
        print()
        print("_"*60)
        print()
        for i in self.queuefields :
            print(i,end="\t         ")
        print()
        print()
        
        for k in range(self.QueueSize()) :
            print("-"*60)
            print(f"\t\t\t--QUEUE ENTRY {k+1}--")
            for j in self.queue[k].values() :
                print(f" __{j}__ ",end=" -- ")
            print("-"*56)
        print()
        print("_"*60)
        print()
        print(f"\t\t  ____PRODUCER 🎉 END____ ")
        print()
        print("•|•|"*8)
        print()
  
-_----__--__Output__--____---



•|•|•|•|•|•|•|•|•|•|•|•|•|•|•|•|

                  ____CONSUMER 🚀 END____

____________________________________________________________
Company          PODUCT          Price           Rating     

------------------------------------------------------------                        --QUEUE ENTRY 1--
 __Applex__  --  __Ixphone__  --  __x1opn90__  --  __5.0__  -- --------------------------------------------------------

____________________________________________________________
                  ____PRODUCER 🎉 END____

•|•|•|•|•|•|•|•|•|•|•|•|•|•|•|•|

from queuePython import PyQueue

queue1=PyQueue(fields=["Company","PODUCT","Price","Rating"])

print(queue1)

queue1.Enqueue(item=["Applex","Ixphone","x1opn90","5.0"])

queue1.QueueDisplayVertical()

print(queue1.isQueueEmpty())
(1) Insert a record in the queue
(2) Delete a record from the queue
(3) Display the waiting list
Implement record as a list containing following fields.
Waiting_no   			Integer
(b)   R (2 π – 1) θ  / (4 π2)
(c)  R (2π – θ) / (4 π)
(d) R θ  / (2 π)
(2.0 atm, 3.0 L, 95 K) →(4.0 atm, 5.0 L, 245 K) with a change in internal energy, ΔU=30.0 Latm. The change in enthalpy ΔH of the process in L atm is:
a) 40.0
b) 42.3
c) 44.0
d) Not defined because pressure is not constant
(b)   R (2 π – 1) θ  / (4 π2)
(c)  R (2π – θ) / (4 π)
(d) R θ  / (2 π)

# module2.py

# A Module For

#A menu driven program in Python that allows the following operations on a 
# Queue of waiting list:
# (1) Insert a record in the queue
# (2) Delete a record from the queue
# (3) Display the waiting list
# Implement record as a list containing following fields.
# Waiting_no   			Integer
# Passenger_name 		String
# Passenger_age			Integer
# Passenger_gender		Character (‘M’ or ‘F’)



# Checks If Queue Is Empty
def isQueueEmpty(queue) :
	
	if len(queue) == 0 :
	    return True
	    
	else :
	    return False


# Enqueue The Item At Last Of Queue
def enqueue(queue) :
    
    waiting_no = input("Enter The Waiting Number [Default : Autoincrement] :\t")
    passenger_name = input("Enter Passenger Name :\t")
    passanger_age = int(input("Enter Passanger Age :\t"))
    passanger_gender = input("Enter Passanger Gender [M / F] :\t")
    passanger_gender = passanger_gender.upper()
    print()
    
    if ( (len(waiting_no) == 0) and isQueueEmpty(queue) ) :
        
        waiting_no = 1
        
    elif (len(waiting_no) == 0) :
        
        waiting_no = queue[-1][0]  + 1
        
        
    data = (int(waiting_no) , passenger_name , passanger_age , passanger_gender)
    
    queue.append(data)
        
# Dequeue The Item From Starting Of Queue
def dequeue(queue) :
    
    if isQueueEmpty(queue) :
        
        print("Queue is empty")
        print()
        
    else :
        
        print(f"{queue.pop(0)} is dequeued from the Queue")
        print()
        

# Display The Queue
def display(queue) :
    
    print("_" * 65)
    print("Waiting_no\tPassenger_name\tPassenger_age\tPassenger_gender")
    print("_" * 65)
    
    for member in queue :
        
        for i in range(len(member)) :
            
            print(member[i] , end = "\t\t")
            
        print()
    
    print("_" * 65)    
    print()
        
        

# prg2.py

#A menu driven program in Python that allows the following operations on a 
# Queue of waiting list:
# (1) Insert a record in the queue
# (2) Delete a record from the queue
# (3) Display the waiting list
# Implement record as a list containing following fields.
# Waiting_no   			Integer
# Passenger_name 		String
# Passenger_age			Integer
# Passenger_gender		Character (‘M’ or ‘F’)


import module2

Q = []

# Shows Basic Commands available
def helper() :
    
    print("(1) Insert a record in the queue")
    print("(2) Delete a record from the queue")
    print("(3) Display the waiting list")
    print()
    
# Prompt Of Menu
def prompt() :
    HEADER = '\033[95m'
    print(f"{HEADER}\\h for help \\q for quit")
    color_yellow = '\033[93m'
    
    while True :
        
        command = input(f"{color_yellow}IRCTC/DataBase/Counter_3/Queue $\t")
        
        if command == "1" :
            
            module2.enqueue(Q)
            
        elif command == "2" :
            
            module2.dequeue(Q)
            
        elif command == "3" :
            
            module2.display(Q)
            
        elif command == "\h" :
            
            helper()
            
        elif command == "\q" :
            
            break
            
        else :
            
            WARNING = '\033[91m'
            
            print(f"{WARNING}Invalid Command")

# Driver Code            
if __name__ == "__main__" :
    
    prompt()
North	
G9-G10	https://bit.ly/3hYRgGH
G11-G12	https://bit.ly/3jZ8O7H
DISPLAY(stack)
where city_name is name of a city.
(a) 50 Ω
(b) 100 Ω
(c) 200 Ω
(d) 400 Ω
(b) +125 kJ
(c) -125  kJ
(d) +250 kJ


So at r=8cm
It will be 10 cm^2/ min .

Issi liye aabhi part 1 hi solve Kiya hai jab Sikh jaunga tab aage Ka attempt Kar lunga

Regards : Kunal Sharma (12501)
Roll no. 12528
------------

•••• Enter **City Stack** Command : - : - 6

StackEmptyError : T2 : [] is an Empty Stack ..

•••• Enter **City Stack** Command : - : - 1


                 ENTER CITY DETAILS __>>

Enter City Name :       Delhi
Enter City Number (Or Self increment ) :

 City : ['Delhi', 1]     Successfully Inserted In stack .

•••• Enter **City Stack** Command : - : - 1


                 ENTER CITY DETAILS __>>

Enter City Name :       Mumbai
Enter City Number (Or Self increment ) : 3

 City : ['Mumbai', 3]    Successfully Inserted In stack .

•••• Enter **City Stack** Command : - : - 3


____________________________________________________________
-------------------- Tue Aug  4 21:33:37 2020 --------------____________________________________________________________
              |•|•|•|•____City  Stack____•|•|•|•|

:::::::::::: •••••••••••• CityStackTop :::::::::: ••••••••••
Fields : -       CityNumber      City

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 1 •      3           Mumbai
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 2 •      1           Delhi

************** •••••••••• City  Stack  End   **************



•••• Enter **City Stack** Command : - : - 4

Stack : [{'Mumbai': 3}, {'Delhi': 1}]
 is Filled Stack .
 Places filled : 2

•••• Enter **City Stack** Command : - : - 5

[{'Mumbai': 3}, {'Delhi': 1}] is Valid And
.    A filled stack to 2 places .

•••• Enter **City Stack** Command : - : - 6


                Raw  Stack


[{'Mumbai': 3}, {'Delhi': 1}]


•••• Enter **City Stack** Command : - : - 2

Successfully Completed :         city    [{'Mumbai': 3}]

•••• Enter **City Stack** Command : - : - 1


                 ENTER CITY DETAILS __>>

Enter City Name :       Chennai
Enter City Number (Or Self increment ) :

 City : ['Chennai', 3]   Successfully Inserted In stack .

•••• Enter **City Stack** Command : - : - 1


                 ENTER CITY DETAILS __>>

Enter City Name :       Kolkata
Enter City Number (Or Self increment ) :

 City : ['Kolkata', 4]   Successfully Inserted In stack .

•••• Enter **City Stack** Command : - : - 1


                 ENTER CITY DETAILS __>>

Enter City Name :       New york City
Enter City Number (Or Self increment ) : 5

 City : ['New york City', 5]     Successfully Inserted In stack .

•••• Enter **City Stack** Command : - : - 1


                 ENTER CITY DETAILS __>>

Enter City Name :       Sri Nagar
Enter City Number (Or Self increment ) :

 City : ['Sri Nagar', 6]         Successfully Inserted In stack .

•••• Enter **City Stack** Command : - : - 3


____________________________________________________________
-------------------- Tue Aug  4 21:35:12 2020 --------------____________________________________________________________
              |•|•|•|•____City  Stack____•|•|•|•|

:::::::::::: •••••••••••• CityStackTop :::::::::: ••••••••••
Fields : -       CityNumber      City

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 1 •      6           Sri Nagar
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 2 •      5           New york City
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 3 •      4           Kolkata
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 4 •      3           Chennai
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 5 •      1           Delhi

************** •••••••••• City  Stack  End   **************



•••• Enter **City Stack** Command : - : - 2

Successfully Completed :         city    [{'Sri Nagar': 6}]

•••• Enter **City Stack** Command : - : - 2

Successfully Completed :         city    [{'New york City': 5}]

•••• Enter **City Stack** Command : - : - 3


____________________________________________________________
-------------------- Tue Aug  4 21:35:22 2020 --------------____________________________________________________________
              |•|•|•|•____City  Stack____•|•|•|•|

:::::::::::: •••••••••••• CityStackTop :::::::::: ••••••••••
Fields : -       CityNumber      City

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 1 •      4           Kolkata
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 2 •      3           Chennai
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 3 •      1           Delhi

************** •••••••••• City  Stack  End   **************



•••• Enter **City Stack** Command : - : - 2

Successfully Completed :         city    [{'Kolkata': 4}]

•••• Enter **City Stack** Command : - : - 2

Successfully Completed :         city    [{'Chennai': 3}]

•••• Enter **City Stack** Command : - : - 3


____________________________________________________________
-------------------- Tue Aug  4 21:35:31 2020 --------------____________________________________________________________
              |•|•|•|•____City  Stack____•|•|•|•|

:::::::::::: •••••••••••• CityStackTop :::::::::: ••••••••••
Fields : -       CityNumber      City

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - stackdata : 1 •      1           Delhi

************** •••••••••• City  Stack  End   **************



•••• Enter **City Stack** Command : - : - 4

Stack : [{'Delhi': 1}]
 is Filled Stack .
 Places filled : 1

•••• Enter **City Stack** Command : - : - 5

[{'Delhi': 1}] is Valid And
.    A filled stack to 1 places .

•••• Enter **City Stack** Command : - : - 6


                Raw  Stack


[{'Delhi': 1}]


•••• Enter **City Stack** Command : - : - 2

Successfully Completed :         city    [{'Delhi': 1}]

•••• Enter **City Stack** Command : - : - 3

StackError : 2 : [] is Empty Stack .

•••• Enter **City Stack** Command : - : - 4

Stack : [] is An Empty stack .

•••• Enter **City Stack** Command : - : - 5

[] is Valid Stack  .

•••• Enter **City Stack** Command : - : - 6

StackEmptyError : T2 : [] is an Empty Stack ..

•••• Enter **City Stack** Command : - : - 1


                 ENTER CITY DETAILS __>>

Enter City Name :
"""

Write a menu driven program in Python that allows the following operations of a stack:
DISPLAY(stack)
where city_name is name of a city.

"""
import time as t

citystack=[]


def isstack(stack) :
    if type(stack)==list :
        result=[True,2]
        if len(stack)!=0 :
            result=[True,3]
            if type(stack[0])==dict :
                result=[True,4]
            else :
                pass
        else :
            pass
    else :
        result=[False,1]
    return result
    
def stackraw(stack,aligned=False) :
    print()
    print(" "*15,"Raw  Stack ")
    print()
    print()
    if aligned==False :
        print(stack)
    elif aligned==True :
        for p in stack :
            print(p)
    print()
    
def isstackempty(stack) :
    result=None
    if type(stack)==list :
        if len(stack)==0 :
            result=True
        else :
            result=False        
    else :
        print(f"StackError : {stack} is invalid for __-isstackempty-__ operation .")
    return result

def StackPush(stack,cityName=["Testcity1",0]) :
    if isstack(stack)[0]==True :
        if isstack(stack)[1] in [2,3,4] :
            if isstackempty(stack)==True or isstackempty(stack)==False :
                if type(cityName)==list :
                    if len(cityName)!=0 :
                        if type(cityName[0])==str :
                            if type(cityName[1])==int:
                                Entry={cityName[0]:cityName[1]}
                                citystack.insert(0,Entry)
                            else :
                                print(f"•StackEntryitemError : 7 : For City Number it should INTEGER . \n As cityName should cityName=[str(Name of city), int(City Number)]")
                        else :
                            print(f"•StackEntryitemError : 6 : For City StackEntry  {cityName} should be cityName=[str(Name of city), int(City Number)]")
                    else :
                        print("~StackEntryError : 5 : {cityName} should be of two order . ")
                else :
                    print(f"|StackEntryError : 4 : {cityName} should be a python list \n Of The type : cityName=[str(Name of city), int(City Number)]")
            else :
                print(f"|StackEmptyError : 3 : {stack} is An Empty Stack . ")
        else :
            print(f"~StackError : 2 : {stack} is Empty stack .")
    else :
        print(f"-StackError : 1 : {stack} \n is Invalid Specific stack .")
                
def StackPop(stack) :
    if isstack(stack)[0]==True :
        if isstack(stack)[1] in [3,4] :
            citystack.pop(0)
        else :
            print(f"")
    else :
        print(f"")

def StackDisplay(stack) :
    if isstack(stack)[0]==True :
        if isstack(stack)[1] in [3,4] :
            prtime=t.ctime()
            print()
            print("_"*60)
            print()
            print("-"*20,prtime,"-"*int(38-len(str(prtime))))
            print("_"*60)
            print()
            space1=" "*12
            print(f"{space1}  |•|•|•|•____City  Stack____•|•|•|•|")
            print()
            print(":"*12,"•"*12,"CityStackTop",":"*10,"•"*10)
            
            print()
            print(f"Fields : - \t CityNumber \t City ")
   
            print()
            stackdata=0
            space2=" "*11
            for i in stack :
                print("- "*30)
                stackdata+=1
                for j,k in i.items() :
                    
                    print(f"stackdata : {stackdata} •      {k}{space2}{j}")
            print("")
            print("*"*14,"•"*10,"City  Stack  End  ","*"*14)
            print("")
            print("")
        else :
            print(f"StackError : 2 : {stack} is Empty Stack . ")
    else :              
        print(f"StackError : 1 : {stack} is Specific Invalid Stack . ")
            
            
   
all=1
CityAutoNum=0
while all>=1 :
    order=input(f"•••• Enter **City Stack** Command : - : - ")
    order=str(order.lower()).strip()
    
    if order=="1" or order=="insert" or order=="push" or order=="add" or order=="enstack" :
        print()
        print(f"\n\t\t ENTER CITY DETAILS __>>\n")
        cityName=input("Enter City Name : \t")
        CityAutoNum+=1
        cityNum=input("Enter City Number (Or Self increment ) : ")
        if str(cityNum).strip()=="" :
            cityNum=CityAutoNum
        else :
            cityNum=int(cityNum)
        stackentry=[cityName,cityNum]
        StackPush(citystack,stackentry)
        print("\n",f"City : {stackentry} \t Successfully Inserted In stack . ")
        print()
                       
    elif order=="2" or order=="delete" or order=="pop" or order=="remove" or order=="destack" :
        print()
        stackdel=citystack[:1]
        StackPop(citystack)
        print(f"Successfully Completed : \t city \t {stackdel}")
        print()
        
    elif order=="3" or order=="show" or order=="display" or order=="present" :
        print()
        StackDisplay(citystack)
        print()
        
    elif order=="4" or order=="empty" or order=="check" or order=="displayable" :
        print()
        if isstackempty(citystack)==True :
            print(f"Stack : {citystack} is An Empty stack .")
        else :
            print(f"Stack : {citystack} \n is Filled Stack . \n Places filled : {len(citystack)}")
        print() 
        
    elif order=="5" or order=="validity" or order=="checkin" or order=="insertable" :
        print()    
        validity=isstack(citystack)
        if validity[0]==True and validity[1]==2 :
            print(f"{citystack} is Valid Stack  .")
            print()    
        elif validity[0]==True and validity[1]==3 :
            print(f"{citystack} is Valid And \n.    An Empty stack .")
            print()    
        elif validity[0]==True and validity[1]==4 :
            print(f"{citystack} is Valid And \n.    A filled stack to {len(citystack)} places .")
            print()    
        elif validity[0]==False and validity[1]==1 :
            print(citystack , "is Invalid Stack .")
            print()    
        else :
            print("Technical error : Due to some reasons program connection failed .")
            print(f" ")    
            break
    elif order=="6" or order=="rawstack" or order=="stackraw" or "stackelements" or order=="cities" :
        print()
        if isstack(citystack)[0]==True :
            if isstackempty(citystack)==False :
                stackraw(citystack)
            else :
                print(f"StackEmptyError : T2 : {citystack} is an Empty Stack ..")
        else :
            print(f"StackError : T1 : {citystack} is not an stack .")
        print()
        
              
    else :
        print(f""" \nUser , Command : {order} is Invalid \n For Specific City Stack Program ....       
        """)
It's a Stack Implementing program for city Encoding \n In a stack.
             
 For Commands Working : 
     Use Commands :
                 
     1 ). To insert an entry in City Stack .
                 
         Commands : 1 , insert , push , add , enstack
                     
     2 ).To delete an entry in City Stack .
                
         Commands : 2 , delete , pop , remove , destack
                     
     3 ).To display our stack .
                 
         Commands : 3 , show , display , prsent
                     
     4 ).To Check if City Stack at moment Empty or not .
                 
         Commands : 4 , Empty , check , displayable
                     
     5 ).To check if City Stack validity upto a level .
                 
         Commands : 5 , validity , checkin , insertable 
                     
     6 ).To display City Stcak in raw form .
                 
         Commands : 6 , rawstack , stackraw , stackelements , cities
                     
     else :
                     Program will specify an error .
Roll no. 12509
Roll no. 12520
Vivek kumar

D:\>mysql -u user1 -h localhost -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> create database southwind;
Query OK, 1 row affected (0.06 sec)

mysql> drop database southwind;
Query OK, 0 rows affected (0.43 sec)

mysql> create database if not exists southwind;
Query OK, 1 row affected (0.01 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> drop database if exists southwind;
Query OK, 0 rows affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> drop database southwind;
ERROR 1008 (HY000): Can't drop database 'southwind'; database doesn't exist
mysql> drop database if exists southwind;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> create database southwind;
Query OK, 1 row affected (0.01 sec)

mysql>
mysql>
mysql> show create database southwind;
+-----------+----------------------------------------------------------------------+
| Database  | Create Database                                                      |
+-----------+----------------------------------------------------------------------+
| southwind | CREATE DATABASE `southwind` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+-----------+----------------------------------------------------------------------+

mysql>


mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> use southwind;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| southwind  |
+------------+

mysql> use mysql;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| mysql      |
+------------+

mysql> use southwind;
Database changed
mysql> show tables;
Empty set (0.03 sec)

mysql> CREATE TABLE IF NOT EXISTS products (
    ->          productID    INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    ->          productCode  CHAR(3)       NOT NULL DEFAULT '',
    ->          name         VARCHAR(30)   NOT NULL DEFAULT '',
    ->          quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
    ->          price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99,
    ->          PRIMARY KEY  (productID)
    ->        );
Query OK, 0 rows affected (0.87 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql>
(a) R/2
(b) R/3
(c) 6 R
(d) 2 R
(a) 59.54 J/mol
(b) 5954 J/mol
(c) 595.4 J/mol
(d) 320.6 J/mol
(c) 2019 Microsoft Corporation. All rights reserved.

D:\WINDOWS\system32>cd \

D:\>start /b mysqld

D:\>mysql -u user1 -h localhost   -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> select database();
+------------+
| database() |
+------------+
| NULL       |
+------------+

mysql> use southwind;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| southwind  |
+------------+

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
+-------------+------------------+------+-----+----------+----------------+

mysql> select * from products;
Empty set (0.03 sec)

mysql> INSERT INTO products VALUES (1001, 'PEN', 'Pen Red', 5000, 1.23);
Query OK, 1 row affected (0.16 sec)

mysql> select * from products;
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql> INSERT INTO products VALUES
    ->          (NULL, 'PEN', 'Pen Blue',  8000, 1.25),
    ->          (NULL, 'PEN', 'Pen Black', 2000, 1.25);
Query OK, 2 rows affected (0.06 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> INSERT INTO products (productCode, name, quantity, price) VALUES
    ->          ('PEC', 'Pencil 2B', 10000, 0.48),
    ->          ('PEC', 'Pencil 2H', 8000, 0.49);
Query OK, 2 rows affected (0.04 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> INSERT INTO products (productCode, name) VALUES ('PEC', 'Pencil HB');
Query OK, 1 row affected (0.03 sec)

mysql> select * from products;
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1001 | PEN         | Pen Red   |     5000 |     1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |     1.25 |
|      1003 | PEN         | Pen Black |     2000 |     1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> INSERT INTO products values (NULL, NULL, NULL, NULL, NULL);
ERROR 1048 (23000): Column 'productCode' cannot be null
mysql>
(a) will decrease by 0.2 %
(b) will increase by 0.5 %
(c) will decrease by 0.05 %
(d) will increase by 0.2%

a)            3, 13

b)            4, 12

c)            6, 10

d)            8, 8

a) - 44 kcal

b) 44 kcal

c) - 22 kcal

d) 22 kcal

Δf​H(HCl)​=ΔH(Rea)−ΔH(Pro)=0.5​(104)+0.5​(58)−103=−22 kcal.
mysql> use southwind;
Database changed
mysql>
mysql> select * from products;
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1001 | PEN         | Pen Red   |     5000 |     1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |     1.25 |
|      1003 | PEN         | Pen Black |     2000 |     1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select productID, productCode from products;
+-----------+-------------+
| productID | productCode |
+-----------+-------------+
|      1001 | PEN         |
|      1002 | PEN         |
|      1003 | PEN         |
|      1004 | PEC         |
|      1005 | PEC         |
|      1006 | PEC         |
+-----------+-------------+

mysql> select * from products where productCode = 'pec';
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select * from products where productCode = "pec";
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> select * from Products where productCode = "pec";
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select * from Products where productCode = "pec"  and price < 2.0;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> select * from Products where productCode = "pec"  and price < 2.0 and quantity > 8000;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> select productID, productCode, quantity
    -> from products
    -> where name like "Pencil%"  or quantity >= 8000;
+-----------+-------------+----------+
| productID | productCode | quantity |
+-----------+-------------+----------+
|      1002 | PEN         |     8000 |
|      1004 | PEC         |    10000 |
|      1005 | PEC         |     8000 |
|      1006 | PEC         |        0 |
+-----------+-------------+----------+

mysql> DELETE FROM products WHERE productID = 1006;
Query OK, 1 row affected (0.16 sec)

mysql> select * from Products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT name, price FROM products;
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> select * from Products group by productCode;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'southwind.Products.productID' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql>
mysql>
mysql>
mysql> select productCode, max(quantity), min(quantity) from Products group by productCode;
+-------------+---------------+---------------+
| productCode | max(quantity) | min(quantity) |
+-------------+---------------+---------------+
| PEC         |         10000 |          8000 |
| PEN         |          8000 |          2000 |
+-------------+---------------+---------------+

mysql>
mysql>
mysql> select productCode, max(quantity), min(quantity)
    -> from products
    -> group by productCode
    -> having productCode = 'PEN';
+-------------+---------------+---------------+
| productCode | max(quantity) | min(quantity) |
+-------------+---------------+---------------+
| PEN         |          8000 |          2000 |
+-------------+---------------+---------------+

mysql>
mysql> select productCode, sum(price)
    -> from products
    -> group by productCode;
+-------------+------------+
| productCode | sum(price) |
+-------------+------------+
| PEC         |       0.97 |
| PEN         |       3.73 |
+-------------+------------+

mysql> select productCode, avg(price)
    -> from products
    -> group by productCode;
+-------------+------------+
| productCode | avg(price) |
+-------------+------------+
| PEC         |   0.485000 |
| PEN         |   1.243333 |
+-------------+------------+

mysql> select productCode, count(*)
    -> from products
    -> group by productCode;
+-------------+----------+
| productCode | count(*) |
+-------------+----------+
| PEC         |        2 |
| PEN         |        3 |
+-------------+----------+

mysql> select name, count(*)
    -> from products
    -> group by name;
+-----------+----------+
| name      | count(*) |
+-----------+----------+
| Pen Black |        1 |
| Pen Blue  |        1 |
| Pen Red   |        1 |
| Pencil 2B |        1 |
| Pencil 2H |        1 |
+-----------+----------+

mysql> select quantity, count(*)
    -> from products
    -> group by quantity;
+----------+----------+
| quantity | count(*) |
+----------+----------+
|     2000 |        1 |
|     5000 |        1 |
|     8000 |        2 |
|    10000 |        1 |
+----------+----------+

mysql> select distinct(quantity)  from products;
+----------+
| quantity |
+----------+
|     5000 |
|     8000 |
|     2000 |
|    10000 |
+----------+

mysql> select all(quantity)  from products;
+----------+
| quantity |
+----------+
|     5000 |
|     8000 |
|     2000 |
|    10000 |
|     8000 |
+----------+

mysql> SELECT name, price FROM products WHERE name LIKE 'P__%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name LIKE 'P___R%';
+---------+-------+
| name    | price |
+---------+-------+
| Pen Red |  1.23 |
+---------+-------+

mysql>
Observe the following PARTICIPANTS and EVENTS table carefully and write the name of the RDBMS operation which will be used to produce the output as shown in RESULT? Also, find the Degree and Cardinality of the RESULT.
Cardinality : 6
 (a) –5 L2 / 2 m/s                 (b) –2 L2 / 5 m/s

(c) –L2 / 2 m/s                   (d) –L2 / 5 m/s
from its atoms is −436 kJ/mol and that of N2 is −712 kJ/mol, then the average bond enthalpy of N−H bond in NH3 is:
(a) -964  kJ /mol
(b) +352 kJ/mol
(c) +1056 kJ/ mol
(d) -1102  kJ/ mol
 Question 1:
Observe the following PARTICIPANTS and EVENTS table carefully and write the name of the RDBMS operation which will be used to produce the output as shown in RESULT? Also, find the Degree and Cardinality of the RESULT.

Degree=4
Cardinality=6
Cartesian product of Two relation PARTICIPANTS and EVNTS or Cross join in SQL .


Degree= Sum of degree of joining tables = 2+ 3= 5

Cardinality = Product of cardinality in joining Tables = 2 * 3 = 6
ii)	What is the cardinality and degree of the above table?


     Degree       : 4 
(Item Code + Item + Qty + Rate )
i) no
ii)degree-4
  Cardinality- 6
    Degree=4
Cardinality -5
 Cardinality: 5
(ii) degree is 4
Cardinality is 5
(i) What is the current of the moving film?
(ii) How long does it take the roller to accumulate a charge of -10 μC?
(a) 6
(b) 3
(c) -6
(d) -3
(a) 5 kJ                           ( b) -110.5 kJ
(c) -676.5 kJ                   (d)  676.5 kJ
     Cardinality = 5

(ii) Cardinality : 5
      Degree : 4

(ii) time = 5000/(12π) s
Current is equal to charge​ that flows in 1 second.

a) Two times
b)  Four times
c)  Eight times                
d) Sixteen times

(a)  π/3

(b)  π/4

(c)  π/6

(d)  π/2
The heat of neutralization is:
	

(a) – 100 X kJ/mol
	

(b) – 50 X kJ/mol
	

(c) + 100 x kJ/mol
	

(d)  +50 X kJ/mol

*Degree : 4*
*Cardinality : 6*

Area will become (1/4) th 
Length will become 4 times 

Hence , Resistance will become Sixteen times of intial resistance


https://t.me/joinchat/QGt00ENWYYMajzVwsyokxw
*Class 11-Class 12*
*10-Aug to 15-Aug*
EMC- - https://bit.ly/2DxHLja
       Degree : 5
       Cardinality of table :4
    Degree : 6
    Cardinality : 7
    Cardinality- 4

    Cardinality-7
    Cardinality : 4

     New Cardinality : 7

Vikas , 12508
    Cardinality - 4
    Cardinality - 7
Roll no. 12520
Roll no. 12523
+-----------+-------+
| name      | price |
+-----------+-------+
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, quantity FROM products WHERE quantity <= 2000;
+-----------+----------+
| name      | quantity |
+-----------+----------+
| Pen Black |     2000 |
+-----------+----------+

mysql> SELECT name, price FROM products WHERE productCode = 'PEN';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name LIKE 'PENCIL%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'Pen%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'pen%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'pen %';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
+-----------+-------+

mysql> SELECT * FROM products WHERE quantity >= 5000 AND name LIKE 'Pen %';
+-----------+-------------+----------+----------+-------+
| productID | productCode | name     | quantity | price |
+-----------+-------------+----------+----------+-------+
|      1001 | PEN         | Pen Red  |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue |     8000 |  1.25 |
+-----------+-------------+----------+----------+-------+

mysql> * FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '* FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %'' at line 1
mysql> select * FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %';
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql>
mysql>
mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE NOT (quantity >= 5000 AND name LIKE 'Pen %');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE  quantity >= 5000 AND name LIKE 'Pen %';
+-----------+-------------+----------+----------+-------+
| productID | productCode | name     | quantity | price |
+-----------+-------------+----------+----------+-------+
|      1001 | PEN         | Pen Red  |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue |     8000 |  1.25 |
+-----------+-------------+----------+----------+-------+

mysql> SELECT * FROM products WHERE  quantity < 5000 OR name NOT LIKE 'Pen %';
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql>
Attendance for: Class List on 2020-08-11

Names	2020-08-11 	Arrival time
vikas 210	?	10:46	11:15
md irfan	?	10:47
suraj shukla	?	10:47
samrat chhabra	?	10:47
aman sharma	?	10:47
himanshu jha	?	10:47
kirti bisht	?	10:47
simran rawat	?	10:47	11:05
âmâñ âñsârî	?	10:47	11:00
supreet singh	?	10:47
deepanshu kumar	?	10:47
himanshi sharma	?	10:47
ketan anand	?	10:47	10:49	11:01	11:02	11:05
pawan joshi	?	10:48	11:10
kunal sharma	?	10:48
vishal kumar	?	10:48	11:06	11:07
vivek kumar	?	10:48	11:14
sahzad hussain	?	10:50
badshah rehman	?	10:50
akshay sharma	?	10:51
rahul kumar	?	10:53	11:08
ashish raj singh	?	10:54
Shubham Kumar	?	10:54
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name NOT IN ('Pen Red', 'Pen Black');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name NOT IN ('Pen Red', 'Pen Black'); select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products
    ->        WHERE (price BETWEEN 1.0 AND 2.0) AND (quantity BETWEEN 1000 AND 2000);
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE productCode IS NULL;
Empty set (0.07 sec)

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price ;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price ASC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC, quantity;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY price LIMIT 2;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY price LIMIT 2, 1;
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql> SELECT * FROM products ORDER BY price;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT productID AS ID, productCode AS Code,
    ->               name AS Description, price AS 'Unit Price'
    ->        FROM products
    ->        ORDER BY ID;
+------+------+-------------+------------+
| ID   | Code | Description | Unit Price |
+------+------+-------------+------------+
| 1001 | PEN  | Pen Red     |       1.23 |
| 1002 | PEN  | Pen Blue    |       1.25 |
| 1003 | PEN  | Pen Black   |       1.25 |
| 1004 | PEC  | Pencil 2B   |       0.48 |
| 1005 | PEC  | Pencil 2H   |       0.49 |
+------+------+-------------+------------+

mysql>  select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> select * , price * 0.10 AS Discount from products;
+-----------+-------------+-----------+----------+-------+----------+
| productID | productCode | name      | quantity | price | Discount |
+-----------+-------------+-----------+----------+-------+----------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |   0.1230 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |   0.1250 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |   0.1250 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |   0.0480 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |   0.0490 |
+-----------+-------------+-----------+----------+-------+----------+

mysql>
mysql>
mysql> SELECT price FROM products;
+-------+
| price |
+-------+
|  1.23 |
|  1.25 |
|  1.25 |
|  0.48 |
|  0.49 |
+-------+

mysql> SELECT DISTINCT price AS 'Distinct Price' FROM products;
+----------------+
| Distinct Price |
+----------------+
|           1.23 |
|           1.25 |
|           0.48 |
|           0.49 |
+----------------+

mysql> SELECT DISTINCT price FROM products;
+-------+
| price |
+-------+
|  1.23 |
|  1.25 |
|  0.48 |
|  0.49 |
+-------+

mysql> SELECT DISTINCT price, name from Products;
+-------+-----------+
| price | name      |
+-------+-----------+
|  1.23 | Pen Red   |
|  1.25 | Pen Blue  |
|  1.25 | Pen Black |
|  0.48 | Pencil 2B |
|  0.49 | Pencil 2H |
+-------+-----------+

mysql> SELECT price, name from Products;
+-------+-----------+
| price | name      |
+-------+-----------+
|  1.23 | Pen Red   |
|  1.25 | Pen Blue  |
|  1.25 | Pen Black |
|  0.48 | Pencil 2B |
|  0.49 | Pencil 2H |
+-------+-----------+

mysql> SELECT DISTINCT productCode, price, name from Products;
+-------------+-------+-----------+
| productCode | price | name      |
+-------------+-------+-----------+
| PEN         |  1.23 | Pen Red   |
| PEN         |  1.25 | Pen Blue  |
| PEN         |  1.25 | Pen Black |
| PEC         |  0.48 | Pencil 2B |
| PEC         |  0.49 | Pencil 2H |
+-------------+-------+-----------+

mysql> SELECT DISTINCT productCode, price from Products;
+-------------+-------+
| productCode | price |
+-------------+-------+
| PEN         |  1.23 |
| PEN         |  1.25 |
| PEC         |  0.48 |
| PEC         |  0.49 |
+-------------+-------+

mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY productCode, productID;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products GROUP BY productCode;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'southwind.products.productID' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
mysql>
mysql>
mysql> SELECT productCode, COUNT(*) FROM products GROUP BY productCode;
+-------------+----------+
| productCode | COUNT(*) |
+-------------+----------+
| PEC         |        2 |
| PEN         |        3 |
+-------------+----------+

mysql> SELECT productCode, COUNT(*) AS count
    ->        FROM products
    ->        GROUP BY productCode
    ->        ORDER BY count DESC;
+-------------+-------+
| productCode | count |
+-------------+-------+
| PEN         |     3 |
| PEC         |     2 |
+-------------+-------+

mysql> SELECT productCode, MAX(price) AS 'Highest Price', MIN(price) AS 'Lowest Price'
    ->        FROM products
    ->        GROUP BY productCode;
+-------------+---------------+--------------+
| productCode | Highest Price | Lowest Price |
+-------------+---------------+--------------+
| PEC         |          0.49 |         0.48 |
| PEN         |          1.25 |         1.23 |
+-------------+---------------+--------------+

mysql> SELECT productCode, MAX(price), MIN(price),
    ->               CAST(AVG(price) AS DECIMAL(7,2)) AS 'Average,
    '>               CAST(STD(price) AS DECIMAL(7,2)) AS 'Std Dev',
    '>               SUM(quantity)
    '>        FROM products
    '>
    '>
    '> ;
    '> ;
    '>
    '>
    '> ;
    '> ^C
mysql>
mysql>
mysql>
mysql> SELECT productCode, MAX(price), MIN(price),
    ->               CAST(AVG(price) AS DECIMAL(7,2)) AS 'Average',
    ->               CAST(STD(price) AS DECIMAL(7,2)) AS 'Std Dev',
    ->               SUM(quantity)
    ->        FROM products
    ->        GROUP BY productCode;
+-------------+------------+------------+---------+---------+---------------+
| productCode | MAX(price) | MIN(price) | Average | Std Dev | SUM(quantity) |
+-------------+------------+------------+---------+---------+---------------+
| PEC         |       0.49 |       0.48 |    0.49 |    0.01 |         18000 |
| PEN         |       1.25 |       1.23 |    1.24 |    0.01 |         15000 |
+-------------+------------+------------+---------+---------+---------------+

mysql>
mysql>
mysql> SELECT
    ->           productCode AS 'Product Code',
    ->           COUNT(*) AS 'Count',
    ->           CAST(AVG(price) AS DECIMAL(7,2)) AS 'Average'
    ->        FROM products
    ->        GROUP BY productCode
    ->        HAVING Count >=3;
+--------------+-------+---------+
| Product Code | Count | Average |
+--------------+-------+---------+
| PEN          |     3 |    1.24 |
+--------------+-------+---------+

mysql>
Enter password: *******
productCode     MAX(price)      MIN(price)      Average Std Dev SUM(quantity)

D:\mysql>mysql -u user1 -h localhost southwind -p  < abc.txt > result.csv
Enter password: *******

D:\mysql>type result.csv
productCode     MAX(price)      MIN(price)      Average Std Dev SUM(quantity)
•	PERKS is Freight Charges per kilometer.
•	Km is kilometers Travelled
•	NOP is number of passangers travelled in vechicle.
i.	To display CNO, CNAME, TRAVELDATE from the table TRAVEL in descending order of CNO.
ii.	To display the CNAME of all customers from the table TRAVEL who are travelling by vechicle with code Vo1 or Vo2
iii.	To display the CNO and CNAME of those customers from the table TRAVEL who travelled between ‘2015-12¬31’ and ‘2015-05-01’.
iv.	To display all the details from table TRAVEL for the customers, who have travel distacne more than 120 KM in ascending order of NOE
v.	SELECT COUNT (*), VCODE FROM TRAVEL GROUP BY VCODE HAVING COUNT (*) > 1;
vi.	SELECT DISTINCT VCODE FROM TRAVEL :
vii.	SELECT A.VCODE, CNAME, VEHICLETYPE FROM TRAVEL A, VEHICLE B WHERE A. VCODE = B. VCODE and KM < 90;
viii.	SELECT CNAME, KM*PERKM FROM TRAVEL A, VEHICLE B WHERE A.VCODE = B.VCODE AND A. VCODE ‘V05’;
(b) 0 A
(c) 0.13 A,  Q to P
(d) 0.13 A , from P to Q
a)Parallelogram

b)Trapezium

c) Square

d)None of these
Database changed
mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> UPDATE products SET quantity = quantity - 100 WHERE name = 'Pen Red';
Query OK, 1 row affected (0.17 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4900 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> UPDATE products SET quantity = quantity + 50, price = 1.27 WHERE name = 'Pen Red';
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4950 |  1.27 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> DELETE FROM products WHERE name LIKE 'Pencil%';
Query OK, 2 rows affected (0.08 sec)

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4950 |  1.27 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> DELETE FROM products;
Query OK, 3 rows affected (0.03 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\>cd mysql

D:\mysql>copy con > products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47
\N,PEC,Pencil 6B,500,0.47
^Z

D:\mysql>type products_in.csv
        1 file(s) copied.

D:\mysql>type products_in.csv
        1 file(s) copied.

D:\mysql>copy con products_in.csv
\N,PEC,Pencil 3B,500,0.52
Overwrite products_in.csv? (Yes/No/All): a
^Z
        1 file(s) copied.

D:\mysql>
D:\mysql>del products_in.csv

D:\mysql>copy con  products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47
^Z
        1 file(s) copied.

D:\mysql>type products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47

D:\mysql>mysql -u user1 -h 127.0.0.1 -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> select * from products;
Empty set (0.01 sec)

mysql> LOAD DATA LOCAL INFILE 'D:/mysql/products_in.csv' INTO TABLE products
    ->          COLUMNS TERMINATED BY ','
    ->          LINES TERMINATED BY '\r\n';
Query OK, 4 rows affected (0.07 sec)
Records: 4  Deleted: 0  Skipped: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1006 | PEC         | Pencil 3B |      500 |  0.52 |
|      1007 | PEC         | Pencil 4B |      200 |  0.62 |
|      1008 | PEC         | Pencil 5B |      100 |  0.73 |
|      1009 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql> delete from products;
Query OK, 4 rows affected (0.04 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\mysql>copy con products_in.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47
^Z
        1 file(s) copied.

D:\mysql>type products_in.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47

D:\mysql>mysqlimport -u user1  -p --local southwind products_in.tsv
Enter password: *******
mysqlimport: Error: 1146, Table 'southwind.products_in' doesn't exist, when using table: products_in

D:\mysql>rename products_in.tsv products.tsv

D:\mysql>type products.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47

D:\mysql>mysqlimport -u user1  -p --local southwind products_in.tsv
Enter password: *******
mysqlimport: Error: 1146, Table 'southwind.products_in' doesn't exist, when using table: products_in

D:\mysql>mysqlimport -u user1  -p --local southwind products.tsv
Enter password: *******
southwind.products: Records: 4  Deleted: 0  Skipped: 0  Warnings: 20

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 7
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> select * from products;
+-----------+-------------+------+----------+-------+
| productID | productCode | name | quantity | price |
+-----------+-------------+------+----------+-------+
|      1013 |             |      |        0 |  0.00 |
|      1014 |             |      |        0 |  0.00 |
|      1015 |             |      |        0 |  0.00 |
|      1016 |             |      |        0 |  0.00 |
+-----------+-------------+------+----------+-------+

mysql> delete from products;
Query OK, 4 rows affected (0.04 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\mysql>type products.tsv
\N      PEC     Pencil  4B      200     0.62
\N      PEC     Pencil  5B      100     0.73
D:\mysql>mysqlimport -u user1  -p --local southwind products.tsv
Enter password: *******
southwind.products: Records: 3  Deleted: 0  Skipped: 0  Warnings: 5

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql> exit
Bye

D:\mysql>type abc.sql
DELETE FROM products;
INSERT INTO products VALUES (2001, 'PEC', 'Pencil 3B', 500, 0.52),
                            (NULL, 'PEC', 'Pencil 4B', 200, 0.62),
                            (NULL, 'PEC', 'Pencil 5B', 100, 0.73),
                            (NULL, 'PEC', 'Pencil 6B', 500, 0.47);
SELECT * FROM products;

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> select * products;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'products' at line 1
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql>
mysql>
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql> source d:/mysql/abc.sql
Query OK, 3 rows affected (0.04 sec)

Query OK, 4 rows affected (0.04 sec)
Records: 4  Duplicates: 0  Warnings: 0

+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql>

D:\>mysql -u user1 -h localhost -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> create database southwind;
Query OK, 1 row affected (0.06 sec)

mysql> drop database southwind;
Query OK, 0 rows affected (0.43 sec)

mysql> create database if not exists southwind;
Query OK, 1 row affected (0.01 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> drop database if exists southwind;
Query OK, 0 rows affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> drop database southwind;
ERROR 1008 (HY000): Can't drop database 'southwind'; database doesn't exist
mysql> drop database if exists southwind;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> create database southwind;
Query OK, 1 row affected (0.01 sec)

mysql>
mysql>
mysql> show create database southwind;
+-----------+----------------------------------------------------------------------+
| Database  | Create Database                                                      |
+-----------+----------------------------------------------------------------------+
| southwind | CREATE DATABASE `southwind` /*!40100 DEFAULT CHARACTER SET latin1 */ |
+-----------+----------------------------------------------------------------------+

mysql>


mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| southwind          |
| sys                |
+--------------------+

mysql> use southwind;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| southwind  |
+------------+

mysql> use mysql;
Database changed
mysql> select database();
+------------+
| database() |
+------------+
| mysql      |
+------------+

mysql> use southwind;
Database changed
mysql> show tables;
Empty set (0.03 sec)

mysql> CREATE TABLE IF NOT EXISTS products (
    ->          productID    INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    ->          productCode  CHAR(3)       NOT NULL DEFAULT '',
    ->          name         VARCHAR(30)   NOT NULL DEFAULT '',
    ->          quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
    ->          price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99,
    ->          PRIMARY KEY  (productID)
    ->        );
Query OK, 0 rows affected (0.87 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+





mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
+-------------+------------------+------+-----+----------+----------------+

mysql> select * from products;
Empty set (0.03 sec)

mysql> INSERT INTO products VALUES (1001, 'PEN', 'Pen Red', 5000, 1.23);
Query OK, 1 row affected (0.16 sec)

mysql> select * from products;
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql> INSERT INTO products VALUES
    ->          (NULL, 'PEN', 'Pen Blue',  8000, 1.25),
    ->          (NULL, 'PEN', 'Pen Black', 2000, 1.25);
Query OK, 2 rows affected (0.06 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> INSERT INTO products (productCode, name, quantity, price) VALUES
    ->          ('PEC', 'Pencil 2B', 10000, 0.48),
    ->          ('PEC', 'Pencil 2H', 8000, 0.49);
Query OK, 2 rows affected (0.04 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> INSERT INTO products (productCode, name) VALUES ('PEC', 'Pencil HB');
Query OK, 1 row affected (0.03 sec)

mysql> select * from products;
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1001 | PEN         | Pen Red   |     5000 |     1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |     1.25 |
|      1003 | PEN         | Pen Black |     2000 |     1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> INSERT INTO products values (NULL, NULL, NULL, NULL, NULL);
ERROR 1048 (23000): Column 'productCode' cannot be null
mysql>

mysql>
mysql> use southwind;
Database changed
mysql>
mysql> select * from products;
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1001 | PEN         | Pen Red   |     5000 |     1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |     1.25 |
|      1003 | PEN         | Pen Black |     2000 |     1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select productID, productCode from products;
+-----------+-------------+
| productID | productCode |
+-----------+-------------+
|      1001 | PEN         |
|      1002 | PEN         |
|      1003 | PEN         |
|      1004 | PEC         |
|      1005 | PEC         |
|      1006 | PEC         |
+-----------+-------------+

mysql> select * from products where productCode = 'pec';
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select * from products where productCode = "pec";
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> select * from Products where productCode = "pec";
+-----------+-------------+-----------+----------+----------+
| productID | productCode | name      | quantity | price    |
+-----------+-------------+-----------+----------+----------+
|      1004 | PEC         | Pencil 2B |    10000 |     0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |     0.49 |
|      1006 | PEC         | Pencil HB |        0 | 99999.99 |
+-----------+-------------+-----------+----------+----------+

mysql> select * from Products where productCode = "pec"  and price < 2.0;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> select * from Products where productCode = "pec"  and price < 2.0 and quantity > 8000;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> select productID, productCode, quantity
    -> from products
    -> where name like "Pencil%"  or quantity >= 8000;
+-----------+-------------+----------+
| productID | productCode | quantity |
+-----------+-------------+----------+
|      1002 | PEN         |     8000 |
|      1004 | PEC         |    10000 |
|      1005 | PEC         |     8000 |
|      1006 | PEC         |        0 |
+-----------+-------------+----------+

mysql> DELETE FROM products WHERE productID = 1006;
Query OK, 1 row affected (0.16 sec)

mysql> select * from Products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT name, price FROM products;
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> 
mysql>
mysql> select productCode, max(quantity), min(quantity) from Products group by productCode;
+-------------+---------------+---------------+
| productCode | max(quantity) | min(quantity) |
+-------------+---------------+---------------+
| PEC         |         10000 |          8000 |
| PEN         |          8000 |          2000 |
+-------------+---------------+---------------+

mysql>
mysql>
mysql> select productCode, max(quantity), min(quantity)
    -> from products
    -> group by productCode
    -> having productCode = 'PEN';
+-------------+---------------+---------------+
| productCode | max(quantity) | min(quantity) |
+-------------+---------------+---------------+
| PEN         |          8000 |          2000 |
+-------------+---------------+---------------+

mysql>
mysql> select productCode, sum(price)
    -> from products
    -> group by productCode;
+-------------+------------+
| productCode | sum(price) |
+-------------+------------+
| PEC         |       0.97 |
| PEN         |       3.73 |
+-------------+------------+

mysql> select productCode, avg(price)
    -> from products
    -> group by productCode;
+-------------+------------+
| productCode | avg(price) |
+-------------+------------+
| PEC         |   0.485000 |
| PEN         |   1.243333 |
+-------------+------------+

mysql> select productCode, count(*)
    -> from products
    -> group by productCode;
+-------------+----------+
| productCode | count(*) |
+-------------+----------+
| PEC         |        2 |
| PEN         |        3 |
+-------------+----------+

mysql> select name, count(*)
    -> from products
    -> group by name;
+-----------+----------+
| name      | count(*) |
+-----------+----------+
| Pen Black |        1 |
| Pen Blue  |        1 |
| Pen Red   |        1 |
| Pencil 2B |        1 |
| Pencil 2H |        1 |
+-----------+----------+

mysql> select quantity, count(*)
    -> from products
    -> group by quantity;
+----------+----------+
| quantity | count(*) |
+----------+----------+
|     2000 |        1 |
|     5000 |        1 |
|     8000 |        2 |
|    10000 |        1 |
+----------+----------+

mysql> select distinct(quantity)  from products;
+----------+
| quantity |
+----------+
|     5000 |
|     8000 |
|     2000 |
|    10000 |
+----------+

mysql> select all(quantity)  from products;
+----------+
| quantity |
+----------+
|     5000 |
|     8000 |
|     2000 |
|    10000 |
|     8000 |
+----------+

mysql> SELECT name, price FROM products WHERE name LIKE 'P__%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name LIKE 'P___R%';
+---------+-------+
| name    | price |
+---------+-------+
| Pen Red |  1.23 |
+---------+-------+

mysql>

mysql> SELECT name, price FROM products WHERE price < 1.0;
+-----------+-------+
| name      | price |
+-----------+-------+
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, quantity FROM products WHERE quantity <= 2000;
+-----------+----------+
| name      | quantity |
+-----------+----------+
| Pen Black |     2000 |
+-----------+----------+

mysql> SELECT name, price FROM products WHERE productCode = 'PEN';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name LIKE 'PENCIL%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'Pen%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'pen%';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
| Pencil 2B |  0.48 |
| Pencil 2H |  0.49 |
+-----------+-------+

mysql> SELECT name, price FROM products WHERE name like 'pen %';
+-----------+-------+
| name      | price |
+-----------+-------+
| Pen Red   |  1.23 |
| Pen Blue  |  1.25 |
| Pen Black |  1.25 |
+-----------+-------+

mysql> SELECT * FROM products WHERE quantity >= 5000 AND name LIKE 'Pen %';
+-----------+-------------+----------+----------+-------+
| productID | productCode | name     | quantity | price |
+-----------+-------------+----------+----------+-------+
|      1001 | PEN         | Pen Red  |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue |     8000 |  1.25 |
+-----------+-------------+----------+----------+-------+

mysql> 
mysql> select * FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %';
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql>
mysql>
mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE NOT (quantity >= 5000 AND name LIKE 'Pen %');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE  quantity >= 5000 AND name LIKE 'Pen %';
+-----------+-------------+----------+----------+-------+
| productID | productCode | name     | quantity | price |
+-----------+-------------+----------+----------+-------+
|      1001 | PEN         | Pen Red  |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue |     8000 |  1.25 |
+-----------+-------------+----------+----------+-------+

mysql> SELECT * FROM products WHERE  quantity < 5000 OR name NOT LIKE 'Pen %';
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql>

Database changed
mysql> SELECT * FROM products WHERE name IN ('Pen Red', 'Pen Black');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name NOT IN ('Pen Red', 'Pen Black');
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name NOT IN ('Pen Red', 'Pen Black'); select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products
    ->        WHERE (price BETWEEN 1.0 AND 2.0) AND (quantity BETWEEN 1000 AND 2000);
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE productCode IS NULL;
Empty set (0.07 sec)

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price ;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price ASC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC, quantity;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY RAND();
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY price LIMIT 2;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY price LIMIT 2, 1;
+-----------+-------------+---------+----------+-------+
| productID | productCode | name    | quantity | price |
+-----------+-------------+---------+----------+-------+
|      1001 | PEN         | Pen Red |     5000 |  1.23 |
+-----------+-------------+---------+----------+-------+

mysql> SELECT * FROM products ORDER BY price;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT productID AS ID, productCode AS Code,
    ->               name AS Description, price AS 'Unit Price'
    ->        FROM products
    ->        ORDER BY ID;
+------+------+-------------+------------+
| ID   | Code | Description | Unit Price |
+------+------+-------------+------------+
| 1001 | PEN  | Pen Red     |       1.23 |
| 1002 | PEN  | Pen Blue    |       1.25 |
| 1003 | PEN  | Pen Black   |       1.25 |
| 1004 | PEC  | Pencil 2B   |       0.48 |
| 1005 | PEC  | Pencil 2H   |       0.49 |
+------+------+-------------+------------+

mysql>  select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> select * , price * 0.10 AS Discount from products;
+-----------+-------------+-----------+----------+-------+----------+
| productID | productCode | name      | quantity | price | Discount |
+-----------+-------------+-----------+----------+-------+----------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |   0.1230 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |   0.1250 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |   0.1250 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |   0.0480 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |   0.0490 |
+-----------+-------------+-----------+----------+-------+----------+

mysql>
mysql>
mysql> SELECT price FROM products;
+-------+
| price |
+-------+
|  1.23 |
|  1.25 |
|  1.25 |
|  0.48 |
|  0.49 |
+-------+

mysql> SELECT DISTINCT price AS 'Distinct Price' FROM products;
+----------------+
| Distinct Price |
+----------------+
|           1.23 |
|           1.25 |
|           0.48 |
|           0.49 |
+----------------+

mysql> SELECT DISTINCT price FROM products;
+-------+
| price |
+-------+
|  1.23 |
|  1.25 |
|  0.48 |
|  0.49 |
+-------+

mysql> SELECT DISTINCT price, name from Products;
+-------+-----------+
| price | name      |
+-------+-----------+
|  1.23 | Pen Red   |
|  1.25 | Pen Blue  |
|  1.25 | Pen Black |
|  0.48 | Pencil 2B |
|  0.49 | Pencil 2H |
+-------+-----------+

mysql> SELECT price, name from Products;
+-------+-----------+
| price | name      |
+-------+-----------+
|  1.23 | Pen Red   |
|  1.25 | Pen Blue  |
|  1.25 | Pen Black |
|  0.48 | Pencil 2B |
|  0.49 | Pencil 2H |
+-------+-----------+

mysql> SELECT DISTINCT productCode, price, name from Products;
+-------------+-------+-----------+
| productCode | price | name      |
+-------------+-------+-----------+
| PEN         |  1.23 | Pen Red   |
| PEN         |  1.25 | Pen Blue  |
| PEN         |  1.25 | Pen Black |
| PEC         |  0.48 | Pencil 2B |
| PEC         |  0.49 | Pencil 2H |
+-------------+-------+-----------+

mysql> SELECT DISTINCT productCode, price from Products;
+-------------+-------+
| productCode | price |
+-------------+-------+
| PEN         |  1.23 |
| PEN         |  1.25 |
| PEC         |  0.48 |
| PEC         |  0.49 |
+-------------+-------+

mysql> SELECT * FROM products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> SELECT * FROM products ORDER BY productCode, productID;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+


mysql>
mysql> SELECT productCode, COUNT(*) FROM products GROUP BY productCode;
+-------------+----------+
| productCode | COUNT(*) |
+-------------+----------+
| PEC         |        2 |
| PEN         |        3 |
+-------------+----------+

mysql> SELECT productCode, COUNT(*) AS count
    ->        FROM products
    ->        GROUP BY productCode
    ->        ORDER BY count DESC;
+-------------+-------+
| productCode | count |
+-------------+-------+
| PEN         |     3 |
| PEC         |     2 |
+-------------+-------+

mysql> SELECT productCode, MAX(price) AS 'Highest Price', MIN(price) AS 'Lowest Price'
    ->        FROM products
    ->        GROUP BY productCode;
+-------------+---------------+--------------+
| productCode | Highest Price | Lowest Price |
+-------------+---------------+--------------+
| PEC         |          0.49 |         0.48 |
| PEN         |          1.25 |         1.23 |
+-------------+---------------+--------------+

mysql>
mysql> SELECT productCode, MAX(price), MIN(price),
    ->               CAST(AVG(price) AS DECIMAL(7,2)) AS 'Average',
    ->               CAST(STD(price) AS DECIMAL(7,2)) AS 'Std Dev',
    ->               SUM(quantity)
    ->        FROM products
    ->        GROUP BY productCode;
+-------------+------------+------------+---------+---------+---------------+
| productCode | MAX(price) | MIN(price) | Average | Std Dev | SUM(quantity) |
+-------------+------------+------------+---------+---------+---------------+
| PEC         |       0.49 |       0.48 |    0.49 |    0.01 |         18000 |
| PEN         |       1.25 |       1.23 |    1.24 |    0.01 |         15000 |
+-------------+------------+------------+---------+---------+---------------+



mysql> use southwind;
Database changed
mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     5000 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> UPDATE products SET quantity = quantity - 100 WHERE name = 'Pen Red';
Query OK, 1 row affected (0.17 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4900 |  1.23 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> UPDATE products SET quantity = quantity + 50, price = 1.27 WHERE name = 'Pen Red';
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4950 |  1.27 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
|      1004 | PEC         | Pencil 2B |    10000 |  0.48 |
|      1005 | PEC         | Pencil 2H |     8000 |  0.49 |
+-----------+-------------+-----------+----------+-------+

mysql> DELETE FROM products WHERE name LIKE 'Pencil%';
Query OK, 2 rows affected (0.08 sec)

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1001 | PEN         | Pen Red   |     4950 |  1.27 |
|      1002 | PEN         | Pen Blue  |     8000 |  1.25 |
|      1003 | PEN         | Pen Black |     2000 |  1.25 |
+-----------+-------------+-----------+----------+-------+

mysql> DELETE FROM products;
Query OK, 3 rows affected (0.03 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\>cd mysql


D:\mysql>copy con  products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47
^Z
        1 file(s) copied.

D:\mysql>type products_in.csv
\N,PEC,Pencil 3B,500,0.52
\N,PEC,Pencil 4B,200,0.62
\N,PEC,Pencil 5B,100,0.73
\N,PEC,Pencil 6B,500,0.47

D:\mysql>mysql -u user1 -h 127.0.0.1 -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
+---------------------+

mysql> select * from products;
Empty set (0.01 sec)

mysql> LOAD DATA LOCAL INFILE 'D:/mysql/products_in.csv' INTO TABLE products
    ->          COLUMNS TERMINATED BY ','
    ->          LINES TERMINATED BY '\r\n';
Query OK, 4 rows affected (0.07 sec)
Records: 4  Deleted: 0  Skipped: 0  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      1006 | PEC         | Pencil 3B |      500 |  0.52 |
|      1007 | PEC         | Pencil 4B |      200 |  0.62 |
|      1008 | PEC         | Pencil 5B |      100 |  0.73 |
|      1009 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql> delete from products;
Query OK, 4 rows affected (0.04 sec)

mysql> select * from products;
Empty set (0.00 sec)

mysql> exit
Bye

D:\mysql>copy con products_in.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47
^Z
        1 file(s) copied.

D:\mysql>type products_in.tsv
\N  PEC  Pencil 3B  500  0.52
\N  PEC  Pencil 4B  200  0.62
\N  PEC  Pencil 5B  100  0.73
\N  PEC  Pencil 6B  500  0.47

D:\mysql>mysqlimport -u user1  -p --local southwind products_in.tsv
Enter password: *******
mysqlimport: Error: 1146, Table 'southwind.products_in' doesn't exist, when using table: products_in

D:\mysql>rename products_in.tsv products.tsv

D:\mysql>type products.tsv
\N	PEC	Pencil	4B	200	0.62
\N	PEC	Pencil	5B	100	0.73



D:\mysql>type products.tsv
\N      PEC     Pencil  4B      200     0.62
\N      PEC     Pencil  5B      100     0.73
D:\mysql>mysqlimport -u user1  -p --local southwind products.tsv
Enter password: *******
southwind.products: Records: 3  Deleted: 0  Skipped: 0  Warnings: 5

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql> exit
Bye

D:\mysql>type abc.sql
DELETE FROM products;
INSERT INTO products VALUES (2001, 'PEC', 'Pencil 3B', 500, 0.52),
                            (NULL, 'PEC', 'Pencil 4B', 200, 0.62),
                            (NULL, 'PEC', 'Pencil 5B', 100, 0.73),
                            (NULL, 'PEC', 'Pencil 6B', 500, 0.47);
SELECT * FROM products;

D:\mysql>mysql -u user1  -h 127.0.0.1  -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.31 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use southwind;
Database changed

mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql>
mysql>
mysql> select * from products;
+-----------+-------------+--------+----------+--------+
| productID | productCode | name   | quantity | price  |
+-----------+-------------+--------+----------+--------+
|      1001 | PEC         | Pencil |        3 | 500.00 |
|      1020 | PEC         | Pencil |        4 | 200.00 |
|      1021 | PEC         | Pencil |        5 | 100.00 |
+-----------+-------------+--------+----------+--------+

mysql> source d:/mysql/abc.sql
Query OK, 3 rows affected (0.04 sec)

Query OK, 4 rows affected (0.04 sec)
Records: 4  Duplicates: 0  Warnings: 0

+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql>
Give the output the following SQL queries :
i.	Select Designation Count (*) From Admin Group By Designation Having Count (*) <2;
ii.	SELECT max (EXPERIENCE) FROM SCH¬OOL;
iii.	SELECT TEACHER FROM SCHOOL WHERE EXPERIENCE >12 ORDER BY TEACHER;
iv.	SELECT COUNT (*), GENDER FROM AD¬MIN GROUP BY GENDER;
(a) 1
(b) 2
(c) 3
(d) 4

(a) A point of maximum         

(b) A point of minimum          

(c) Points of maximum as well as of minimum

(d) Neither a point of maximum nor minimum
a pressure of 101.33 kPa.
Database changed
mysql> select * from products;
+-----------+-------------+-----------+----------+-------+
| productID | productCode | name      | quantity | price |
+-----------+-------------+-----------+----------+-------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |
+-----------+-------------+-----------+----------+-------+

mysql> CREATE TABLE suppliers (
    ->          supplierID  INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    ->          name        VARCHAR(30)   NOT NULL DEFAULT '',
    ->          phone       CHAR(8)       NOT NULL DEFAULT '',
    ->          PRIMARY KEY (supplierID)
    ->        );
Query OK, 0 rows affected (1.06 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
| suppliers           |
+---------------------+

mysql> describe suppliers;
+------------+------------------+------+-----+---------+----------------+
| Field      | Type             | Null | Key | Default | Extra          |
+------------+------------------+------+-----+---------+----------------+
| supplierID | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name       | varchar(30)      | NO   |     |         |                |
| phone      | char(8)          | NO   |     |         |                |
+------------+------------------+------+-----+---------+----------------+

mysql> INSERT INTO suppliers VALUE
    ->           (501, 'ABC Traders', '88881111'),
    ->           (502, 'XYZ Company', '88882222'),
    ->           (503, 'QQ Corp', '88883333');
Query OK, 3 rows affected (0.14 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql>
mysql> select * from suppliers;
+------------+-------------+----------+
| supplierID | name        | phone    |
+------------+-------------+----------+
|        501 | ABC Traders | 88881111 |
|        502 | XYZ Company | 88882222 |
|        503 | QQ Corp     | 88883333 |
+------------+-------------+----------+

mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
+-------------+------------------+------+-----+----------+----------------+

mysql> ALTER TABLE products
    ->        ADD COLUMN supplierID INT UNSIGNED NOT NULL;
Query OK, 0 rows affected (1.21 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
| supplierID  | int(10) unsigned | NO   |     | NULL     |                |
+-------------+------------------+------+-----+----------+----------------+

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |          0 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |          0 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |          0 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |          0 |
+-----------+-------------+-----------+----------+-------+------------+

mysql> UPDATE products SET supplierID = 501;
Query OK, 4 rows affected (0.07 sec)
Rows matched: 4  Changed: 4  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        501 |
+-----------+-------------+-----------+----------+-------+------------+

mysql>
mysql>
mysql> ALTER TABLE products
    ->        ADD FOREIGN KEY (supplierID) REFERENCES suppliers (supplierID);
Query OK, 4 rows affected (0.87 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> describe products;
+-------------+------------------+------+-----+----------+----------------+
| Field       | Type             | Null | Key | Default  | Extra          |
+-------------+------------------+------+-----+----------+----------------+
| productID   | int(10) unsigned | NO   | PRI | NULL     | auto_increment |
| productCode | char(3)          | NO   |     |          |                |
| name        | varchar(30)      | NO   |     |          |                |
| quantity    | int(10) unsigned | NO   |     | 0        |                |
| price       | decimal(7,2)     | NO   |     | 99999.99 |                |
| supplierID  | int(10) unsigned | NO   | MUL | NULL     |                |
+-------------+------------------+------+-----+----------+----------------+

mysql>
mysql> UPDATE products SET supplierID = 502 WHERE productID  = 2004;
Query OK, 1 row affected (0.17 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        502 |
+-----------+-------------+-----------+----------+-------+------------+

mysql> SELECT products.name, price, suppliers.name
    ->        FROM products, suppliers
    ->        WHERE products.supplierID = suppliers.supplierID
    ->           AND price < 0.6;
+-----------+-------+-------------+
| name      | price | name        |
+-----------+-------+-------------+
| Pencil 3B |  0.52 | ABC Traders |
| Pencil 6B |  0.47 | XYZ Company |
+-----------+-------+-------------+

mysql> select * products;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'products' at line 1
mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        502 |
+-----------+-------------+-----------+----------+-------+------------+

mysql> select * from suppliers;
+------------+-------------+----------+
| supplierID | name        | phone    |
+------------+-------------+----------+
|        501 | ABC Traders | 88881111 |
|        502 | XYZ Company | 88882222 |
|        503 | QQ Corp     | 88883333 |
+------------+-------------+----------+

mysql> SELECT products.name, price, suppliers.name
    ->        FROM products, suppliers
    ->        WHERE products.supplierID = suppliers.supplierID
    ->           AND price < 0.6;
+-----------+-------+-------------+
| name      | price | name        |
+-----------+-------+-------------+
| Pencil 3B |  0.52 | ABC Traders |
| Pencil 6B |  0.47 | XYZ Company |
+-----------+-------+-------------+

mysql>
mysql> SELECT products.name, price, suppliers.name , phone
    ->        FROM products, suppliers
    ->        WHERE products.supplierID = suppliers.supplierID
    ->           AND price > 0.6;
+-----------+-------+-------------+----------+
| name      | price | name        | phone    |
+-----------+-------+-------------+----------+
| Pencil 4B |  0.62 | ABC Traders | 88881111 |
| Pencil 5B |  0.73 | ABC Traders | 88881111 |
+-----------+-------+-------------+----------+

mysql> SELECT products.name AS 'Product Name', price, suppliers.name AS 'Supplier Name'
    ->        FROM products, suppliers
    ->        WHERE products.supplierID = suppliers.supplierID AND price < 0.6;
+--------------+-------+---------------+
| Product Name | price | Supplier Name |
+--------------+-------+---------------+
| Pencil 3B    |  0.52 | ABC Traders   |
| Pencil 6B    |  0.47 | XYZ Company   |
+--------------+-------+---------------+

mysql>
mysql>
mysql>
mysql>
mysql>
mysql> SELECT products.name AS 'Product Name', price, suppliers.name AS 'Supplier Name'
    ->        FROM products
    ->           JOIN suppliers ON products.supplierID = suppliers.supplierID
    ->        WHERE price < 0.6;
+--------------+-------+---------------+
| Product Name | price | Supplier Name |
+--------------+-------+---------------+
| Pencil 3B    |  0.52 | ABC Traders   |
| Pencil 6B    |  0.47 | XYZ Company   |
+--------------+-------+---------------+

mysql>
(i) SELECT Name, Joinyear FROM APPLI¬CANTS
	WHERE GENDER=’F’ and C_ID=’A02′;
(ii)	SELECT MIN (Joinyear) 
	FROM APPLICANTS
	WHERE Gender=’m’;
(iii)	SELECT AVG (Fee) FROM APPLICANTS
	WHERE C_ID=’A0T OR C_ID=’A05′;
(iv)	SELECT SUM- (Fee), C_ID FROM C_ ID
	GROUP BY C_ID
	HAVING COUNT(*)=2;
wires is equal to L, the cross-section radius of each wire equals a. In the case a << L find:
(a) the current density at the point equally removed from the axes of the wires by a distance r if the potential difference between the
wires is equal to V;
(b) the electric resistance of the medium per unit length of the wires.

     (a) 2                                           (b) 3

     (c) 4                                           (d) None of these

B). ( rho * 4 )/(pi*L^2)
Database changed
mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
| suppliers           |
+---------------------+

mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        502 |
+-----------+-------------+-----------+----------+-------+------------+

mysql> select * from suppliers;
+------------+-------------+----------+
| supplierID | name        | phone    |
+------------+-------------+----------+
|        501 | ABC Traders | 88881111 |
|        502 | XYZ Company | 88882222 |
|        503 | QQ Corp     | 88883333 |
+------------+-------------+----------+

mysql>
mysql> delete from suppliers where supplierID = 502;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`southwind`.`products`, CONSTRAINT `products_ibfk_1` FOREIGN KEY (`supplierID`) REFERENCES `suppliers` (`supplierID`))
mysql>
mysql>
mysql>
mysql>
mysql>

mysql>
mysql> select productID, products.supplierID
    -> from Products, Suppliers
    -> where products.supplierID = suppliers.supplierID;
+-----------+------------+
| productID | supplierID |
+-----------+------------+
|      2001 |        501 |
|      2002 |        501 |
|      2003 |        501 |
|      2004 |        502 |
+-----------+------------+

mysql>
mysql> select * from products;
+-----------+-------------+-----------+----------+-------+------------+
| productID | productCode | name      | quantity | price | supplierID |
+-----------+-------------+-----------+----------+-------+------------+
|      2001 | PEC         | Pencil 3B |      500 |  0.52 |        501 |
|      2002 | PEC         | Pencil 4B |      200 |  0.62 |        501 |
|      2003 | PEC         | Pencil 5B |      100 |  0.73 |        501 |
|      2004 | PEC         | Pencil 6B |      500 |  0.47 |        502 |
+-----------+-------------+-----------+----------+-------+------------+

mysql>
mysql> create view  products_quantity AS
    -> select name, quantity from products;
Query OK, 0 rows affected (0.11 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
| products_quantity   |
| suppliers           |
+---------------------+

mysql>
mysql> select * from products_quantity;
+-----------+----------+
| name      | quantity |
+-----------+----------+
| Pencil 3B |      500 |
| Pencil 4B |      200 |
| Pencil 5B |      100 |
| Pencil 6B |      500 |
+-----------+----------+

mysql> CREATE VIEW products_suppliers AS select productID, products.supplierID, suppliers.name
    ->  from Products, Suppliers
    -> where products.supplierID = suppliers.supplierID;
Query OK, 0 rows affected (0.13 sec)

mysql> show tables;
+---------------------+
| Tables_in_southwind |
+---------------------+
| products            |
| products_quantity   |
| products_suppliers  |
| suppliers           |
+---------------------+

mysql> select * from products_suppliers;
+-----------+------------+-------------+
| productID | supplierID | name        |
+-----------+------------+-------------+
|      2001 |        501 | ABC Traders |
|      2002 |        501 | ABC Traders |
|      2003 |        501 | ABC Traders |
|      2004 |        502 | XYZ Company |
+-----------+------------+-------------+

mysql> select * from products_suppliers  where productID = 2002;
+-----------+------------+-------------+
| productID | supplierID | name        |
+-----------+------------+-------------+
|      2002 |        501 | ABC Traders |
+-----------+------------+-------------+

mysql> select * from products_suppliers  where supplierID = 502;
+-----------+------------+-------------+
| productID | supplierID | name        |
+-----------+------------+-------------+
|      2004 |        502 | XYZ Company |
+-----------+------------+-------------+

mysql> select * from products_suppliers  where supplierID = 501;
+-----------+------------+-------------+
| productID | supplierID | name        |
+-----------+------------+-------------+
|      2001 |        501 | ABC Traders |
|      2002 |        501 | ABC Traders |
|      2003 |        501 | ABC Traders |
+-----------+------------+-------------+

mysql>
Query OK, 1 row affected (0.08 sec)

mysql> use hospital_db;
Database changed
mysql>
mysql>
mysql> CREATE TABLE patients (
    ->           patientID      INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    ->           name           VARCHAR(30)   NOT NULL DEFAULT '',
    ->           dateOfBirth    DATE          NOT NULL,
    ->           lastVisitDate  DATE          NOT NULL,
    ->           nextVisitDate  DATE          NULL,
    ->           PRIMARY KEY (patientID)
    ->        );
Query OK, 0 rows affected (0.70 sec)

mysql> show tables;
+-----------------------+
| Tables_in_hospital_db |
+-----------------------+
| patients              |
+-----------------------+

mysql> describe patients;
+---------------+------------------+------+-----+---------+----------------+
| Field         | Type             | Null | Key | Default | Extra          |
+---------------+------------------+------+-----+---------+----------------+
| patientID     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name          | varchar(30)      | NO   |     |         |                |
| dateOfBirth   | date             | NO   |     | NULL    |                |
| lastVisitDate | date             | NO   |     | NULL    |                |
| nextVisitDate | date             | YES  |     | NULL    |                |
+---------------+------------------+------+-----+---------+----------------+

mysql> INSERT INTO patients VALUES
    ->           (1001, 'Ah Teck', '1991-12-31', '2012-01-20', NULL),
    ->           (NULL, 'Kumar', '2011-10-29', '2012-09-20', NULL),
    ->           (NULL, 'Ali', '2011-01-30', CURDATE(), NULL);
Query OK, 3 rows affected (0.13 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from patients;
+-----------+---------+-------------+---------------+---------------+
| patientID | name    | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+---------+-------------+---------------+---------------+
|      1001 | Ah Teck | 1991-12-31  | 2012-01-20    | NULL          |
|      1002 | Kumar   | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali     | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+---------+-------------+---------------+---------------+

mysql> SELECT * FROM patients
    ->        WHERE lastVisitDate BETWEEN '2012-09-15' AND CURDATE()
    ->        ORDER BY lastVisitDate;
+-----------+-------+-------------+---------------+---------------+
| patientID | name  | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+-------+-------------+---------------+---------------+
|      1002 | Kumar | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali   | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+-------+-------------+---------------+---------------+

mysql> SELECT * FROM patients
    ->        WHERE YEAR(dateOfBirth) = 2011
    ->        ORDER BY MONTH(dateOfBirth), DAY(dateOfBirth)
    -> ;
+-----------+-------+-------------+---------------+---------------+
| patientID | name  | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+-------+-------------+---------------+---------------+
|      1003 | Ali   | 2011-01-30  | 2020-08-14    | NULL          |
|      1002 | Kumar | 2011-10-29  | 2012-09-20    | NULL          |
+-----------+-------+-------------+---------------+---------------+

mysql> SELECT * FROM patients
    ->        WHERE MONTH(dateOfBirth) = MONTH(CURDATE())
    ->           AND DAY(dateOfBirth) = DAY(CURDATE());
Empty set (0.00 sec)

mysql> SELECT * FROM patients
    ->        WHERE MONTH(dateOfBirth) = 1;
+-----------+------+-------------+---------------+---------------+
| patientID | name | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+------+-------------+---------------+---------------+
|      1003 | Ali  | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+------+-------------+---------------+---------------+

mysql> SELECT name, dateOfBirth, TIMESTAMPDIFF(YEAR, dateOfBirth, CURDATE()) AS age
    ->        FROM patients
    ->        ORDER BY age, dateOfBirth;
+---------+-------------+------+
| name    | dateOfBirth | age  |
+---------+-------------+------+
| Kumar   | 2011-10-29  |    8 |
| Ali     | 2011-01-30  |    9 |
| Ah Teck | 1991-12-31  |   28 |
+---------+-------------+------+

mysql> SELECT name, lastVisitDate FROM patients
    ->        WHERE TIMESTAMPDIFF(DAY, lastVisitDate, CURDATE()) > 60;
+---------+---------------+
| name    | lastVisitDate |
+---------+---------------+
| Ah Teck | 2012-01-20    |
| Kumar   | 2012-09-20    |
+---------+---------------+

mysql> SELECT name, lastVisitDate FROM patients
    ->        WHERE TO_DAYS(CURDATE()) - TO_DAYS(lastVisitDate) > 60;
+---------+---------------+
| name    | lastVisitDate |
+---------+---------------+
| Ah Teck | 2012-01-20    |
| Kumar   | 2012-09-20    |
+---------+---------------+

mysql> SELECT * FROM patients
    ->        WHERE dateOfBirth > DATE_SUB(CURDATE(), INTERVAL 18 YEAR);
+-----------+-------+-------------+---------------+---------------+
| patientID | name  | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+-------+-------------+---------------+---------------+
|      1002 | Kumar | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali   | 2011-01-30  | 2020-08-14    | NULL          |
+-----------+-------+-------------+---------------+---------------+

mysql> UPDATE patients
    ->        SET nextVisitDate = DATE_ADD(CURDATE(), INTERVAL 6 MONTH)
    ->        WHERE name = 'Ali';
Query OK, 1 row affected (0.07 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM patients;
+-----------+---------+-------------+---------------+---------------+
| patientID | name    | dateOfBirth | lastVisitDate | nextVisitDate |
+-----------+---------+-------------+---------------+---------------+
|      1001 | Ah Teck | 1991-12-31  | 2012-01-20    | NULL          |
|      1002 | Kumar   | 2011-10-29  | 2012-09-20    | NULL          |
|      1003 | Ali     | 2011-01-30  | 2020-08-14    | 2021-02-14    |
+-----------+---------+-------------+---------------+---------------+

mysql> select now(), curdate(), curtime();
+---------------------+------------+-----------+
| now()               | curdate()  | curtime() |
+---------------------+------------+-----------+
| 2020-08-14 16:12:50 | 2020-08-14 | 16:12:50  |
+---------------------+------------+-----------+

mysql>
+--------------------------------------+
| DATEDIFF('2012-02-01', '2012-01-28') |
+--------------------------------------+
|                                    4 |
+--------------------------------------+

mysql> SELECT DATEDIFF('2012-02-01', '2011-01-28');
+--------------------------------------+
| DATEDIFF('2012-02-01', '2011-01-28') |
+--------------------------------------+
|                                  369 |
+--------------------------------------+

mysql> SELECT TIMESTAMPDIFF(DAY, '2012-02-01', '2012-01-28');
+------------------------------------------------+
| TIMESTAMPDIFF(DAY, '2012-02-01', '2012-01-28') |
+------------------------------------------------+
|                                             -4 |
+------------------------------------------------+

mysql>
FROM COMPANY, CUSTOMER WHERE
COMPANY. CID=CUSTOMER.CID AND

            (a) (–∞, 1]                                           (b) [3, ∞)

            (c) (–∞, 1] U [3, ∞)                                 (d) [1, 3]
changing the temperature?

(a) 3 : 4
(b) 3 : 2
(c) 5 : 1
(d) 5 : 4

        (a) is ey + x =2                   (b) is x + y = e

        (c) is ex + y = 1                  (d) does not exist
	FROM WATCHES W, SALE S 
	WHERE W. WAT£H1D!=S.WATCHID; 
	FROM WATCHES W, SALE S 
	WHERE W. WATCHID = S.WATCHID GROUP BY S.WATCHID;

            (a) Increasing

            (b) Decreasing

            (c) Increasing in (0, p/4) and decreasing in (p/4, p/2)

            (d) None of these

To join by phone instead, dial ‪+1 515-493-4637‬ and enter this PIN: ‪441 987 385#
(i) SELECT MAX (PRICE), MIN (PRICE) FROM ITEMS;
(ii) SELECT PRICE*QTY
FROM ITEMS WHERE CODE-1004;
(iii)	SELECT DISTINCT TCODE FROM ITEMS;
(iv) SELECT INAME, TNAME FROM ITEMS I, TRADERS T WHERE I.TCODE=T.TCODE AND QTY< 100;

The value of internal resistance of the cell is 
(a) 0.25 Ω
(b) 0.95 Ω
(c) 0.5 Ω
(d) 0.75 Ω
(a) 0
(b) -1
(c) 10
(d) -10
import mysql.connector
import mysql.connector


mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

print(mydb)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38' "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%' "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers MODIFY id INT auto_increment FIRST")

mycursor.execute("DESCRIBE customers")

for x in mycursor:
    print(x)
Roll no. 12520
(ii)	Write SQL commands for the following statements: 
-To display the names of all the white coloured vehicles.
- To display name of vehicle name and capacity of vehicles in ascending order of their sitting capacity.
- To display the highest charges at which a vehicle can be hired from CABHUB.
- To display the customer name and the corresponding name of the vehicle hired by them.
(c)Give the output of the following SQL queries : 
(i) SELECT COUNT(DISTINCT Make) FROM CABHUB;
(ii) SELECT MAX(Charges), MIN(Charges)
FROM CABHUB;
The more number of particle there will be the more will be the entropy. 
Also solid solids have less entropy than liquid due rigidity in solids.
Same goes with liquid and gas.
So, in 1. Entropy increase(due to less number of particles )

State of initial solid substances changed to gas that has more degree of freedom and due to their natural oscillations and reaction potential energy they will randomly arranged more than solid substance in initial substances .

More no. Of particles  after reaction so randomness of particles are more in final substances than initial .


More no. Of moles/~particles in initial  substances will be more random than final due to this Entropy decrease and entropy change become negative .


Since , State of substances changed to liquid state from more random gaseous state , and no. Of particles or moles in final substances is less than initial so the entropy decreasing and the change in entropy is negative .

In case 1 : 1 mol of solid had converted to 3 mol of gas and hence entropy is  increased

In case 2 : 3 mol of gas had converted to 2 mol of gas and hence decrease in entropy

In case 3 : 3 mol of gas had converted to 2 mol of liquid and hence decrease in entropy

Student ID and Roll no. Are candidate key ,, Student ID is primary key , according to my table .
Roll no. : 12508
Query OK, 1 row affected (0.01 sec)


mysql> use products_db;
Database changed
mysql> CREATE TABLE users (id INT UNSIGNED auto_increment PRIMARY KEY,
    ->      name VARCHAR(30),
    ->          fav INT UNSIGNED);
Query OK, 0 rows affected (0.49 sec)

mysql>
mysql> CREATE TABLE products (id INT UNSIGNED PRIMARY KEY,
    ->      name VARCHAR(30) NOT NULL);
Query OK, 0 rows affected (0.31 sec)

mysql> show tables;
+-----------------------+
| Tables_in_products_db |
+-----------------------+
| products              |
| users                 |
+-----------------------+

mysql> INSERT INTO users (name, fav) VALUES
    ->     ('John', 154),
    ->     ('Peter', 154),
    ->     ('Amy', 155),
    ->     ('Hannah', 0),
    ->     ('Michael', 0);
Query OK, 5 rows affected (0.16 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from users;
+----+---------+------+
| id | name    | fav  |
+----+---------+------+
|  1 | John    |  154 |
|  2 | Peter   |  154 |
|  3 | Amy     |  155 |
|  4 | Hannah  |    0 |
|  5 | Michael |    0 |
+----+---------+------+

mysql> INSERT INTO products (id, name) VALUES
    ->     (154, 'Chocolate Heaven'),
    ->      (155,  'Tasty Lemon'),
    ->      (156, 'Vanilla Dreams');
Query OK, 3 rows affected (0.05 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from  products;
+-----+------------------+
| id  | name             |
+-----+------------------+
| 154 | Chocolate Heaven |
| 155 | Tasty Lemon      |
| 156 | Vanilla Dreams   |
+-----+------------------+

mysql>
mysql> SELECT
    ->   users.name AS user,   products.name AS favorite
    ->   FROM users, products
    ->   WHERE users.fav = products.id;
+-------+------------------+
| user  | favorite         |
+-------+------------------+
| John  | Chocolate Heaven |
| Peter | Chocolate Heaven |
| Amy   | Tasty Lemon      |
+-------+------------------+

mysql> SELECT
    ->   users.name AS user,
    ->   products.name AS favorite
    ->   FROM users
    ->   INNER JOIN products ON users.fav = products.id;
+-------+------------------+
| user  | favorite         |
+-------+------------------+
| John  | Chocolate Heaven |
| Peter | Chocolate Heaven |
| Amy   | Tasty Lemon      |
+-------+------------------+

mysql>
mysql> SELECT
    ->   users.name AS user,
    ->   products.name AS favorite
    ->   FROM users
    ->   LEFT JOIN products ON users.fav = products.id;
+---------+------------------+
| user    | favorite         |
+---------+------------------+
| John    | Chocolate Heaven |
| Peter   | Chocolate Heaven |
| Amy     | Tasty Lemon      |
| Hannah  | NULL             |
| Michael | NULL             |
+---------+------------------+

mysql>
mysql> SELECT
    ->   users.name AS user,
    ->   products.name AS favorite
    ->   FROM users
    ->   RIGHT JOIN products ON users.fav = products.id;
+-------+------------------+
| user  | favorite         |
+-------+------------------+
| John  | Chocolate Heaven |
| Peter | Chocolate Heaven |
| Amy   | Tasty Lemon      |
| NULL  | Vanilla Dreams   |
+-------+------------------+

mysql>
mysql>
mysql> SELECT * FROM users
    -> CROSS JOIN products;
+----+---------+------+-----+------------------+
| id | name    | fav  | id  | name             |
+----+---------+------+-----+------------------+
|  1 | John    |  154 | 154 | Chocolate Heaven |
|  1 | John    |  154 | 155 | Tasty Lemon      |
|  1 | John    |  154 | 156 | Vanilla Dreams   |
|  2 | Peter   |  154 | 154 | Chocolate Heaven |
|  2 | Peter   |  154 | 155 | Tasty Lemon      |
|  2 | Peter   |  154 | 156 | Vanilla Dreams   |
|  3 | Amy     |  155 | 154 | Chocolate Heaven |
|  3 | Amy     |  155 | 155 | Tasty Lemon      |
|  3 | Amy     |  155 | 156 | Vanilla Dreams   |
|  4 | Hannah  |    0 | 154 | Chocolate Heaven |
|  4 | Hannah  |    0 | 155 | Tasty Lemon      |
|  4 | Hannah  |    0 | 156 | Vanilla Dreams   |
|  5 | Michael |    0 | 154 | Chocolate Heaven |
|  5 | Michael |    0 | 155 | Tasty Lemon      |
|  5 | Michael |    0 | 156 | Vanilla Dreams   |
+----+---------+------+-----+------------------+

mysql>
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123'
)

mycursor = mydb.cursor()

sql = "CREATE DATABASE IF NOT EXISTS products_db"
mycursor.execute (sql)

sql = "USE products_db"
mycursor.execute (sql)

sql = "CREATE TABLE users (id INT UNSIGNED auto_increment PRIMARY KEY,\
     name VARCHAR(30), \
         fav INT UNSIGNED)"
mycursor.execute (sql)

sql = "CREATE TABLE products (id INT UNSIGNED PRIMARY KEY,\
     name VARCHAR(30) NOT NULL)"

mycursor.execute (sql)

sql = "SHOW TABLES"
mycursor.execute (sql)

for x in mycursor:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
    ('John', 154),
    ('Peter', 154),
    ('Amy', 155),
    ('Hannah', 0),
    ('Michael', 0)
]

mycursor.executemany(sql, val)

mydb.commit()

sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
    (154, 'Chocolate Heaven'),
     (155,  'Tasty Lemon'),
     (156, 'Vanilla Dreams')
]

mycursor.executemany(sql, val)

mydb.commit()

sql = "SELECT * FROM users"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

sql = "SELECT * FROM products"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "SELECT \
    users.name AS user,   products.name AS favorite \
    FROM users, products \
    WHERE users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 

print("\n\n")

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
import mysql.connector

mydb = mysql.connector.connect (
    host = 'localhost',
    user = 'user1',
    password = 'user123',
    database = 'products_db'
)

mycursor = mydb.cursor()

sql = "SELECT * FROM users \
       CROSS JOIN products"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='user1',
                                         password='user123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database()")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
(b) To display product name and price of all those products, whose price is in the range of 10000 and 15000 (both values inclusive).
(c) To display the number of products, which are supplied by each suplier. i.e., the expected output should be; 
	S01   2
	S02   2
	S03   1
(d) To display the price, product name and quantity (i.e., qty) of those products which have quantity more thhn 100.
(e) To display the names of those suppliers, who are either from DELHI or from CHENNAI.
(f) To display the name of the companies and the name of the products in descending order of company names.
	 Obtain the outputs of the following SQL queries based on the data given in tables PRODUCTS and SUPPLIERS above. 
g1) SELECT DISTINCT SUPCODE FROM PRODUCTS;
g2) SELEC MAX (PRICE), MIN (PRICE) FROM PRODUCTS;
g3) SELECT PRICE*QTY
FROM PRODUCTS WHERE PID = 104; (g4)
g4) SELECT PNAME, SNAME
FROM PRODUCTS P, SUPPLIERS S WHERE E SUPCODE = S. SUPCODE
AND QTY>100;

(a) 220 Ω
(b) 110 Ω
(c) 55 Ω
(d) 13.75 Ω

 (a) is equal to 5                        (b) is equal to 3

 (c) is equal to 7                       (d) does not exist
A → B proceeds virtually to the end. Determine: 
(a) the sign of ΔS of the reaction; 
(b) the sign of ΔG for the reaction B → A at the temperature T
(c) the possibility of the reaction B → A proceeding at low temperatures.
B:-G=-ve
C:- ?
(B) -ve
(C) yes ! , It can proceed

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='user1',
                                         password='user123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database()")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='user1',
                                         password='user123')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='user1',
                                         password='user123')
    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (10, 'Lenovo ThinkPad P71', 30459, '2019-08-14') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

import mysql.connector
from mysql.connector import Error

def insertVariblesIntoTable(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='user1',
                                             password='user123')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        recordTuple = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertVariblesIntoTable(2, 'Area 51M', 60999, '2019-04-14')
insertVariblesIntoTable(3, 'MacBook Pro', 200499, '2019-06-20')
+--------------------+
| Database           |
+--------------------+
| information_schema |
| electronics        |
| hospital_db        |
| mydatabase         |
| mysql              |
| performance_schema |
| products_db        |
| southwind          |
| sys                |
+--------------------+

mysql> use electonics;
ERROR 1049 (42000): Unknown database 'electonics'
mysql> use electronics;
Database changed
mysql> show tables;
+-----------------------+
| Tables_in_electronics |
+-----------------------+
| laptop                |
+-----------------------+

mysql> select * from laptop;
+----+---------------------+--------+---------------+
| Id | Name                | Price  | Purchase_date |
+----+---------------------+--------+---------------+
|  2 | Area 51M            |  60999 | 2019-04-14    |
|  3 | MacBook Pro         | 200499 | 2019-06-20    |
| 10 | Lenovo ThinkPad P71 |  30459 | 2019-08-14    |
+----+---------------------+--------+---------------+

mysql>
*Class 11-Class 12*
*17-Aug to 22-Aug*
https://bit.ly/3g3ceTE
o	To display all DepName along with the DepCde in descending order of DepCde.
o	To display the average age of Employees in DepCde as 103.
o	To display the name of DepHead of the Employee named “Sanjeev P”
o	To display the details of all employees who has joined before 2007 from EMPL¬OYEE table.
(b)	Give the output of the following SQL queries: 
o	SELECT COUNT (DISTINCT DepCde) FROM EMPLOYEE;
o	SELECT MAX(JoinDate), MIN (JointDate) FROM EMPLOYEE;
o	SELECT TName, DepHead FROM EMPLOYEE E, DEPARTMENT D
WHERE E.DepCde = D.DepCde;
o	SELECT COUNT (*) FROM EMPLOYEE WHERE Salary > 60000 AND Age > 30;
(a) 0.0012 /°C
(b) 0.0024 /°C
(c) 0.0032 /°C
(d) 0.0064 /°C

(a) Increasing
(b)   Decreasing
(c) Neither increasing nor decreasing
(d) None of these
the standard change in enthalpy ΔH°(298) of formation of CuO.
No student will  miss any class or test of any subject without informing the concerned subject teacher conducted by DOE via online mode.
In case,  if any student of class XII-E,do not appear or miss any class or test consider it as an essential part of your attendance.
No student will  miss any class or test of any subject without informing the concerned subject teacher conducted by DOE via online mode.
In case,  if any student of class XII-E,do not appear or miss any class or test consider it as an essential part of your attendance.

To join by phone instead, dial ‪+1 347-754-4502‬ and enter this PIN: ‪706 674 782#
*Class 11-Class 12*
*24-Aug to 29-Aug*
*EMC*
https://bit.ly/31mjKol
Join with Google Meet: https://meet.google.com/qrt-wwnd-jpw

216877