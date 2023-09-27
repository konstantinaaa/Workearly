"""
Basic Assignment Exercise 2
Use the input as x and the function
shown below in order to produce the needed integer results.
F(x) = (x+2)*(x/5)
Examples
Input: 5
Output: 7
Input: 10
Output: 24
"""
def BasicAssignmentExercise2(num):
    num = int(num)
    return int((num + 2)*(num/5))


print(BasicAssignmentExercise2(input()))
