def replace_letters(last1, last2):
    last1.replace(last1[:2], last2[:2])
    last2.replace(last2[:2], last1[:2])
    return last2.replace(last2[:2], last1[:2]) + " " + last1.replace(last1[:2], last2[:2])


last1 = 'abcde'
last2 = 'lmnop'
print(replace_letters(last2,last1))
