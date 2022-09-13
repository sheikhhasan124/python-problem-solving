""" print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!") """


# problem-1 -----------
# print("aaaaaaaa\nbbbbbbbbb\n\tccccccc\n\t\tdddddddd")

# problem-2 -----------
""" import datetime
time = datetime.datetime.now()
print("date is",time) """

""" import datetime
time = datetime.datetime.now()
print("all time is",time)
print("year is", time.year)
print("day is", time.strftime("%A"))
print("month is", time.strftime("%B")) """

# problem -3 ---------
# Write a Python program which accepts the radius of a circle from the user and compute the area.
""" from math import pi
x = float(input("input the ridius of the circle:"))
print("the area of the circle " + str(x) + " is: "+ str(pi * x**2)) """

# problem -4 -------------
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

""" fname = input("enter first name : ")
lname = input("enter last name : ")
print(" Hello " + lname + " "+ fname) """

# problem -5 --------------
# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

""" values = input("give some comma seperate num : ")
list = values.split(",")
tuple = tuple(list)
print("List : ", list)
print("tuple : ", tuple) """

# problem -6 ------------
# Write a Python program to accept a filename from the user and print the extension of that.

""" fileName = input("enter a file name : ")
fExtention = fileName.split(".")
input("the extention of the file name is : " + repr( fExtention[-1])) """

# problem -7 ---------
# Write a Python program to display the first and last colors from the following list.
""" colourList = ["white", "blue", "black","green"]
print("%s %s"%(colourList[0], colourList[-1])) """

# problem - 8 -----------
# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
""" examDate = (10,11,2022)
print("the exam will start from : %i / %i / %i"%examDate) """

# problem 9 - -------------
""" x = int(input("input an integer: "))
n1 = int("%s" % x)
n2 = int("%s%s" % (x,x))
n3 = int("%s%s%s" % (x,x,x))
print(n1+n2+n3) """