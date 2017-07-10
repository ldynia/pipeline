FROM ubuntu:17.10

MAINTAINER Lukasz Dynowski ludd@bioinformatics.dtu.dk

# Add startup script
ADD startup.sh /docker/startup.sh

# OS Update & Upgrade
RUN apt update -y && apt upgrade -y

# Install packages
RUN apt install -y \
  default-jre \
  g++ \
  gcc \
  git \
  make \
  python \
  python-pip \
  ssh

# Remove temp and cached files
RUN rm  -rf /tmp/* /var/cache/apt/*

# Generate ssh keys
RUN ssh-keygen -A
RUN mkdir -p /var/run/sshd

# Install slurm-pipeline
RUN git clone https://github.com/acorg/slurm-pipeline
RUN pip install -r /slurm-pipeline/requirements-2.txt
RUN cd slurm-pipeline && python setup.py install

# Install next flow
RUN wget -qO- get.nextflow.io | bash
RUN mv nextflow /usr/local/bin

# Install luigi
RUN pip install luigi==2.6.2

EXPOSE 22

# Execute starup script
ENTRYPOINT ["/docker/startup.sh"]
