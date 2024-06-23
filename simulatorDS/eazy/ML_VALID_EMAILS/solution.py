import re
from re import compile as c # for valid_emails_2
from typing import List


def valid_emails_1(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""

    valid_email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")

    def is_valid_email(email: str) -> bool:
        return bool(valid_email_regex.fullmatch(email))

    emails = [email for email in strings if is_valid_email(email)]
    return emails

def valid_emails_2(emails: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""
    regex_string = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    return list(filter(c(regex_string).match, emails))
