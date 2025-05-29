FROM gitpod/workspace-full

USER root

# Install python3-venv so you can use virtual environments
RUN apt-get update && \
    apt-get install -y python3.10-venv && \
    rm -rf /var/lib/apt/lists/*

USER gitpod
