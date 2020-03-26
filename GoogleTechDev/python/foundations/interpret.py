"""
https://codingbat.com/prob/p294185

Write a simple interpreter which understands "+", "-", and "*" operations. Apply the operations in order using command/arg pairs starting with the initial value of `value`. If you encounter an unknown command, return -1.


interpret(1, ["+"], [1]) → 2
interpret(4, ["-"], [2]) → 2
interpret(1, ["+", "*"], [1, 3]) → 6
"""


import unittest


def interpret(value, commands, args):
    next_value = value;

    for i in range(len(commands)):
        if not is_valid_operand(commands[i]):
            return -1;

        next_value = calculate(next_value, args[i], commands[i] )
    return next_value;


def is_valid_operand(op):
    return '+' in op or '-' in op or '*' in op


def calculate(p1, p2, op):
    if '+' == op:
        return p1 + p2;
    if '-' == op:
        return p1 - p2;
    if '*' == op:
        return p1 * p2;


class InterpretTests(unittest.TestCase):
    def test_interpreter(self):
        self.assertEqual(2, interpret(1, ['+'], [1]))
        self.assertEqual(2, interpret(4, ['-'], [2]))
        self.assertEqual(6, interpret(1, ['+', '*'], [1, 3]))
        self.assertEqual(12, interpret(3, ['*'], [4]))
        self.assertEqual(-1, interpret(0, ['?'], [4]))
        self.assertEqual(4, interpret(1, ['+', '*', '-'], [1, 3, 2]))


if __name__ == '__main__':
    unittest.main()
