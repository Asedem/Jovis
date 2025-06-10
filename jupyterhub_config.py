c = get_config()

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 80

c.Authenticator.allow_all = True

c.Authenticator.admin_users = {'admin'}

c.JupyterHub.db_url = 'sqlite:////srv/jupyterhub/data/jupyterhub.sqlite'