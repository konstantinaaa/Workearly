"""
Have the function LongestWord(sen) take the sen
parameter being passed and return the longest word
in the string. If there are two or more words that
are the same length, return the first word from the
string with that length.
Ignore punctuation and assume sen will not be empty.
Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
"""
import string

def LongestWord(sen):
    # Remove punctuation from the input string
    new_sen = sen.translate(sen.maketrans("", "", string.punctuation))

    # Split the string into words
    word_list = new_sen.split()

    # Initialize the longest_word to the first word
    longest_word = word_list[0]

    for word in word_list:
        # Compare the length of the current word with the length of the longest_word
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

print(LongestWord(input()))
