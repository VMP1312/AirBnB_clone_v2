#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""

from datetime import datetime
from fabric.api import local

T = datetime.now()


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    files = 'versions/web_static_{}{}{}{}{}{}.tgz'\
        .format(T.year, T.month, T.day, T.hour, T.minute, T.second)
    local('mkdir -p versions')
    execute = local("tar -cvzf " + files + " ./web_static/")
    if execute.succeeded:
        return files
