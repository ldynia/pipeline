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
  openssh

# Remove temp and cached files
RUN rm  -rf /tmp/* /var/cache/apk/*

# Generate ssh keys
RUN ssh-keygen -A
RUN mkdir -p /var/run/sshd

EXPOSE 22

# Execute starup script
ENTRYPOINT ["/docker/startup.sh"]
