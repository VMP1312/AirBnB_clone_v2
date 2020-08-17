#!/usr/bin/python3
"""Distributes an archive to your web servers."""

from fabric.api import put, run, env
from os import path


env.hosts = ['35.185.63.9', '54.242.105.247']


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""

    rout = "/data/web_static/releases/"

    if not path.exists(archive_path):
        return False

    ret = True

    tmpfolder = put(archive_path, '/tmp/')

    if tmpfolder.failed:
        ret = False

    dirc = archive_path.replace(".tgz", "").replace("versions/", "")
    dest = run('mkdir -p {}' + dirc + '/'.fotmat(rout))

    if dest.failed:
        ret = False

    unpack = run('tar -xzf /tmp/' + dirc + '.tgz' +
                 ' -C {}' + dirc + '/'.fotmat(rout))

    if unpack.failed:
        ret = False

    clean = run('rm /tmp/' + dirc + '.tgz')

    if clean.failed:
        ret = False

    move = run('mv {}' + dirc + '/web_static/* {}' + dirc + '/'.fotmat(rout))

    if move.failed:
        ret = False

    cleanfolder = run('rm -rf {}' + dirc + '/web_static'.fotmat(rout))

    if cleanfolder.failed:
        ret = False

    rmold = run('rm -rf /data/web_static/current')

    if rmold.failed:
        ret = False

    new = run('ln -sf {}' + dirc +
              '/' + ' /data/web_static/current'.fotmat(rout))

    if new.failed:
        ret = False

    if ret:
        print("New version deployed!")

    return ret
