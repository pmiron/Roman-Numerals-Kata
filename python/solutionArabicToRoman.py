def arabic_to_roman(number):
    result_roman_number = ''
    if number == 4:
        result_roman_number = 'IV'
    else:
        for i in range(number):
            result_roman_number += 'I'

    return result_roman_number

