# Python-Project

## 1. How to Open Command Paltte in Code:
    - View -> Command Palette (OR)
    - Ctrl + Shift + P

## 2. Select Correct Python Version for development in Code
  - Type    python : select interpreter and select the correct version of Python


## How to open Terminal
    - Click Terminal menu and Select Terminal (OR)
    - Ctrl + Shift + ~  (next to number 1)
    - To open an existing terminal but we closed it then ctrl + ~

## Get the Python version
    - Type py -3 --version in Wonrdown
    - type python3 --version in other operating system

## Launch python
    - Type py in terminal in windows
    - Type python in other Operating system


    
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private", redirect_uri="https://example.com/callback", client_id="fc0bcbea6d4941968e295dcf3e547867",
        client_secret="a35abe163f794a25a9b5b72207742cdd", show_dialog=True, cache_path="token.txt", username="newmancroos"
    )
)
