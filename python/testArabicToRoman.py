import unittest

from solutionArabicToRoman import arabic_to_roman


class ArabicToRomanTests(unittest.TestCase):
    def test_number_1_is_I(self):
        self.assertEqual( 'I', arabic_to_roman(1))

    def test_number_2_is_not_I(self):
        self.assertNotEqual('I', arabic_to_roman(2))

    def test_number_2_is_II(self):
        self.assertEqual('II', arabic_to_roman(2))

    def test_number_3_is_III(self):
        self.assertEqual('III', arabic_to_roman(3))

    def test_number_4_is_IV(self):
        self.assertEqual('IV', arabic_to_roman(4))

    def test_number_5_is_V(self):
        self.assertEqual('V', arabic_to_roman(5))

    def test_number_6_is_VI(self):
        self.assertEqual('VI', arabic_to_roman(6))

    def test_number_7_is_VII(self):
        self.assertEqual('VII', arabic_to_roman(7))

    def test_number_8_is_VIII(self):
        self.assertEqual('VIII', arabic_to_roman(8))

    def test_number_9_is_IX(self):
        self.assertEqual('IX', arabic_to_roman(9))

    def test_number_10_is_X(self):
        self.assertEqual('X', arabic_to_roman(10))

    def test_number_11_is_XI(self):
        self.assertEqual('XI', arabic_to_roman(11))

    def test_number_14_is_XIV(self):
        self.assertEqual('XIV', arabic_to_roman(14))

    def test_number_19_is_XIX(self):
        self.assertEqual('XIX', arabic_to_roman(19))

    def test_number_38_is_XIX(self):
        self.assertEqual('XXXVIII', arabic_to_roman(38))

    def test_number_84_is_XIX(self):
        self.assertEqual('XXXXXXXXIV', arabic_to_roman(84))

    def test_number_99_is_XIX(self):
        self.assertEqual('XXXXXXXXXIX', arabic_to_roman(99))
