def arabic_to_roman(number):
    result_roman_number = ''
    if number == 6:
        result_roman_number = 'VI'
    elif number == 5:
        result_roman_number = 'V'
    elif number == 4:
        result_roman_number = 'IV'
    else:
        for i in range(number):
            result_roman_number += 'I'

    return result_roman_number

