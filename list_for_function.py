import random

random.seed(10)
numbers = []
numbers = [random.randint(1, 50)
           for numb in range(1, 10)]

count = 0
while count > 10:
    my_numbers = input("Enter numbers between 1 and 50:")
numbers += [count]
count += count
#print(numbers)


def my_number(numbers):
    count = 0
    for number in numbers:
        count +=1

    return count

def get_length(numbers):
    result = 0
    for number in numbers:sum +=1
    return result

def get_sum_of_even(numbers):
    return sum (numbers[1::2])

def get_sum_of_odd(numbers):
    return sum (numbers[::2])

def get_product_of_third_elements(numbers):
    product = 1
    for index in numbers:
        product *= numbers[index]
        return product

def sumz(numbz):
    total = 0
    for number in numbz:
        total += number
        return total

def get_average (numbers):
    return sumz(numbers)/len(numbers)

def get_maximum(numbers):
    return max(numbers)
def get_minimum(numbers):
    minimum =numbers[0]
    for element in numbers:
        if element < minimum:
            minimum = element
            return minimum

def get_String(words):
    for word in words:
        if len(word) >= 2 and word [0] == word[-1]:
            return [word]

def get_String(word):
    result = []
    for word in word:
        result.append(word)
        return result

