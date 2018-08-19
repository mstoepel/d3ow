import requests
import pandas as pd

data = requests.get('https://api.overwatchleague.com/stats/players?season_id=YYYY').json()
data = data['data']

df = pd.DataFrame(data)
df.to_csv('ow.csv', index=False)


