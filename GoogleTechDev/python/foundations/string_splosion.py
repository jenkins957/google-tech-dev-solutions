"""
Given a non-empty string like "Code" return a string like "CCoCodCode"
"""


import unittest


def string_splosion(input_string):
    exploded_string = ''
    for i in range(len(input_string)):
        exploded_string += input_string[:i + 1]

    return exploded_string


class StringSplosionTests(unittest.TestCase):
    def test_should_explode_string(self):
        self.assertEqual('CCoCodCode', string_splosion('Code'))
        self.assertEqual('aababc', string_splosion('abc'))
        self.assertEqual('aab', string_splosion('ab'))
        self.assertEqual('x', string_splosion('x'))
        self.assertEqual('ffafadfade', string_splosion('fade'))
        self.assertEqual('TThTheTherThere', string_splosion('There'))
        self.assertEqual('KKiKitKittKitteKitten', string_splosion('Kitten'))
        self.assertEqual('BByBye', string_splosion('Bye'))
        self.assertEqual('GGoGooGood', string_splosion('Good'))
        self.assertEqual('BBaBad', string_splosion('Bad'))


if __name__ == '__main__':
    unittest.main()
