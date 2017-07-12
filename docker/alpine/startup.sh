#!/bin/sh

# Execute logic when image is run by docker-compose
if [ ! -z "$DOCKER_COMPOSE" ]; then
  # Remove known_hosts
  if [ -f /root/.ssh/known_hosts ] && [ -f /root/.ssh/authorized_keys ]; then
    rm /root/.ssh/known_hosts
    rm /root/.ssh/authorized_keys
  fi

  # Add pipline's id key to authorized_keys
  cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

  # Add piep/container to known_hosts by looping over evry pipe/containers
  for pipe in $(echo $PIPES | tr "," "\n")
  do
    ssh-keyscan  "$pipe" >> /root/.ssh/known_hosts
  done
fi

echo "Ssh deamon started in foreground"
/usr/sbin/sshd -D

exec "$@"
