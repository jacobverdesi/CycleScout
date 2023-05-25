import requests
import json

# Make Strava auth API call with your
# client_code, client_secret and code
response = requests.post(
    url='https://www.strava.com/oauth/token',
    data={
        'client_id': 72828,
        'client_secret': '4f0825d1530a7907f490bc6c45e982c7b11cea05',
        'code': '6f5e07db89e04a9f107840417b590b760b99b472',
        'grant_type': 'authorization_code'
    }
)
# Save json response as a variable
strava_tokens = response.json()
# Save tokens to file
with open('strava_tokens.json', 'w') as outfile:
    json.dump(strava_tokens, outfile)
# Open JSON file and print the file contents
# to check it's worked properly
with open('strava_tokens.json') as check:
    data = json.load(check)
print(data)
