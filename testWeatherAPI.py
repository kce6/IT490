import requests

#make the API call and store response
url = 'http://api.openweathermap.org/data/2.5/weather?zip=94040,us'
r = requests.get(url)
print("Status code:", r.status_code)

#store API response in a variable
response_dict = r.json()

# Process Results
print(response_dict.keys())
