#!/usr/bin/python3
"""ALL"""
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['35.185.63.9', '54.242.105.247']
T = datetime.now()


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    files = 'versions/web_static_{}{}{}{}{}{}.tgz'\
        .format(T.year, T.month, T.day, T.hour, T.minute, T.second)
    local('mkdir -p versions')
    execute = local("tar -cvzf " + files + " ./web_static/")
    if execute.succeeded:
        return files
    return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""

    if not os.path.exists(archive_path):
        return False

    ret = True

    tmpfolder = put(archive_path, '/tmp/')

    if tmpfolder.failed:
        ret = False

    dirc = archive_path.replace(".tgz", "").replace("versions/", "")
    dest = run('mkdir -p /data/web_static/releases/' + dirc + '/')

    if dest.failed:
        ret = False

    unpack = run('tar -xzf /tmp/' + dirc + '.tgz' +
                 ' -C /data/web_static/releases/' + dirc + '/')

    if unpack.failed:
        ret = False

    clean = run('rm /tmp/' + dirc + '.tgz')

    if clean.failed:
        ret = False

    move = run('mv /data/web_static/releases/' + dirc +
               '/web_static/* /data/web_static/releases/' + dirc + '/')

    if move.failed:
        ret = False

    cleanfolder = run('rm -rf /data/web_static/releases/' + dirc +
                      '/web_static')

    if cleanfolder.failed:
        ret = False

    rmold = run('rm -rf /data/web_static/current')

    if rmold.failed:
        ret = False

    new = run('ln -sf /data/web_static/releases/' + dirc +
              '/' + ' /data/web_static/current')

    if new.failed:
        ret = False

    if ret:
        print("New version deployed!")

    return ret


def deploy():
    """Creates and distributes an archive to your web servers"""

    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
