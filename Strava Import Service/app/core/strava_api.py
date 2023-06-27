import json
import logging

import pandas as pd
import requests
from stravalib import Client

from app.config import settings

# logging.log(logging.INFO, f"Strava API URL: {STRAVA_API_URL}")
strava_api_client = Client()
# STRAVA_API_URL = "https://www.strava.com/api/v3/"

# def get_access_token(code):
#     strava_token = requests.post(
#         url='https://www.strava.com/oauth/token',
#         data={
#             'client_id': settings.client_id,
#             'client_secret': settings.client_secret,
#             'code': code,
#             'grant_type': 'authorization_code'
#         }
#     ).json()
#     return strava_token
#
# def get_refresh_token(refresh_token):
#     strava_token = requests.post(
#         url='https://www.strava.com/oauth/token',
#         data={
#             'client_id': settings.client_id,
#             'client_secret': settings.client_secret,
#             'refresh_token': refresh_token,
#             'grant_type': 'refresh_token'
#         }
#     ).json()
#     return strava_token
# def get_athlete(access_token):
#     url = STRAVA_API_URL + "athlete"
#     athlete = requests.get(url + '?access_token=' + access_token).json()
#     return athlete
#
# def get_activities(access_token, page):
#     url = STRAVA_API_URL + "activities/"
#     activities_list = requests.get(url + '?access_token=' + access_token + '&per_page=' + str(page)).json()
#     with open(f'activities_{page}.json', 'w') as outfile:
#         json.dump(activities_list, outfile)
#     return activities_list
