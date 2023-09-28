"""
Have the function LargestPair(num) take
the num parameter being passed and determine
the largest double digit number within the
whole number. For example: if num is 4759472
then your program should return 94 because that
is the largest double digit number. The input will
always contain at least two positive digits.
Examples
Input: 453857
Output: 85
Input: 363223311
Output: 63
"""

def LargestPair(num):
    num = str(num)
    num1 = num[:-1] # it removes the last character from the string.
    m = max(num1)
    p = num.find(m)
    return f'{m}{num[p+1]}'


print(LargestPair(589))
