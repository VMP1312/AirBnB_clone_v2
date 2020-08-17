#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""

from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    local('tar -cvzf "versions/web_static_{}.tgz" web_static'.format(time))
    path = "versions/web_static_{}.tgz" web_static'.format(time)
    if command.succeeded:
        return fn
    return None
