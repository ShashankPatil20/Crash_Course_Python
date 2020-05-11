"""
1.Question 1
The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can
be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization.
Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even".
Fill in the blanks in this function to return True if the passed
string is a palindrome, False if not.

"""


def is_palindrome(input_string):
    new_string = input_string.split()
    new_string = "".join(new_string).lower()
    reverse_string = new_string[::-1]

    if new_string == reverse_string:
        return True
    else:
        return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True

"""
2.Question 2
Using the format method, fill in the gaps in the convert_distance function so that it returns 
the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) 
should return "12 miles equals 19.2 km".
"""
def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

"""
4.Question 4
Fill in the gaps in the nametag function so that it uses the format method to return first_name and the 
first initial of last_name followed by a period. 
For example, nametag("Jane", "Smith") should return "Jane S."
"""

"""Fill in the gaps in the nametag function so that it uses the format method to return first_name 
and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."
"""

def nametag(first_name, last_name):
	return("{} {[0]}.".format(first_name,last_name))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."