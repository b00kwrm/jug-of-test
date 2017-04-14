# got this from: https://github.com/danriti/nginx-gunicorn-flask
# use Debian image
FROM debian:testing-slim

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python3 python3-pip nginx gunicorn3 supervisor

# Setup flask application
RUN mkdir /webapp
ADD . /webapp
RUN pip3 install -r /webapp/requirements.txt

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# Expose 8000
EXPOSE 8000:8000

# Start processes
CMD ["/usr/bin/supervisord"]