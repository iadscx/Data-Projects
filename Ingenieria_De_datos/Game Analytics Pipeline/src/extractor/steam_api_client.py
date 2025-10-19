# src/api/steam_api_client.py
import requests
import json
import os
from datetime import datetime

def fetch_steam_top_games(limit=20):
    """
    Extrae datos de los juegos más populares desde la API pública de Steam.
    Guarda los datos en JSON local (simulando un bucket S3).
    """
    app_list_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    app_data = requests.get(app_list_url).json()["applist"]["apps"]

    selected_games = app_data[:limit]
    results = []

    for game in selected_games:
        appid = game["appid"]
        name = game["name"]

        player_url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={appid}"
        player_data = requests.get(player_url).json()

        results.append({
            "appid": appid,
            "name": name,
            "players": player_data.get("response", {}).get("player_count", 0),
            "timestamp": datetime.now().isoformat()
        })

    os.makedirs("data/steam-raw", exist_ok=True)
    file_path = f"data/steam-raw/steam_data_{datetime.now().date()}.json"

    with open(file_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Datos guardados en {file_path} ({len(results)} juegos).")
    return file_path

if __name__ == "__main__":
    fetch_steam_top_games()

