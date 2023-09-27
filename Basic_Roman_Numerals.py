'''
Have the function BasicRomanNumerals(str) read str which will be a string of Roman numerals. The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. In Roman numerals, to create a number like 11 you simply add a 1 after the 10, so you get XI. But to create a number like 19, you use the subtraction notation which is to add an I before an X or V (or add an X before an L or C). So 19 in Roman numerals is XIX.

The goal of your program is to return the decimal equivalent of the Roman numeral given. For example: if str is "XXIV" your program should return 24
Examples
Input: "IV"
Output: 4
Input: "XLVI"
Output: 46
'''
def BasicRomanNumerals(strParam):
  # Define a dictionary that maps Roman numeral characters to their numeric values.
  roman_numerals = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
  }

  # Initialize total to keep track of the final integer value and prev_value to track the previous character's value.
  total = 0
  prev_value = 0

  for numeral in strParam:
    value = roman_numerals[numeral]

    # Compare the current value with the previous value.
    if value > prev_value:
      # If the current value is greater than the previous value, it means subtraction is required.
      # To account for this, subtract twice the previous value from the total.
      total += value - 2 * prev_value
    else:
      # If the current value is less than or equal to the previous value, simply add it to the total.
      total += value

    # Update prev_value for the next iteration.
    prev_value = value

  return total


print(BasicRomanNumerals(input()))
