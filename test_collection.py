import collection


def test_that_set_is_not_empty():
    sum_collection = {1, 2, 3, 4, 5, 6, 7}
    assert 28 == collection.sum_of_set(sum_collection)


def test_that_set_can_remove_element():
    remove_item = {1, 2, 3, 4, 5, 6, 7}
    after_removal = {1, 2, 3, 4, 5, 7}
    list_result = collection.remove_number_from_set(remove_item, 8)
    assert after_removal == list_result


def test_that_it_can_accept_two_set():
    num_1 = {1, 2, 3, 4,}
    num_2 = {5, 6, 7}
    new_element = {1, 2, 3, 4, 5, 6, 7}
    list_result = collection.find_intersection(num_1, num_2, new_element)
    assert new_element == list_result



