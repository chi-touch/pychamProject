import collection4


def test_that_list_has_duplicate_elements():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers1 = [2, 3, 4, 6]
    duplicates = [1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10]
    list_duplicate = collection4.duplicate_list(duplicates)
    assert duplicates == list_duplicate


