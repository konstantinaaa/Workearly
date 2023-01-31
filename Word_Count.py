"""
Have the function WordCount(str) take the str string
parameter being passed and return the number of words
the string contains
(e.g. "Never eat shredded wheat or cake" would return 6).
Words will be separated by single spaces.
Examples
Input: "Hello World"
Output: 2
Input: "one 22 three"
Output: 3
"""
def WordCount(strParam):
    strParam = strParam.split(" ")
    count = 0
    for i in strParam:
        count += 1
    return count
print(WordCount(input()))