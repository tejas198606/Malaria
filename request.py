import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Number of reported cases of cholera':2.0000,'Number of reported deaths from cholera':9.0000,'Cholera case fatality rate':6.0000,'Country_new':2.00000})

print(r.json())
