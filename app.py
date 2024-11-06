from flask import Flask, render_template
from sync_anime_to_calendar import sync_anime_to_calendar  # Ensure this import is correct
import threading

app = Flask(__name__)

# Route to serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to sync anime to Google Calendar
@app.route('/sync', methods=['GET'])
def sync_anime():
    sync_thread = threading.Thread(target=sync_anime_to_calendar)
    sync_thread.start()
    return "Syncing anime to Google Calendar...", 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Runs the web app on localhost:5000
