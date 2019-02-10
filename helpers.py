import os
import threading
import requests

from dotenv import load_dotenv

load_dotenv(verbose=True)


api_key = os.getenv('API_KEY')

base_url = 'https://api.vultr.com/v1'


def get_url(path):
    return f'{base_url}/{path}'


def execute(path, headers={}, method='get', **kwargs):
    headers['API-key'] = api_key

    url = endpoints[path]

    if method == 'get':
        return requests.get(url, headers=headers, **kwargs)

    return requests.post(url, headers=headers, **kwargs)


endpoints = {
    'server_list': get_url('server/list'),
    'server_create': get_url('server/create'),
    'server_destroy': get_url('server/destroy')
}


def set_interval(func, sec):
    def method():
        set_interval(func, sec)
        func()

    timer = threading.Timer(sec, method)
    timer.start()

    return timer
