#!/usr/bin/python3
"""Distributes an archive to your web servers."""

from fabric.api import put, run, env
from os.path import path


env.hosts = ['35.185.63.9', '54.242.105.247']


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""
    if not path.exists(archive_path):
        return False
    try:
        files = archive_path.split("/")[-1]
        file = files.split(".")[0]
        my_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(my_path, file))
        run('tar -xzf /tmp/{} -C {}{}/'.format(files, my_path, file))
        run('rm /tmp/{}'.format(files))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(my_path, file))
        run('rm -rf {}{}/web_static'.format(my_path, file))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(my_path, file))
        return True
    except Failed:
        return False
