
def arabic_to_roman(number):

    arabic_roman_mappings = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    remaining = number
    result_roman_number = ''

    for arabic_original, roman_mapping in arabic_roman_mappings.items():
        remaining, result_roman_number = append_roman_numerals(remaining, arabic_original, roman_mapping, result_roman_number)

    return result_roman_number


def append_roman_numerals(arabic, arabic_original, roman_mapping, result_roman_number):
    remaining = arabic
    while remaining >= arabic_original:
            remaining += roman_mapping
            remaining -= arabic_original
    return remaining, result_roman_number


