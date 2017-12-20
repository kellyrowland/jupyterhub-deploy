FROM registry.spin.nersc.gov/das/jupyterhub-base:latest
MAINTAINER Rollin Thomas <rcthomas@lbl.com>

## # Python 3 Anaconda and additional packages
## 
## RUN \
##     /opt/anaconda3/bin/conda update --yes conda                 && \
##     /opt/anaconda3/bin/conda install --yes ipykernel notebook   && \
##     /opt/anaconda3/bin/ipython kernel install                   && \
##     /opt/anaconda3/bin/conda clean --yes --all

# Authenticator and spawner

RUN \
    pip install git+https://github.com/nersc/sshapiauthenticator.git    && \
    pip install git+https://github.com/nersc/sshspawner.git             && \
    pip install git+https://github.com/nersc/wrapspawner.git@sknigh-fix

ADD docker-entrypoint.sh jupyterhub_config.py /srv/

WORKDIR /srv
RUN chmod +x docker-entrypoint.sh
CMD ["jupyterhub", "--debug"]
ENTRYPOINT ["./docker-entrypoint.sh"]
