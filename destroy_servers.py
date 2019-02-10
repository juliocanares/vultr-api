#!/usr/bin/env python3

from helpers import execute
from list_servers import list_servers


def destroyServer(subid):
    data = {
        'SUBID': subid
    }

    response = execute('server_destroy', method='post', data=data)

    if response.status_code is 200:
        return print(f'server {subid} destroyed')

    print('there was a problem!')


servers = list_servers()

if len(servers) is 0:
    print('no servers to destroy')
    exit()

for subid in servers.keys():
    destroyServer(subid)

print('all servers destroyed')
