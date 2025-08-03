import string
import random

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    return url and (url.startswith('http://') or url.startswith('https://'))
