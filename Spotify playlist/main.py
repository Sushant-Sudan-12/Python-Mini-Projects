from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    authmanager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=,
        client_secret=,
        show_dialog=True,
        cache_path="token.txt",
        username=,
    )
)

client_id = "feb8e6e5c6f84165bef677ce3fec7a9b"
client_secret = "c53c265fead94c01b1f0e4ffa7179b46"

date = input("Which date's playlist do you want YYYY-MM-DD:")

response = requests.get("https://www.billboard.com/charts/hot-100/"+ date)

soup = BeautifulSoup(response.text,"html.parser")
song_name_span = soup.select("li ul li h3")
song_list_old = [song.getText().strip() for song in song_name_span]
song_list = song_list_old[:10]
print(song_list)