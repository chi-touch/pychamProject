import task1


def test_that_letters_can_be_replaced():
    # letter1 = 'abc'
    # letter2 = 'xyz'
    # result = 'xyc abz'
    # assert result == task1.replace_letters(letter2, letter1)
    #
    # num1 = 'chi'
    # num2 = 'day'
    # answer = 'dai chy'
    # assert answer == task1.replace_letters(num2, num1)

    last1 = 'abcde'
    last2 = 'lmnop'
    result2 = 'lmcde abnop'
    assert result2 == task1.replace_letters(last2, last1)
