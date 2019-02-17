def arabic_to_roman(number):
    remaining = number
    result_roman_number = ''

    remaining, result_roman_number = append_roman_numerals(remaining, 9, 'IX', result_roman_number)
    remaining, result_roman_number = append_roman_numerals(remaining, 5, 'V', result_roman_number)
    remaining, result_roman_number = append_roman_numerals(remaining, 4, 'IV', result_roman_number)

    for i in range(remaining):
        result_roman_number += 'I'

    return result_roman_number


def append_roman_numerals(arabic, arabicKeyValue, romanKeyValue, romanDigitsBuilder):
    result = arabic
    if result >= arabicKeyValue:
        romanDigitsBuilder += romanKeyValue
        result -= arabicKeyValue
    return result, romanDigitsBuilder


