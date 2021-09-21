# Sign your name:________________
# In all the short programs below, do a good job communicating with your end user!
import math
math.pi

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.

name= input("what is your name ")
print("hello", name)
print("")

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base= float(input("what is the base "))
height= float(input("what is the height "))
print("the area of this triangle is", base*height/2)
print("")

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius= float(input("what is the radius "))
print("the radius is", 2*math.pi*radius)
print("")

# 4. Ask a user for an integer and then print the square root.
number= float(input("gimme an integer"))
print("the square root is", number**0.5)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass=float(input("what is the mass"))
acceleration=float(input("what is the acceleration"))
print("the force is", mass*acceleration)
print("get it?")
