from faker import Faker
fake = Faker('en_US')
# print(fake.text())

def automations(file):
    with open(file,'r') as file:
        print(file.read())






automations('automation/assets/potential-contacts.txt')        