from typing import Dict


def send_welcome_email(user):
    # The function is missing type annotations
    print(f"Sending welcome email to {user.email}")

def process_data(data: Dict[str, int]) -> int:
    # Incorrect data passed, expecting dict with string keys and int values
    total = sum(data["key1"], data["key2"])  # Error: data is not correctly typed
    return total
