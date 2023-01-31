"""
Have the function AlphabetSoup(str) take the
str string parameter being passed and return
the string with the letters in alphabetical order
(ie. hello becomes ehllo). Assume numbers and punctuation
symbols will not be included in the string.
Examples
Input: "coderbyte"
Output: bcdeeorty
Input: "hooplah"
Output: ahhloop
"""
def AlphabetSoup(strParam):
    strParam = sorted(strParam)
    string = ""
    return string.join(strParam)
print(AlphabetSoup(input()))