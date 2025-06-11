FROM jupyterhub/jupyterhub:latest

WORKDIR /srv/jupyterhub

COPY requirements.txt .

RUN pip install jupyterhub-firstuseauthenticator dockerspawner

RUN pip cache purge