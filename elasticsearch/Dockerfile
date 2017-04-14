# Get official Docker image
FROM docker.elastic.co/elasticsearch/elasticsearch:5.2.2

# Get root
USER root

# update image
RUN apk update && apk upgrade

# install nginx
RUN apk add nginx supervisor

# Copy supervisord file
# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/

# Add new nginx config
ADD nginx.conf /etc/nginx/nginx.conf

# Create nginx run dir
RUN mkdir /run/nginx

# chown files for elasticsearch
RUN chown -R elasticsearch:elasticsearch /run/nginx && chown -R elasticsearch:elasticsearch /var/lib/nginx \
&& chown -R elasticsearch:elasticsearch /var/log/nginx

USER elasticsearch

# Override Command
CMD ["/usr/bin/supervisord"]