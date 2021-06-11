import re

potentials = open("assets/potential-contacts.txt")
# print(potentials.read())

email_pattern = re.compile('\S+@\S+')
emails_only = re.findall(email_pattern,potentials)

print(emails_only)