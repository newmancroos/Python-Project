from  bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# travel_to = input("What Year would like to travel? Type the date in this format YYYY-MM-DD: ")
billboard_url="https://www.billboard.com/charts/hot-100/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
travel_to="2000-08-12"
response = requests.get(billboard_url + travel_to, headers=header)

site_content= response.text
# print(site_content)

soup = BeautifulSoup(site_content,"html.parser")

# song_list=[item.getText().strip() for item in soup.select(selector="#title-of-a-story")]
song_list=song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private", redirect_uri="https://example.com/callback", client_id="fc0bcbea6d4941968e295dcf3e547867",
        client_secret="a35abe163f794a25a9b5b72207742cdd", show_dialog=True, cache_path="token.txt", username="newmancroos"
    )
)

userid=sp.current_user()["id"]
song_uris=[]

year=travel_to.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped")

playlist = sp.user_playlist_create(user=userid, name=f"{travel_to} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)