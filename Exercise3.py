"""
Basic Assignment Exercise 3
How many times can the letter e be found in the given string arrays?

Examples
Input: ["This is", "an array", "of strings!"]
Output: 0
Input: ["Python exercises", "are", "so much", "fun!"]
Output: 4
"""
def BasicAssignmentExercise3(strArr):
       count = 0
       for i in strArr:
              if i == 'e':
                     count += 1
       return count
""" or 
def BasicAssignmentExercise3(strArr):
       return strArr.count("e")

print(BasicAssignmentExercise3(input()))
"""

print(BasicAssignmentExercise3(input()))

