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
    new_sen = sen.translate(sen.maketrans("","", string.punctuation))
    new_sen = list(new_sen.split(" "))
    longest_word = new_sen[0]
    for i in new_sen:
        if len(longest_word) >= len(i):
            longest_word = longest_word
        else:
            longest_word = i
    return longest_word

print(LongestWord(input()))