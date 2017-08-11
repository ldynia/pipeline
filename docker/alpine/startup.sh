#!/bin/ash

# Execute logic when image is run by docker-compose
if [ ! -z "$DOCKER_COMPOSE" ]; then
  # Remove known_hosts
  if [ -f /root/.ssh/known_hosts ]; then
    echo "Removing '/root/.ssh/known_hosts'"
    rm /root/.ssh/known_hosts
  fi

  # Remove authorized_keys
  if [ -f /root/.ssh/authorized_keys ]; then
    echo "Removing '/root/.ssh/authorized_keys'"
    rm /root/.ssh/authorized_keys
  fi

  # Add pipline's id key to authorized_keys
  cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

  # Add piep/container to known_hosts by looping over evry pipe/containers
  for pipe in $(echo $PIPES | tr "," "\n")
  do
    echo "Adding '$pipe'' to '/root/.ssh/known_hosts'"
    ssh-keyscan  "$pipe" >> /root/.ssh/known_hosts
  done
fi

echo "Ssh deamon started in foreground"
/usr/sbin/sshd -D

exec "$@"
