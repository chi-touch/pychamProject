import phone_book

def test_for_first_name():
    phone_book.add_contact_name('chichi')
    assert 'chichi' == phone_book.get_contact_name(1)

def test_for_last_name():
    phone_book.add_contact_name("david")
    assert 'david' == phone_book.get_contact_name(1)

def test_for_phone_number():
    phone_book.add_phone_number('08103722570')
    assert '08103722570' == phone_book.get_phone_number(1)

def test_for_email():
    phone_book.add_email('chichi@gmail.com')
    assert "chichi@gmail.com" == phone_book.get_email(1)
def test_multiple_names_collection():
    phone_book.add_contact_name('chichi')
    assert 'chichi' == phone_book.get_contact_name(1)
    phone_book.add_contact_name('chichi1')
    assert 'chichi1' == phone_book.get_contact_name(1)
    phone_book.add_contact_name('chichi2')
    assert 'chichi2' == phone_book.get_contact_name(1)
    phone_book.add_contact_name('chichi3')
    assert 'chichi3' == phone_book.get_contact_name(1)

#def add_contact_name(**args):
    # contact_name.append(**args)
def add_phone_number():
    pass
