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
    return phoneNumber[index-1]

def add_email(email):
    emailAddress.append(email)

def get_email(index):
    return emailAddress[index -1]

def add_total_Contact(contactName, phoneNumber, emailAddress):
    totalContact.append((contactName,phoneNumber,emailAddress))

def get_total_contact(contactName,phoneNumber,emailAddress):
    return totalContact[contactName,phoneNumber,emailAddress]
def main():
    name = str(input("Enter your first name and surname:"))
    phone_N0 = str(input("Enter your your phone number:"))
    Email_adress = str(input("Enter your email address:"))

    print(str.format("Name:"
                  "Phone_number:",
                  'Email_address:',
                  name, phone_N0, Email_adress))

    add_contact_name(name)
    add_phone_number(phone_N0)
    add_email(Email_adress)
    add_total_Contact(contactName,phoneNumber,emailAddress)

    print("your details is:", get_contact_name(index=1),get_phone_number(index=1),get_email(index=1))


main()