# Use Debian Bullseye Slim as the base image
FROM debian:bullseye-slim

# Install necessary packages and PyPDF2 in one step
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    vim \
    make \
    && pip3 install PyPDF2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Add ll alias
RUN echo "alias ll='ls -lah'" >> /root/.bashrc
