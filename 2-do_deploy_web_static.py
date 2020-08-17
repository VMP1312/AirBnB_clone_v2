#!/usr/bin/python3
"""Distributes an archive to your web servers."""

from fabric.api import put, run, env
from os.path import path


env.hosts = ['35.185.63.9', '54.242.105.247']


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""

    rout = "/data/web_static/releases/"
    dirc = archive_path.replace(".tgz", "").replace("versions/", "")

    if not path.exists(archive_path):
        return False

    ret = True

    tmpfolder = put(archive_path, '/tmp/')
    if tmpfolder.failed:
        ret = False

    dest = run('mkdir -p {}{}/'.format(rout, dirc))

    if dest.failed:
        ret = False

    unpack = run('tar -xzf /tmp/{1}.tgz -C {0}{1}/'.format(rout, dirc))

    if unpack.failed:
        ret = False

    clean = run('rm /tmp/{}'.format(dirc))

    if clean.failed:
        ret = False

    move = run('mv {0}{1}/web_static/* {0}{1}/'.format(rout, dirc))

    if move.failed:
        ret = False

    cleanfolder = run('rm -rf {}{}/web_static'.format(rout, dirc))

    if cleanfolder.failed:
        ret = False

    rmold = run('rm -rf /data/web_static/current')
    if rmold.failed:
        ret = False

    new = run('ln -s {}{}/ /data/web_static/current'.format(rout, dirc))
    if new.failed:
        ret = False

    if ret:
        print("All tasks succeeded!")

    return ret
