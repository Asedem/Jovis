# jupyterhub_config.py

import os

c = get_config()

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 80

c.JupyterHub.hub_port = 8080

c.JupyterHub.authenticator_class = 'native'

import nativeauthenticator
c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]

c.Authenticator.allow_all = True
c.Authenticator.admin_users = {'admin'}

c.JupyterHub.db_url = 'sqlite:////srv/jupyterhub/data/jupyterhub.sqlite'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

c.DockerSpawner.image = 'jupyter-notebook-instance:latest'

c.DockerSpawner.remove_containers = True

notebook_base_path = os.environ.get('NOTEBOOK_DIR_PATH')
if not notebook_base_path:
    raise ValueError("NOTEBOOK_DIR_PATH environment variable not set. Please create a .env file.")

c.DockerSpawner.volumes = {
    f'{notebook_base_path}/{{username}}': '/home/jovyan/work'
}
c.DockerSpawner.notebook_dir = '/home/jovyan/work'

c.DockerSpawner.network_name = os.environ.get('COMPOSE_PROJECT_NAME', 'jupyterhub') + '_jupyterhub_network'
c.JupyterHub.hub_connect_ip = 'jupyterhub'
c.JupyterHub.hub_connect_port = 8080