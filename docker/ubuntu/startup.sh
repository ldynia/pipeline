#!/bin/sh

# Add webapp's key to pipline's authorized_keys
# tail /srv/www/compare/htdocs/docker/shared_data/id_rsa.pub > /root/.ssh/authorized_keys

# Start ssh deamon in foreground
/usr/sbin/sshd -D &

exec "$@"
