#!/usr/bin/env python3

from helpers import execute


def list_servers():
    response = execute('server_list')

    return response.json()
