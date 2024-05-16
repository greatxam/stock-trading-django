# Created by Maximillian M. Estrada on 2024-05-15

# Dockerfile to build Stock Trading

# Use an official Debian image
FROM debian:bookworm

RUN apt-get update && \
	apt-get upgrade -y

# Install required packages
RUN apt-get install -y \
    build-essential \
    cron \
    python3.11 \
    python3-pip \
    apache2 \
    libapache2-mod-wsgi-py3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Python packages
COPY ./requirements.txt /
RUN pip install -r /requirements.txt --break-system-packages && \
    rm /requirements.txt

# Set the working directory to `/var/www/stock_trading`
WORKDIR /var/www/stock_trading

# Copy the application directory contents into the container at `/var/www/stock_trading`
COPY ./src/stock_trading /var/www/stock_trading

# Override Apache HTTPD default website configuration
COPY ./src/apache2/stock_trading_vhost.conf /etc/apache2/sites-available/000-default.conf

# Set the Hostname
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Apache HTTPD file permissions
RUN chown -R www-data:www-data /var/www
RUN chmod -R 755 /var/www

# Docker entrypoint script
COPY --chmod=0755 ./docker-entrypoint.sh /
ENTRYPOINT ["/bin/sh", "/docker-entrypoint.sh"]
