"""
1.Question 1
Given a list of filenames, we want to rename all the files with the extension hpp to the extension h by generating a list of tuples of the form (old_name, new_name).

That is, given the following list of filenames

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

complete the starter code to generate the following newfilenames list of tuples

newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
"""


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for oldfilename in filenames:
  if ".hpp" in oldfilename:
    newfilenames.append((oldfilename,oldfilename.replace(".hpp",".h")))
  else:
    newfilenames.append((oldfilename,oldfilename))

print (newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]


"""
2.Question 2
The permissions of a file in a Linux system are split into three sets of three permissions: 
read, write, and execute for the owner, group, and others. Each of the three values can be expressed 
as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. 
Or it can be written with a string using the letters r, w, and x or - when the permission is not granted. 
For example: 640 is read/write for the owner, read for the group, and no permissions for the others; 
converted to a string, it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute 
for group and others; converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code 
convert a permission in octal format into a string format.

"""
def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

"""
3.Question 3
Fill in the gaps in the nametag function so that it uses the format method to return first_name and the 
first initial of last_name followed by a period. 
For example, nametag("Jane", "Smith") should return "Jane S."
"""

"""Fill in the gaps in the nametag function so that it uses the format method to return first_name 
and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."
"""

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result+="-"
    return result
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

"""
4.Question 4
Let's create a function that turns text into pig latin: a simple text transformation 
that modifies each word moving the first character to the end and appending 
"ay" to the end. For example, python ends up as ythonpay.
"""


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        texts = word[1:] + word[0] + "ay" + " "
        say += texts
        # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay

