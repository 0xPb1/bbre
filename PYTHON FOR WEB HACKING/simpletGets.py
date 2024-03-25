import requests
requests.packages.urllib3.disable_warnings() # ignore SSL warnings

params = {
    'limit': 10,
    'offset': 2
}

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
    }

resp = requests.get('http://ergast.com/api/f1/2022/last/drivers.json', params=params, proxies=proxies, verify=False)

print (resp.json())

# print(resp.headers)

# print(resp.status_code)

# print (resp.text)

# print (resp.data)