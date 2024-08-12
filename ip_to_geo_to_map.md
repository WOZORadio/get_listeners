<!--
https://github.com/lifeparticle/Markdown-Cheatsheet?tab=readme-ov-file#links
-->
# How to plot IPs on a Map
this is ultimate goal of this module is to take IPs that listeners are on and display their info on a map.

## research - first see if you can find via google
``` python
$ google 
```

## Geolocate an IP address using an IP address database try: [Geolocation DB][1]
An easy way to geolocate an IP address is to use an online geolocation database like Geolocation DB. Geolocation DB is free-to-use and doesn't require an API key. It stores an impressive database of IP addresses obtained from Internet service providers.

[1]: https://www.abstractapi.com/guides/ip-geolocation/how-to-geolocate-an-ip-address-in-python

``` python
import requests
import json

# IP address to test
ip_address = '147.229.2.90'
request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result  = json.loads(result)print(result)
```