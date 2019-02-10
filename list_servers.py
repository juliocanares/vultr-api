from helpers import execute


def list_servers():
    response = execute('server_list')

    return response.json()
