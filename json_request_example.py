# JSON requests from NASA API
# Code from in-class

import json
import requests 
import time


request = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
nasa = request.json()
print(nasa)

# Finding when the ISS is over the house!
# Parameters and get request
parameters = {"lat":44.91, "lon":-93.34}
req = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
iss = json.loads(req.text)

# Writing the output to a file
'''
with open ('view.txt', 'w') as outfile: 
    json.dump(iss, outfile, indent=4, separators=(',',':'), sort_keys=True)
outfile.close()
'''

# Parse some stuff
print(json.dumps(iss, indent=4))
print(iss['request'])
print(iss['response'])

# Get the risetime of the ISS from the response and format it nicely
start_overhead = iss['response'][0].get('risetime')
nice_time = time.localtime(start_overhead)
formatted_nice_time = f"{nice_time[1]}-{nice_time[2]}-{nice_time[0]} at {nice_time[3]}:{nice_time[4]}:{nice_time[5]}"
print(f"The ISS will next be overhead the house on {formatted_nice_time}.")

