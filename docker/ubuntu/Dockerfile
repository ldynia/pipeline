FROM debian:9.0

MAINTAINER Lukasz Dynowski ludd@bioinformatics.dtu.dk

# Create pipline common directories
VOLUME ["/pipeline/data", "/pipeline/results"]

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
  python3 \
  python3-pip \
  ssh \
  wget

# Remove temp and cached files
RUN rm  -rf /tmp/* /var/cache/apt/*

# Setup SSH
RUN ssh-keygen -A
RUN ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
RUN mkdir -p /var/run/sshd
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys
RUN sed -i -e 's/HashKnownHosts yes/HashKnownHosts no/g' /etc/ssh/ssh_config
RUN sed -i -e 's/#   StrictHostKeyChecking ask/    StrictHostKeyChecking no/g' /etc/ssh/ssh_config

# Install slurm-pipeline
RUN git clone https://github.com/acorg/slurm-pipeline
RUN pip3 install -r /slurm-pipeline/requirements-3.txt
RUN cd slurm-pipeline && python3 setup.py install

# Install next flow
RUN wget -qO- get.nextflow.io | bash
RUN mv nextflow /usr/local/bin

# Install luigi
RUN pip3 install luigi==2.6.2
RUN pip3 install snakemake==3.13.3

EXPOSE 22

# Execute starup script
ENTRYPOINT ["/docker/startup.sh"]
