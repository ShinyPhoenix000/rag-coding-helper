# Requests Library Documentation

## Installation

```bash
pip install requests
```

## Making Requests

### GET Request
```python
import requests
response = requests.get('https://api.example.com/data')
print(response.status_code)
print(response.text)
```

### POST Request
```python
import requests
payload = {'key': 'value'}
response = requests.post('https://api.example.com/data', data=payload)
print(response.json())
```

### PUT Request
```python
import requests
payload = {'key': 'new_value'}
response = requests.put('https://api.example.com/data/1', data=payload)
print(response.json())
```

### DELETE Request
```python
import requests
response = requests.delete('https://api.example.com/data/1')
print(response.status_code)
```

## Headers, Params, and Cookies

### Custom Headers
```python
headers = {'Authorization': 'Bearer TOKEN'}
response = requests.get('https://api.example.com/data', headers=headers)
```

### Query Parameters
```python
params = {'search': 'query'}
response = requests.get('https://api.example.com/data', params=params)
```

### Cookies
```python
cookies = {'session_id': '123456'}
response = requests.get('https://api.example.com/data', cookies=cookies)
```

## JSON Handling
```python
response = requests.get('https://api.example.com/data')
data = response.json()
```

## Sessions
```python
session = requests.Session()
session.get('https://api.example.com/data')
```

## File Upload
```python
files = {'file': open('report.csv', 'rb')}
response = requests.post('https://api.example.com/upload', files=files)
```

## Authentication
```python
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.example.com/secure', auth=HTTPBasicAuth('user', 'pass'))
```

## Error Handling
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
```

## References
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [Requests GitHub](https://github.com/psf/requests)