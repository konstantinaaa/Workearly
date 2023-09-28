"""
Basic Assignment Exercise 5
Print the amount of numbers contained within the given string.
If two or more numbers exist next to each other, their values need to be combined to a single number.
Examples
Input: "This string has 1 number!"
Output: 1
Input: "2 + 13 = 15"
Output: 3
Input: "*2*3*1 2*51" 
Output: 5
Input: "Th1s 1s 4 w0rk34rly 3x3rc1s3!"
Output: 9
Input: "0 x 1 = 0. 0 x 2 = 0" 
Output: 6
Input: "5 is a natural number. 5 is an odd number. 5 is the only prime number that is the sum of two consecutive prime numbers. namely 2 and 3. 5 is also the only prime number to end with 5 in ones place." 
Output: 7
"""

def BasicAssignmentExercise5(strParam):
    # Initialize variables to keep track of numbers and the final count
    current_number = ""
    count = 0

    for char in strParam:
        # Check if the character is a digit
        if char.isdigit():
            current_number += char  # Add the digit to the current number and if the character is not a digit, it means we have reached the end of a number
        elif len(current_number) != 0:  # counts the numbers and reset the counter number
            count += 1  
            current_number = ""  # Reset current_number

    # Check if there's a remaining number at the end of the string
    if len(current_number) != 0:
        count += 1

    return count




print(BasicAssignmentExercise5(input()))
