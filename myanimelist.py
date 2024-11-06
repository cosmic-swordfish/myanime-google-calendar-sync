import requests

def get_watchlist():
    url = "https://api.myanimelist.net/v2/anime/watchlist"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Example: Fetch watchlist
watchlist = get_watchlist()
print(watchlist)

