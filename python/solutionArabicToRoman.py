def arabic_to_roman(number):

    arabic_roman_mapping = {
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    remaining = number
    result_roman_number = ''

    for arabic, roman in arabic_roman_mapping.items():
        remaining, result_roman_number = append_roman_numerals(remaining, arabic, roman, result_roman_number)

    return result_roman_number


def append_roman_numerals(arabic, arabic_key_value, roman_key_value, roman_digits_builder):
    result = arabic
    while result >= arabic_key_value:
            roman_digits_builder += roman_key_value
            result -= arabic_key_value
    return result, roman_digits_builder


