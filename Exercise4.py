"""
Basic Assignment Exercise 4
Find the sum of all the list's elements, excluding the last one.

Afterwards, multiply the sum you found with the last element in the list.
Finally, convert the output to an integer.

Examples
Input: [1, 2, 3, 4, 5]
Output: 50
Input: [12, 12, 43, 54, 0]
Output: 0
4. For input [32, 22, 23, 32, 22, 32] the output was incorrect. The correct output is 4192

5. For input [1, 1, 1, 1, 1, 1, 1, 1, 1, 10] the output was incorrect. The correct output is 90

6. For input [16, 13, 15, 15, 21, 41, 71, 14, 19, 1230] the output was incorrect. The correct output is 276750

7. For input [5,-15, -75] the output was incorrect. The correct output is 750
"""
def BasicAssignmentExercise4(arr):
    new_arr = []
    i = 0
    while i < len(arr) - 1:
        new_arr.append(arr[i])
        i += 1
    s = sum(new_arr)
    return int(s*arr[-1])



print(BasicAssignmentExercise4([5,-15, -75]))