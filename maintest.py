import kata
import unittest


class TestOperations(unittest.TestCase):

    def test_syntax(self):
        self.assertRaises(kata.FluentSyntaxError, lambda: kata.Cal.one.two.three)
        self.assertRaises(kata.FluentSyntaxError, lambda: kata.Cal.one.plus.minus.two)

    def test_add(self):
        self.assertEqual(kata.Cal.new.one.plus.two, 3)
        self.assertEqual(kata.Cal.new.zero.plus.two, 2)
        self.assertEqual(kata.Cal.new.nine.plus.two, 11)

    def test_subtract(self):
        self.assertEqual(kata.Cal.new.one.minus.two, -1)
        self.assertEqual(kata.Cal.new.zero.minus.two, -2)
        self.assertEqual(kata.Cal.new.nine.minus.two, 7)

    def test_multiply(self):
        self.assertEqual(kata.Cal.new.one.times.two, 2)
        self.assertEqual(kata.Cal.new.zero.times.two, 0)
        self.assertEqual(kata.Cal.new.nine.times.two, 18)

    def test_divide(self):
        self.assertEqual(kata.Cal.new.one.divided_by.two, 0)
        self.assertEqual(kata.Cal.new.zero.divided_by.two, 0)
        self.assertEqual(kata.Cal.new.nine.divided_by.two, 4)
        self.assertRaises(ZeroDivisionError, lambda: kata.Cal.new.nine.divided_by.zero)

if __name__ == '__main__':
    unittest.main()
