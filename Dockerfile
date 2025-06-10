FROM jupyterhub/jupyterhub:latest

WORKDIR /srv/jupyterhub

COPY requirements.txt .

RUN pip install jupyterhub-nativeauthenticator dockerspawner

RUN pip cache purge