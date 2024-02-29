def sum_of_set(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def remove_number_from_set(numbers, number):
    if number in numbers:
        numbers.remove(number)
        return numbers

    return "none"


def find_intersection(num_1, num_2, new_element):
    num_1 | num_2
    return new_element






