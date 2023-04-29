import requests
import os
#
# url = "https://download.geofabrik.de/north-america/us-northeast-latest.osm.pbf"
# nh='http://download.geofabrik.de/north-america/us/new-hampshire-latest.osm.bz2'
# response = requests.get(nh)
#
# with open("new-hampshire-latest.osm.bz2", "wb") as f:
#     f.write(response.content)
print('done')
postgis_url='postgresql://postgres:postgres@0.0.0.0:5432/postgres'
os.system(f'osm2pgsql -c  -d {postgis_url}  /app/new-hampshire-latest.osm.bz2')
# osm2pgsql -c -d postgresql://postgres:postgres@localhost:5432/postgres /app/new-hampshire-latest.osm