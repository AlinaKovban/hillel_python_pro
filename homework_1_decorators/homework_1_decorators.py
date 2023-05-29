import functools
import requests
import psutil
from collections import Counter


def memory(f):
    def internal(*args, **kwargs):
        process = psutil.Process()
        memory_usage_before = process.memory_info().rss
        print(f'Usage memory before {memory_usage_before}')
        f(*args, **kwargs)
        memory_usage_after = process.memory_info().rss
        print(f'Usage memory after {memory_usage_after}')
    return internal
        


def cache(max_limit):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                return deco._cache[cache_key]
            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                least_used_key = min(deco._cache, key=deco._cache.get)
                del deco._cache[least_used_key]
            deco._cache[cache_key] = result
            return result
        deco._cache = Counter()
        return deco
    return internal


@memory
@cache(64)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content



fetch_url('https://www.google.com/')
print('----')
fetch_url('https://www.google.com/')
print('----')
fetch_url('https://www.facebook.com/')
print('----')
fetch_url('https://github.com/')
