import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    # def max_integer(list=[]):
    def test_list_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_str(self):
        with self.assertRaises(TypeError):
            (max_integer([1, 2, 3, 'red']))

    def test_negative_int(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

