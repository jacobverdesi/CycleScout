import requests
import json
# Make Strava auth API call with your
# client_code, client_secret and code
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': [INSERT_CLIENT_ID_HERE],
                            'client_secret': '[INSERT_CLIENT_SECRET_KEY]',
                            'code': '[INSERT_CODE_FROM_URL_HERE]',
                            'grant_type': 'authorization_code'
                            }
                )
#Save json response as a variable
strava_tokens = response.json()
# Save tokens to file
with open('strava_tokens.json', 'w') as outfile:
    json.dump(strava_tokens, outfile)
# Open JSON file and print the file contents
# to check it's worked properly
with open('strava_tokens.json') as check:
  data = json.load(check)
print(data)