from automation import __version__
from automation.automation import *

def test_version():
    assert __version__ == '0.1.0'


def test_automation_number_1():
    actual = automations('automation/assets/potential-contacts.txt')
    expected = '070-531-008'
    assert actual[0] == expected

# '070-531-008'


def test_automation_number_2():
    actual = automations('automation/assets/potential-contacts.txt')
    expected = '660-537-521'
    assert actual[1] == expected


def test_automation_email_1():
    actual = emails('automation/assets/potential-contacts.txt')
    expected = 'zmyers@yahoo.com'
    assert expected == actual[0]
#'zmyers@yahoo.com'

def test_automation_email_2():
    actual = emails('automation/assets/potential-contacts.txt')
    expected = 'williamsdanielle@hotmail.com'
    assert expected == actual[1]

    