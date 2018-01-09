FROM registry.spin.nersc.gov/das/jupyterhub-base:latest
MAINTAINER Rollin Thomas <rcthomas@lbl.com>

# Authenticator and spawner

RUN \
    pip install git+https://github.com/nersc/sshapiauthenticator.git    && \
    pip install git+https://github.com/nersc/sshspawner.git             && \
    pip install git+https://github.com/nersc/batchspawner.git           && \
    pip install git+https://github.com/nersc/wrapspawner.git@sknigh-fix && \
    pip install git+https://github.com/nersc/nerscspawner.git

ADD docker-entrypoint.sh jupyterhub_config.py /srv/

WORKDIR /srv
RUN chmod +x docker-entrypoint.sh
CMD ["jupyterhub", "--debug"]
ENTRYPOINT ["./docker-entrypoint.sh"]
