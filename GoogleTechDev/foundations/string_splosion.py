"""
Given a non-empty string like "Code" return a string like "CCoCodCode"
"""


import unittest


def string_splosion(input_string):
    exploded_string = ''
    for i in range(1, len(input_string) + 1):
        exploded_string += input_string[:i]

    return exploded_string


class StringSplosionTests(unittest.TestCase):
    def test_should_explode_string(self):
        self.assertEquals('CCoCodCode', string_splosion('Code'))
        self.assertEquals('aababc', string_splosion('abc'))
        self.assertEquals('aab', string_splosion('ab'))
        self.assertEquals('x', string_splosion('x'))
        self.assertEquals('ffafadfade', string_splosion('fade'))
        self.assertEquals('TThTheTherThere', string_splosion('There'))
        self.assertEquals('KKiKitKittKitteKitten', string_splosion('Kitten'))
        self.assertEquals('BByBye', string_splosion('Bye'))
        self.assertEquals('GGoGooGood', string_splosion('Good'))
        self.assertEquals('BBaBad', string_splosion('Bad'))


if __name__ == '__main__':
    unittest.main()