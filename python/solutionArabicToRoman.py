def arabic_to_roman(number):

    arabic_roman_mapping = {
        9: 'IX',
        5: 'V',
        4: 'IV'
    }

    remaining = number
    result_roman_number = ''

    for arabic, roman in arabic_roman_mapping.items():
        remaining, result_roman_number = append_roman_numerals(remaining, arabic, roman, result_roman_number)

    for i in range(remaining):
        result_roman_number += 'I'

    return result_roman_number


def append_roman_numerals(arabic, arabicKeyValue, romanKeyValue, romanDigitsBuilder):
    result = arabic
    if result >= arabicKeyValue:
        romanDigitsBuilder += romanKeyValue
        result -= arabicKeyValue
    return result, romanDigitsBuilder


