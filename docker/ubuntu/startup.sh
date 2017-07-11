#!/bin/bash

# Execute logic when image is run by docker-compose
if [ ! -z "$DOCKER_COMPOSE" ]; then
  # Add piep/container to known_hosts by looping over evry pipe/containers
  for pipe in $(echo $PIPES | tr "," "\n")
  do
    # File exist
    if [ -f /root/.ssh/known_hosts ]; then
      # Is pipe to be found in known_hosts
      if grep -q $pipe /root/.ssh/known_hosts ; then
        echo "Do noting for pipe found in known_hosts"
      else
        echo "Pipe not found -add pipe to known_hosts"
        ssh-keyscan  "$pipe" >> /root/.ssh/known_hosts
      fi
    else
      echo "File does not exist -create file with pipe"
      ssh-keyscan  "$pipe" >> /root/.ssh/known_hosts
    fi
  done
fi

echo "Start ssh deamon in foreground"
/usr/sbin/sshd -D
