import secrets
import string

# Define a function to generate a random password
def generate_random_password(length=12):
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?'
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password
