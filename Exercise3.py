"""
Basic Assignment Exercise 3
How many times can the letter e be found in the given string arrays?

Examples
Input: ["This is", "an array", "of strings!"]
Output: 0
Input: ["Python exercises", "are", "so much", "fun!"]
Output: 4
1. For input ["It is difficult to", "understand the lengths he would", "go to remain", "rich."] the output was incorrect. The correct output is 4

2. For input ["The overpass", "went under the highway", "and into a", "secret world."] the output was incorrect. The correct output is 5
"""
def BasicAssignmentExercise3(strArr):
       strArr = str(strArr)
       return strArr.count("e")


print(BasicAssignmentExercise3(input()))