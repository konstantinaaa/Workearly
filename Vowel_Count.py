"""
Have the function VowelCount(str) take the
str string parameter being passed and return
the number of vowels the string contains
(ie. "All cows eat grass and moo" would return 8).
 Do not count y as a vowel for this challenge.
Examples
Input: "hello"
Output: 2
Input: "coderbyte"
Output: 3
"""
def VowelCount(strParam):
    count = 0
    for i in strParam.lower():
        if i in "aeuio":
            count += 1
    return count

print(VowelCount(input()))