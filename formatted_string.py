# Format-string in python
#There are three ways in fpormatting string in python
# 1. Using % operator (old way)
name = "Abebe"
age = 36
print("My name is %s and I am %d years old." %(name,age))
#%s represent string
#%d represent integer
#%f represent float
#%x represent hexadecimal
#%o represent octal
#%e represent exponential
#%c represent character
#%r represent raw string
#%g represent general
#%a represent ascii
#%u represent unsigned decimal
#%i represent integer
# Method two str.format()
print("my name is {} . I am {} years old.".format(name,age))
# Everything is replaced by curly bracket in method two string format
# f-string
print(f"My name is {name}. I am {age} years old.")
# in f-string  we replace the value of the variable in curly bracket.
# f-string is the most recent way of formatting string in python
# Exercises
name = 'lydia'
age = 21
print("Hello,my name is %s and I am %d years old" %(name,age))
# Exercise 2
def multiplication_table(n):
    for i in range(1,11):
        print("%d * %d = %d" %(n,i,n*i))
multiplication_table(5)
# Exercise 3
radius = input("Enter the radius of the circle.")
radius = float(radius)
def area_of_circle(radius):
   
    area = 3.14*radius**2
    print(f"The area of the circle is {area}")
area_of_circle(7)

          