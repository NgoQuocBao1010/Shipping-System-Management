import secrets


def customOrderId():
    return secrets.token_urlsafe(4)
