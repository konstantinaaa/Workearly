"""
Basic Assignment Exercise 1
Print the sum of the first and last elements in the given list.
The list's length may vary throughout the different test cases.
Examples
Input: [1,2,3,4,5]
Output: 6
Input: [56,43,87,34,675,2]
Output: 58
"""
def BasicAssignmentExercise1(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + arr[-1]


# keep this function call here
print(BasicAssignmentExercise1([563, 134, 5636, 2313, 134, 2]))