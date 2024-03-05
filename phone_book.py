contactName = []
phoneNumber = []
emailAddress = []
totalContact = []


def add_contact_name(name):
    contactName.append(name)


def get_contact_name(index):
    return contactName[index - 1]


def add_phone_number(number):
    phoneNumber.append(number)


def get_phone_number(index):
    return phoneNumber[index - 1]


def add_email(email):
    emailAddress.append(email)


def get_email(index):
    return emailAddress[index - 1]

def add_contact(contactName, phoneNumber, emailAddress):
    contact ={'contactName': contactName, 'phoneNumber':phoneNumber, 'emailAddress': emailAddress}
    totalContact.append(contact)
    return "Contact successfully added"
def add_total_Contact(contactName, phoneNumber, emailAddress):
    totalContact.append((contactName, phoneNumber, emailAddress))

def get_total_Contact(contactName, phoneNumber, emailAddress):
    return totalContact[contactName, phoneNumber, emailAddress];

def main():
    while totalContact!= -1:
        contactName = str(input("Enter your first name and surname:"))
        phoneNumber = str(input("Enter your your phone number:"))
        emailAddress = str(input("Enter your email address:"))
        return "you have successfully saved your contact"

def search_contact(contactName):
    contactName = str(input("Enter your first name and surname:"))
    return contactName in totalContact

    add_contact_name(contactName)
    add_phone_number(phoneNumber)
    add_email(emailAddress)
    add_total_Contact(contactName, phoneNumber, emailAddress)

    print("your details is:", get_contact_name(index=1), get_phone_number(index=1), get_email(index=1))



#main()


