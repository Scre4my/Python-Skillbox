import re
import doctest
def validate_password(password):
    """
    Validates whether the input string is a correct password.

    >>> validate_password('rtG&3FG#Tr^e')
    True
    >>> validate_password('a^A1@*@1Aa')
    True
    >>> validate_password('oF^a1D@y5%e6')
    True
    >>> validate_password('parol')
    False
    >>> validate_password('password')
    False
    >>> validate_password('qwerty')
    False
    >>> validate_password('lOngPa$$W0Rd')
    False
    >>> validate_password('питон')
    False
    """
    if len(password) < 8:
        return False
    if not re.match(r'^[a-zA-Z0-9^$%@#&*]{8,}$', password):
        return False
    if len(re.findall(r'[a-z]', password)) < 2:
        return False
    if len(re.findall(r'\d', password)) < 1:
        return False
    if len(set(re.findall(r'[^a-zA-Z0-9^$%@#&*]', password))) < 3:
        return False
    if any(char in ',.!?' for char in password):
        return False
    return True