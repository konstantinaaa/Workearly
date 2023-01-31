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
    for i in range(len(strParam)+1):
        if strParam[i] == strParam[-(i+1)]:
            return True
        else:
            return False

# keep this function call here
print(Palindrome(input()))