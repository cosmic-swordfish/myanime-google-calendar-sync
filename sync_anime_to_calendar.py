from google_calendar import authenticate_google  # Make sure this is defined properly
from myanimelist import get_watchlist  # Make sure this fetches watchlist data
from googleapiclient.errors import HttpError
import datetime

def add_event_to_google_calendar(service, anime_title, start_datetime, end_datetime):
    event = {
        'summary': anime_title,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'UTC',
        },
    }
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
    except HttpError as error:
        print(f"An error occurred: {error}")

def sync_anime_to_calendar():
    service = authenticate_google()  # Ensure Google API authentication
    watchlist = get_watchlist()  # Fetch MyAnimeList watchlist data

    for anime in watchlist['data']:
        anime_title = anime['node']['title']
        start_datetime = datetime.datetime.now().isoformat()  # Replace with actual anime release date
        end_datetime = (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat()  # Example duration

        add_event_to_google_calendar(service, anime_title, start_datetime, end_datetime)

# Run the sync
sync_anime_to_calendar()
