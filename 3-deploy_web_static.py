#!/usr/bin/python3
"""ALL"""
from os import path
from fabric.api import sudo, env, put, local
from datetime import datetime

env.hosts = ['35.190.142.12', '34.229.218.28']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        local('mkdir -p versions')
        local('tar -cvzf "versions/web_static_{}.tgz" web_static'.format(time))
        path = "versions/web_static_{}.tgz" web_static'.format(time)
        return path
    except failed:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""

    if not path.isfile(archive_path):
        return False

    files = archive_path.split("/")[-1]
    name = files.split(".")[0]
    tmp = "/tmp/{}".format(files)
    data = "/data/web_static/releases/{}/".format(name)
    curr = "/data/web_static/current"

    if put("0-setup_web_static.sh", "/tmp/").failed:
        return False

    if sudo("chmod u+x /tmp/0-setup_web_static.sh").failed:
        return False

    if sudo("/tmp/0-setup_web_static.sh").failed:
        return False

    if sudo("rm /tmp/0-setup_web_static.sh").failed:
        return False

    if put(archive_path, tmp).failed:
        return False

    if sudo("rm -rf {}".format(data)).failed:
        return False
    if sudo("mkdir -p {}".format(data)).failed:
        return False

    if sudo("tar -xzf {} -C {}".format(tmp, data)).failed:
        return False

    if sudo("rm {}".format(tmp)).failed:
        return False

    if sudo("mv {}web_static/* {}".format(data, data)).failed:
        return False

    if sudo("rm -rf {}web_static".format(data)).failed:
        return False

    if sudo("rm -rf {}".format(curr)).failed:
        return False

    if sudo("ln -s {} {}".format(data, curr)).failed:
        return False

    print("New version deployed!")

    return True


def deploy():
    """Creates and distributes an archive to your web servers"""

    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
