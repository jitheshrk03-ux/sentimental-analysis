import requests
response= requests.post("http://127.0.0.1:5000/predict",json={'review': 'the movie was boring!'})
print(response.json())