#!/usr/bin/env python3
import argparse
from helpers import execute
from list_servers import list_servers

parser = argparse.ArgumentParser('destroy servers')
parser.add_argument('--hostname', type=str)

args = parser.parse_args()


def exitOnEmpty(items):
    if len(items) != 0:
        return

    print('no servers to destroy')
    exit()


def destroyServer(subid):
    data = {
        'SUBID': subid
    }

    response = execute('server_destroy', method='post', data=data)

    if response.status_code is 200:
        return print(f'server {subid} destroyed')

    print('there was a problem!')


servers = list_servers()

exitOnEmpty(servers)

hostname = args.hostname
subidsToRemove = []

for subid in servers:
    server = servers[subid]

    if hostname:
        if server['tag'] == hostname:
            subidsToRemove.append(subid)
    else:
        subidsToRemove.append(subid)

exitOnEmpty(subidsToRemove)

for subid in subidsToRemove:
    destroyServer(subid)

if hostname:
    print(f'all {hostname} servers destroyed')
else:
    print('all servers destroyed')
