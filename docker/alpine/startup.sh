#!/bin/ash

# Execute logic when image is run by docker-compose
if [ ! -z "$DOCKER_COMPOSE" ]; then

  # Add pipline's id key to authorized_keys
  if [ -f /root/.ssh/id_rsa.pub ]; then
    echo "Add pipline's 'id_rsa.pub' key to authorized_keys"
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys
  else
    echo "Generating 'id_rsa.pub' and adding it to authorized_keys"
    ssh-keygen -A
    yes | ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
    cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys
  fi

fi

echo "Ssh deamon started in foreground"
/usr/sbin/sshd -D

exec "$@"
