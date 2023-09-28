"""
Have the function Palindrome(str) take
the str parameter being passed and return
the string true if the parameter is a palindrome,
(the string is the same forward as it is backward)
otherwise return the string false. For example:
"racecar" is also "racecar" backwards. Punctuation
and numbers will not be part of the string.
Examples
Input: "never odd or even"
Output: true
Input: "eye"
Output: true
"""
def Palindrome(strParam):
    # Remove spaces and convert to lowercase
    new_str = "".join(strParam.split()).lower()

    # Check if the cleaned string is equal to its reverse
    if new_str == new_str[::-1]:
        return True
    else:
        return False
    

# keep this function call here
print(Palindrome(input()))
