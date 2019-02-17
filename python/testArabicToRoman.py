import unittest

from solutionArabicToRoman import arabic_to_roman


class ArabicToRomanTests(unittest.TestCase):
    def test_number_1_is_I(self):
        self.assertEqual(arabic_to_roman(1), 'I')

    def test_number_2_is_not_I(self):
        self.assertNotEqual(arabic_to_roman(2), 'I')

    def test_number_2_is_II(self):
        self.assertEqual(arabic_to_roman(2), 'II')
