#!/usr/bin/env python3

import threading
import argparse
from helpers import execute
from list_servers import list_servers

parser = argparse.ArgumentParser('vultr')
parser.add_argument('--servers', required=True, type=int)
parser.add_argument('--hostname',  required=True, type=str)

args = parser.parse_args()

delimiter = '-'


def create_server(hostname):
    hostname_parts = hostname.split(delimiter)
    label = delimiter.join(hostname_parts[:-1])

    data = {
        'DCID': 39,
        'VPSPLANID': 201,
        'OSID': 270,
        'SSHKEYID': '5c5e3f4ee8b5d',
        'hostname': hostname,
        'tag': label,
        'label': hostname
    }

    return execute('server_create', method='post', data=data)


def checkServers():
    servers = list_servers()

    for id in new_server_ids:
        current_server = servers[id]
        status = current_server['status']
        label = current_server['label']
        ip = current_server['main_ip']

        print(f'{label} is {status} in {ip}')


new_server_ids = []

for i in range(args.servers):
    hostname = f'{args.hostname}{delimiter}{i + 1}'
    response = create_server(hostname)

    print(f'creating {hostname}')

    data = response.json()

    new_server_ids.append(data['SUBID'])

print('servers created')
print('waiting for active status...')


timer = threading.Timer(10, checkServers)
timer.start()
