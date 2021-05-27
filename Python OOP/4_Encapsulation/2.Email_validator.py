import re


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def validate(self, email):
        (name, mail, domain) = re.split(r'[@.]', email)
        return self.__validate_name(name) and self.__validate_mail(mail) and self.__validate_domain(domain)

    def __validate_name(self, name):
        return name and self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains




