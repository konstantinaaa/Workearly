"""
Have the function LetterCapitalize(str)
take the str parameter being passed and
capitalize the first letter of each word.
Words will be separated by only one space.
Examples
Input: "hello world"
Output: Hello World
Input: "i ran there"
Output: I Ran There
"""
import string
def LetterCapitalize(strParam):
    return string.capwords(strParam)
print(LetterCapitalize(input()))