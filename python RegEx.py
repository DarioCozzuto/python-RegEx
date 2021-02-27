#https://www.w3schools.com/python/python_regex.asp
#Python has a built-in package called re, which can be used to work with Regular Expressions.

#Import the re module:
import re 


#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

