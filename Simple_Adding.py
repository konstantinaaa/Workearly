"""
Have the function SimpleAdding(num)
add up all the numbers from 1 to num.
For example: if the input is 4 then your program
should return 10 because 1 + 2 + 3 + 4 = 10.
For the test cases, the parameter num will be any number
from 1 to 1000.
Examples
Input: 12
Output: 78
Input: 140
Output: 9870
"""
def SimpleAdding(num):
    num = int(num)
    num_list = []
    for i in range(1, num + 1):
        num_list.append(i)
    return sum(num_list)

# keep this function call here
print(SimpleAdding(input()))