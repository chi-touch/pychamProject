import list_for_function


class MyTestCase:
    def test_that_function_is_not_none(self):
        numbers = list(range(10,20))
        assert 10 == list_for_function.get.length(numbers)
        assert 25 == list_for_function.get.length(numbers)

    def test_that_function_return_sum_of_even_numbers(self):
        numbers = list(range(10,20))
        assert 75 == list_for_function.get.length(numbers)

    def test_that_fuction_returns_sum_of_odd_numbers(self):
        numbers = list(range(10,20))
        assert 70 == list_for_function.get.length(numbers)

    def test_that_function_return_product_of_third_elements(self):
        numbers = list(range(10,20))
        assert 3240 == list_for_function.get_length(numbers)

    def test_that_function_return_average(self):
        numbers = list(range(10,20))
        assert 14.5 == list_for_function.get_length(numbers)

    def test_that_function_return_largest_elements(self):
        numbers = list(range(10,20))
        assert 19 == list_for_function.get_length(numbers)

    def test_that_function_return_smallest_elements(self):
        numbers = list(range(10,20))
        assert 10 == list_for_function.get_length(numbers)

    def test_that_function_return_list_of_String(self):
        names = ['hannah', 'praise', 'balikis','bolaji']
        assert ['hannah']== list_for_function.get_String(names)
        assert ['hannah','miriam'] ==list_for_function.get_String(names)








