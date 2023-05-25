FROM python:3.11

# Install required packages
RUN apt-get update && \
    apt-get install -y osm2pgsql postgresql-client && \
    rm -rf /var/lib/apt/lists/*
#
## Create a working directory
#WORKDIR /app
#
#COPY ../requirements.txt requirements.txt
## install python dependencies
#RUN pip install --upgrade pip
#
#RUN pip install -r requirements.txt
#
## Copy the Python script into the container
#COPY .. .
#
#
#
## Set environment variables for the database connection
#ENV PGHOST=localhost \
#    PGPORT=5432 \
#    PGUSER=postgres \
#    PGPASSWORD=postgres \
#    PGDATABASE=postgres

EXPOSE 5432
# Run the Python script to download OSM data and import it into PostGIS using osm2pgsql
#CMD python3 import_osm.py