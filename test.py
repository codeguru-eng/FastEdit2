# Python3 program to validate
# HTML tag using regex.
# using regular expression
import re

# Function to validate
# HTML tag using regex.
def isValidHTMLTag(str):

    # Regex to check valid
    # HTML tag using regex.
    regex = "<(\"[^\"]*\"|'[^']*'|[^'\">])*>"
    
    # Compile the ReGex
    p = re.compile(regex)
    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
# Driver code

# Test Case 1:
str1 = "<input value = '>'>"
print(isValidHTMLTag(str1))

# Test Case 2:
str2 = "< br/>"
print(isValidHTMLTag(str2))