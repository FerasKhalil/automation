from faker import Faker
import re
fake = Faker('en_US')
# print(fake.text())
potentional_contacts = ''


def automations(file):


    phone_number = fake.phone_number()
    phone_number_lister = []
    shape_of_phone_number = "[\d]{3}-[\d]{3}-[\d]{3}"

    with open(file,'r') as file:
        file = file.read()
        get_phone_numbers = re.findall(shape_of_phone_number,file)

    for phone_number in get_phone_numbers:
        if phone_number not in phone_number_lister:
            phone_number_lister.append(phone_number)   
    with open('automation/assets/phone_number_lister.txt','w') as file:
        for phone_number in phone_number_lister:
            file.write(phone_number)
    return phone_number_lister


    
    # with open(file,'r') as file:
    #     # print(file.read())
    #     file = file.read()
    #     get_phone_numbers = re.findall(phone_shape,file)

    # with open(file,'r') as file:
    #     # print(file.read())
    #     file = file.read()
    #     get_phone_numbers = re.findall(shape_of_phone_number,file)

def emails(file):

    email = fake.email()
    email_regex = "[1-9a-z]*@[a-z]*.[a-z]*"
    emails_lister = []


    with open(file,'r') as file:
        file = file.read()
        get_emails = re.findall(email_regex,file)
    for email in get_emails:
        if email  not in emails_lister:
            emails_lister.append(email)
    with open('automation/assets/emails.txt','w') as file:
        for email in emails_lister:
            file.write(email)
    return emails_lister                    







if __name__ == "__main__":
    print(automations('automation/assets/potential-contacts.txt'))
    print(emails("automation/assets/potential-contacts.txt"))        