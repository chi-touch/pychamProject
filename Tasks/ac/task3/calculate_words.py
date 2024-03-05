def calculate_words(words):
    letters = 0
    digits = 0
    for word in words:
        if word.isalpha():
            letters += 1
        if word.isdigit():
            digits += 1

    return f"LETTERS {letters} DIGITS {digits}"


print(calculate_words('hello world 123'))


def calculate_words(sample):
    upper = 0
    lower = 0
    for word in sample:
        if word.isupper():
            upper += 1
        if word.islower():
            lower += 1
    return f"UPPER {upper} LOWER {lower}"


print(calculate_words('Hello world'))
