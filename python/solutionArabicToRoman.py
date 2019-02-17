def arabic_to_roman(number):
    remaining = number
    result_roman_number = ''
    if remaining >= 5:
        result_roman_number = 'V'
        remaining -= 5
    elif number == 4:
        result_roman_number = 'IV'
        remaining -= 4
    for i in range(remaining):
        result_roman_number += 'I'

    return result_roman_number

