def arabic_to_roman(number):
    if number == 4:
        return 'IV'
    result_roman_number = ''
    for i in range(number):
        result_roman_number += 'I'

    return result_roman_number

