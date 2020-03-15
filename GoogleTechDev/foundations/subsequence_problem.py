"""
The Challenge

Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
"""


import unittest


def find_longest_subsequence(input_string, words):
    longest_word = ''

    #Optimisation, by sorting words in decending order of length, first one found must be longest
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        if is_subsequence(input_string, word):
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word


def is_subsequence(input_string, word):
    offset = 0
    for c in word:
        offset = __find_position_first_occurrence(input_string, c, offset);
        if offset == -1:
            return False
    return True


def __find_position_first_occurrence(input_string, c, offset=0):
    for index, char in enumerate(input_string[offset:]):
        if c == char:
            return index
    return -1


class SubsequenceProblemTests(unittest.TestCase):
    def test_should_find_longest_subsequence_from_list_if_words(self):
        words = ["able", "ale", "apple", "bale", "kangaroo"]
        self.assertEquals('apple', find_longest_subsequence('abppplee', words))

    def test_should_be_a_subsequence_of_input_string(self):
        self.assertTrue(is_subsequence('abppplee', 'apple'))
        self.assertTrue(is_subsequence('abppplee', 'able'))
        self.assertTrue(is_subsequence('abppplee', 'ale'))

    def test_should_not_be_a_subsequence_of_input_string_wrong_order(self):
        self.assertFalse(is_subsequence('abppplee', 'bale'))
        self.assertFalse(is_subsequence('abppplee', 'pale'))

    def test_should_not_be_a_subsequence_of_input_string_wrong_characters(self):
        self.assertFalse(is_subsequence('abppplee', 'tree'))
        self.assertFalse(is_subsequence('abppplee', 'banana'))

    def test_should_not_be_a_subsequence_of_input_string_missing_characters(self):
        self.assertFalse(is_subsequence('abppplee', 'apples'))
        self.assertFalse(is_subsequence('abppplee', 'male'))


if __name__ == '__main__':
    unittest.main()
