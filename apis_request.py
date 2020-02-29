import requests
import pandas as pd

url = "https://the-cocktail-db.p.rapidapi.com/list.php"

querystring = {"g":"list"}

headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "9b67c8bd9dmsh26f9d76eccc8788p14ab60jsnebafab540e1b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
df = pd.DataFrame(data['drinks'])
print(df[:10],df[-10:])