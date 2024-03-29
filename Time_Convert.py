"""
Have the function TimeConvert(num) take the num
parameter being passed and return the number of
hours and minutes the parameter converts to
(ie. if num = 63 then the output should be 1:3).
Separate the number of hours and minutes with a colon.
Examples
Input: 126
Output: 2:6
Input: 45
Output: 0:45
"""
def TimeConvert(num):
    num = int(num)
    hours = num // 60
    minutes = num % 60
    return f"{hours}:{minutes}"
print(TimeConvert(input()))