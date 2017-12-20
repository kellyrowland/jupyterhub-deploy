FROM registry.spin.nersc.gov/das/jupyterhub-spin:latest
MAINTAINER Rollin Thomas <rcthomas@lbl.com>

# Additional Ubuntu packages
# TODO: resolve zsh thing that Rollin ran into b/c datatran

RUN \
    apt-get --yes install   \
        openssh-server      \
        zsh

RUN \
    mkdir -p /var/run/sshd

ADD docker-entrypoint.sh /srv/
ADD NERSC-keys-api /usr/lib/nersc-ssh-keys/
ADD get_port.py /opt/anaconda3/bin/
RUN chmod a+x /usr/lib/nersc-ssh-keys/NERSC-keys-api

RUN \
    echo "AuthorizedKeysCommand /usr/lib/nersc-ssh-keys/NERSC-keys-api" >> /etc/ssh/sshd_config && \
    echo "AuthorizedKeysCommandUser nobody" >> /etc/ssh/sshd_config

WORKDIR /srv
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT [ "./docker-entrypoint.sh" ]
CMD [ "/usr/sbin/sshd", "-p", "22", "-D" ]
