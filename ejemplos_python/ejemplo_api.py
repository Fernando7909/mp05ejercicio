import requests

# URL de l'API
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Barcelona",
    "appid": "b02c3fbd01111ff26f563ccc7f9ce955",  # substitueix per la teva clau d'API
    "units": "metric",
    "lang": "ca"
}

# Fer la sol·licitud GET
resposta = requests.get(url, params=params)

# Verificar si la sol·licitud ha tingut èxit

if resposta.status_code == 200:
    dades = resposta.json()  # Convertir la resposta a JSON
    print (resposta)
    print("Temperatura a Barcelona:", dades['main']['temp'], "°C")
    print("Descripció del clima:", dades['weather'][0]['description'])
else:
    print("Error en la sol·licitud:", resposta.json())
