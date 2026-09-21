# #Q1-->Write a program to print Twinkle Twinkle Little star poem in python.
# print("Twinkle Twinkle Little Star")
# print("How I Wonder What You Are!")
# print("Up above the world so high,")
# print("Like a diamond in the sky.")

# #Q2-->Use REPL and print the table of 5 using it.
# for i in range(1,11):
#     print(5*i)

# #Q3-->Install an external module and use it to perform an operation of your interest.
import pyttsx3
engine =pyttsx3.init()
engine.say("Hello,welcome to python Programming!")
engine.runAndWait()
 
# #Q4-->Write a program to print the contents of a directory using the os module.
# import os
# directory = os.listdir()
# print(directory)

# #Q5-->Label the program written in Problem 4 with comments.
# import os
# #Get the list of files and folders 
# directory = os.listdir()
# #print the contents of the directory
# print(directory)