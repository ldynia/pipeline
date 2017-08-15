FROM alpine:3.6

MAINTAINER Lukasz Dynowski ludd@bioinformatics.dtu.dk

# Create pipline common directories
VOLUME ["/pipeline/data", "/pipeline/results"]

# Add startup script
ADD startup.sh /docker/startup.sh

# OS Update & Upgrade
RUN apk update && apk upgrade

# Install packages
RUN apk add \
  openssh \
  python3

# Generate ssh keys
RUN ssh-keygen -A
RUN ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
RUN mkdir -p /var/run/sshd
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys
RUN sed -i -e 's/#   StrictHostKeyChecking ask/    StrictHostKeyChecking no/g' /etc/ssh/ssh_config

# Install luigi
RUN pip3 install luigi==2.6.2

# Remove temp and cached files
RUN rm  -rf /tmp/* /var/cache/apk/*

EXPOSE 22

# Execute starup script
ENTRYPOINT ["/docker/startup.sh"]
