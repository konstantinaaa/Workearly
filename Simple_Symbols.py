"""
Have the function SimpleSymbols(str) take the
str parameter being passed and determine if it
is an acceptable sequence by either returning the
string true or false. The str parameter will be composed
of + and = symbols with several characters between them
(ie. ++d+===+c++==a) and for the string to be true each letter
must be surrounded by a + symbol. So the string to the left
would be false. The string will not be empty and will have
at least one letter.
Examples
Input: "+d+=3=+s+"
Output: true
Input: "f++d+"
Output: false
"""
def SimpleSymbols(strParam):
    # Check if the first or last character is a letter
    if strParam[0].isalpha() or strParam[-1].isalpha():
        return False

    for i in range(1, len(strParam) - 1):
        # Check if the current character is a letter
        if strParam[i].isalpha():
            # Check if the characters to the left and right are not '+'
            if strParam[i - 1] != '+' or strParam[i + 1] != '+':
                return False

    return True

