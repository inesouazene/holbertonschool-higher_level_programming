#!/usr/bin/python3


def sum_elements_less_than_max(elements):
    sum_of_elements = 0
    max_element = max(elements)

    for element in elements:
        if max_element > element:
            sum_of_elements += element

    return max_element - sum_of_elements


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    numeral_keys = list(roman_numerals.keys())

    total_value = 0
    last_value = 0
    current_values = [0]

    for char in roman_string:
        if char in numeral_keys:
            current_value = roman_numerals[char]
            if current_value <= last_value:
                total_value += sum_elements_less_than_max(current_values)
                current_values = [current_value]
            else:
                current_values.append(current_value)
            last_value = current_value

    total_value += sum_elements_less_than_max(current_values)

    return total_value
