import kata
import unittest


class TestOperations(unittest.TestCase):

    def test_syntax(self):
        self.assertRaises(kata.FluentSyntaxError, lambda: kata.Cal.new.one.two.three)
        self.assertRaises(kata.FluentSyntaxError, lambda: kata.Cal.new.one.plus.minus.two)

    def test_add(self):
        self.assertEqual(kata.Cal.new.one.plus.two, 3)
        self.assertEqual(kata.Cal.new.zero.plus.two, 2)
        self.assertEqual(kata.Cal.new.nine.plus.two, 11)
        self.assertEqual(kata.Cal.new.twelve.plus.two, 14)

    def test_subtract(self):
        self.assertEqual(kata.Cal.new.one.minus.two, -1)
        self.assertEqual(kata.Cal.new.zero.minus.two, -2)
        self.assertEqual(kata.Cal.new.nine.minus.two, 7)
        self.assertEqual(kata.Cal.new.nineteen.minus.ten, 9)

    def test_multiply(self):
        self.assertEqual(kata.Cal.new.one.times.two, 2)
        self.assertEqual(kata.Cal.new.zero.times.two, 0)
        self.assertEqual(kata.Cal.new.nine.times.two, 18)
        self.assertEqual(kata.Cal.new.eleven.times.two, 22)

    def test_divide(self):
        self.assertEqual(kata.Cal.new.one.divided_by.two, 0)
        self.assertEqual(kata.Cal.new.zero.divided_by.two, 0)
        self.assertEqual(kata.Cal.new.nine.divided_by.two, 4)
        self.assertEqual(kata.Cal.new.fourteen.divided_by.two, 7)
        self.assertRaises(ZeroDivisionError, lambda: kata.Cal.new.nine.divided_by.zero.result)

    def test_hundred(self):
        self.assertEqual(kata.Cal.new.one.hundred.times.two, 200)
        self.assertEqual(kata.Cal.new.one.hundred.times.two.hundred, 20000)
        self.assertEqual(kata.Cal.new.one.hundred.plus.one, 101)


if __name__ == '__main__':
    unittest.main()
