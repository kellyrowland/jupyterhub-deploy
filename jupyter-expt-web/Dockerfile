#FROM registry.spin.nersc.gov/das/jupyterhub-expt-base:latest
FROM jupyterhub-base.begin-jupyter-expt:latest
MAINTAINER Rollin Thomas <rcthomas@lbl.com>

# Authenticator and spawner

RUN \
    pip install git+https://github.com/nersc/sshapiauthenticator.git    && \
    pip install git+https://github.com/nersc/sshspawner.git             && \
    pip install git+https://github.com/jupyterhub/batchspawner.git      && \
    pip install git+https://github.com/jupyterhub/wrapspawner.git       && \
    pip install git+https://github.com/nersc/nerscspawner.git

ADD docker-entrypoint.sh jupyterhub_config.py /srv/
ADD templates /srv/templates/

WORKDIR /srv
RUN chmod +x docker-entrypoint.sh
CMD ["jupyterhub", "--debug"]
ENTRYPOINT ["./docker-entrypoint.sh"]
