FROM jupyterhub/jupyterhub:latest

RUN useradd -m -s /bin/bash admin && echo "admin:adminpass" | chpasswd

RUN pip install \
    numpy \
    pandas \
    matplotlib \
    scikit-learn \
    scipy \
    black \
    isort \
    jupyter-collaboration \
    jupyterlab_darkside_theme \
    jupyterlab-code-formatter

RUN pip cache purge