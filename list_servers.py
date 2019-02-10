#!/usr/bin/env python3
import json
from helpers import execute


def list_servers():
    response = execute('server_list')

    return response.json()


if __name__ == '__main__':
    result = list_servers()
    beautified = json.dumps(result, sort_keys=True, indent=4)

    print(beautified)
