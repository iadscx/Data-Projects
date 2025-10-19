import requests
import json
import os

def extract_data():
    API_KEY = os.getenv("STEAM_API_KEY")
    API_URL = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/"

    print("Extrayendo datos desde Steam API")
    response = requests.get(API_URL)
    data = response.json()

    os.makedirs("data", exist_ok=True)
    with open("data/raw_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Datos guardados en data/raw_data.json")
