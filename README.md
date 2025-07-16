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


## Python Web Development
### What is Flask and DJango?
    * Flask and Django are both popular web framework wrtieen in Python, but they differ significantly in their approch and features.
    # Flask:
        <b>Microframework:</b>
        - Flask is considered a "microframework" because it provides only the essential tools for building web applications, such as routing and request handling. It offers a minimalist design, giving developers more control and flexibility in choosing external libraries and components.
        - Flexibility and Customization:
                Flask does not impose a rigid project structure or specific development patterns. This allows developers to customize the framework to their needs and freely manage files, structure directories, and implement features.
        - Use Cases:
        Flask is often chosen for smaller to medium-sized projects, APIs, microservices, and rapid prototyping due to its lightweight nature and ease of setup.
    # Django:
    - Convention over Configuration:
        Django promotes a conventional structure and development patterns, which can streamline development for larger, more complex applications.
    - Use Cases:
        Django is well-suited for building large-scale, complex web applications such as content management systems (CMS), e-commerce platforms, and social networks, where rapid development and scalability are crucial. 

#Installing Flask:
- import flask   -> and then using red mark we can install it
- using Python packages incon in the Pycharm editor
- Using pip in terminal -- > pip install Flask

#Sample Web end=point:
    <pre>
    from flask import Flask
    @app.route('/')
    def hello_world():
        return "Hello world!"
    </pre>

- To run the end point in
      * Mac -> <b>export FLASK_APP=hello.py</b>   and then flask run<br/>
      * Windows  -> <b>set FLASK_APP=hellp.py</b><br/>
  and then ->  <b>flask --app hello run</b>
