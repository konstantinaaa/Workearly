"""
Have the function ExOh(str) take the str
parameter being passed and return the string
true if there is an equal number of x's and o's,
otherwise return the string false. Only these two
letters will be entered in the string, no punctuation
or numbers. For example: if str is "xooxxxxooxo" then
the output should return false because there are 6 x's and 5 o's.
Examples
Input: "xooxxo"
Output: true
Input: "x"
Output: false
"""
def ExOh(strParam):
    x = strParam.count("x")
    o = strParam.count("o")
    if x == o:
        return True
    else:
        return False
print(ExOh(input()))
