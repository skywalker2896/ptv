from hashlib import sha1
import hmac
import requests
import urllib.parse

def calculate_signature(url, key):
    hashed = hmac.new(str.encode(key), str.encode(url), sha1)
    signature = hashed.hexdigest()
    return signature

def get_url(url, dev_id, key):
    url += ('&' if ('?' in url) else '?')
    url += 'devid={}'.format(str(dev_id))

    signature = calculate_signature(url, key)

    return 'https://timetableapi.ptv.vic.gov.au{}&signature={}'.format(url, signature)

def ptv_api(url):
    url = get_url(url, 3001045, 'cb4465fe-5b62-4082-b31b-f98da31ba57f')
    payload = requests.get(url, verify=True)
    return payload.json()

def search(query):
    href = f"/v3/search/{urllib.parse.quote_plus(query).replace('%2F', '/')}"
    
    return ptv_api(href)

def departures(route_type, stop_id, route_id):
    # route_type = 
    href = f"/v3/departures/route_type/{urllib.parse.quote_plus(route_type).replace('%2F', '/')}/stop/{urllib.parse.quote_plus(stop_id).replace('%2F', '/')}/route/{urllib.parse.quote_plus(route_id).replace('%2F', '/')}"
    return ptv_api(href)

if __name__ == '__main__':
    stop_name = input("Please enter a stop name: ")
    stop_info = search(stop_name)
    if stop_info:
        print(stop_info)

    
    departures(stop_info["stops"][0]["stop_id"])