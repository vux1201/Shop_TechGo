import re

PATTERN = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"


def password_strong(password):
    return bool(re.match(PATTERN, password))
