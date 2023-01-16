import requests
import pandas as pd
import json

url = "https://data.cityofchicago.org/resource/4ijn-s7e5.json"

response = requests.get(url)
df = pd.DataFrame(response.json())
df.to_csv('Food_Inspections.csv', index=False)