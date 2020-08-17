#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

chown -R ubuntu:ubuntu /data

sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
