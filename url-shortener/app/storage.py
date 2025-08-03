import time

# In-memory stores
url_store = {}
click_stats = {}

def save_url(short_code, original_url):
    timestamp = time.strftime('%Y-%m-%dT%H:%M:%S')
    url_store[short_code] = {
        'url': original_url,
        'created_at': timestamp
    }
    click_stats[short_code] = 0

def get_url(short_code):
    return url_store.get(short_code)

def increment_click(short_code):
    if short_code in click_stats:
        click_stats[short_code] += 1

def get_stats(short_code):
    if short_code not in url_store:
        return None
    return {
        'url': url_store[short_code]['url'],
        'clicks': click_stats[short_code],
        'created_at': url_store[short_code]['created_at']
    }
