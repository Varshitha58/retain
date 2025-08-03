from app.utils import generate_short_code, is_valid_url
from app.storage import save_url, get_url, increment_click, get_stats

def shorten_url(original_url):
    if not is_valid_url(original_url):
        return {'error': 'Invalid URL'}

    short_code = generate_short_code()
    while get_url(short_code):
        short_code = generate_short_code()

    save_url(short_code, original_url)

    return {
        'short_code': short_code,
        'short_url': f'http://localhost:5000/{short_code}'
    }

def get_original_url(short_code):
    data = get_url(short_code)
    if not data:
        return {'error': 'Short code not found'}

    increment_click(short_code)
    return {'url': data['url']}

def get_url_stats(short_code):
    stats = get_stats(short_code)
    if not stats:
        return {'error': 'Short code not found'}
    return stats
