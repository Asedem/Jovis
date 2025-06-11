FROM jupyterhub/jupyterhub:latest

WORKDIR /srv/jupyterhub

RUN pip install jupyterhub-firstuseauthenticator dockerspawner

RUN pip cache purge