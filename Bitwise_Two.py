"""
Have the function BitwiseTwo(strArr) take the array of
strings stored in strArr, which will only contain two
strings of equal length that represent binary numbers,
and return a final binary string that performed the bitwise
AND operation on both strings. A bitwise AND operation places
a 1 in the new string where there is a 1 in both locations in
the binary strings, otherwise it places a 0 in that spot.
For example: if strArr is ["10111", "01101"] then your program
should return the string "00101"
Examples
Input: ["100", "000"]
Output: 000
Input: ["10100", "11100"]
Output: 10100
"""
def BitwiseTwo(strArr):
    a = ""
    for i in range(len(strArr[0])):
        if (strArr[0][i] == '1') and (strArr[1][i] == '1'):
            a += '1'
        else:
            a += '0'
    return a


print(BitwiseTwo(["10111", "01101"]))
