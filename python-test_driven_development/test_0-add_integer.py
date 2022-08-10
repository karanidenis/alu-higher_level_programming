import unittest
import add_integer


class TestAdd(unittest.TestCase):

    def test_for_int_numbers(self):
        self.assertEqual(add_integer(2, 2), 4)

    def test_for_float_numbers(self):
        self.assertEqual(add_integer(2.5, 5.4), 7.9)

    def test_for_tuple(self):
        with self.assertRaises(TypeError):
            add_integer('1', 3)

    def test_for_str(self):
        with self.assertRaises(TypeError):
            add_integer(2, 'hi')

    def test_for_negative_as_subtraction(self):
        self.assertEqual(add_integer(3, -4), -1)

    def test_add_number_and_list(self):
        with self.assertRaises(TypeError):
            add_integer(2, [])

    def test_passing_none(self):
        with self.assertRaises(TypeError):
            add_integer(None)

    def test_for_overflow(self):
        with self.assertRaises(OverflowError):
            add_integer(float('inf', 0))

    def test_for_Nan(self):
        with self.assertRaises(ValueError):
            add_integer(3, float('Nan'))


if __name__ == '__main__':
    unittest.main()
