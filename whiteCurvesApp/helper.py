import secrets


def generate_applicant_id():
    random_id = secrets.token_hex(3)
    return f"WC{random_id}".upper()


