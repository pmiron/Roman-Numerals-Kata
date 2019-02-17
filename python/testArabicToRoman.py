import unittest

from solutionArabicToRoman import arabic_to_roman


class ArabicToRomanTests(unittest.TestCase):
    def test_number_1_is_I(self):
        self.assertEqual(arabic_to_roman(1), 'I')

    def test_number_2_is_not_I(self):
        self.assertNotEqual(arabic_to_roman(2), 'I')

    def test_number_2_is_II(self):
        self.assertEqual(arabic_to_roman(2), 'II')

    def test_number_3_is_III(self):
        self.assertEqual(arabic_to_roman(3), 'III')

    def test_number_4_is_IV(self):
        self.assertEqual(arabic_to_roman(4), 'IV')

    def test_number_5_is_V(self):
        self.assertEqual(arabic_to_roman(5), 'V')

    def test_number_6_is_VI(self):
        self.assertEqual(arabic_to_roman(6), 'VI')
