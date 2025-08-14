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
        app = Flask(_ _name_ _)
        @app.route('/')
        def hello_world():
            return "Hello world!"
    </pre>

- To run the end point in
      * Mac -> <b>export FLASK_APP=hello.py</b>   and then flask run<br/>



## Notes:
<p>
    We can easily edit any html content from Chrome directly by using
    <pre>
        document.body.contentEditable=true
    </pre>
    in Chrome console. Once we edit, delete the desoign, we need to save the page as html and then we can replce the existing page our side
</p>
      * Windows  -> <b>set FLASK_APP=hellp.py</b><br/>
  and then ->  <b>flask --app hello run</b>



## Securing Password
1. Plain Password
2. Encrypt (caesar cipher - shifting letter)
3. Hashing ( Revers is not posible - Using Hashing function SHA250, SHA512. )
4. Hashing and Salting  (random charector along with user password will be hashed)  - After generating the Hashed+Salted code the Salt and generated hashed code will be saved in the user table for validating the password when the login.
   <pre>
<b>MD5 and bcrypt are both hashing algorithms, but they differ significantly in their design, intended use, and security implications, particularly for password storage.</b><br/>
**MD5 (Message-Digest Algorithm 5):** <br/>
**Purpose:** <br/>
MD5 was designed as a fast and efficient algorithm for generating fixed-size hash values for data integrity checks and message authentication.
**Speed:** <br/>
It is computationally fast, making it suitable for applications where quick hashing is required, such as verifying file integrity or creating checksums.
**Security:** <br/>
MD5 is considered cryptographically broken for security-sensitive applications like password storage due to its vulnerability to collision attacks (where two different inputs produce the same hash) and pre-image attacks (recovering the original input from the hash).

<br/><br/><br/>
**bcrypt:** <br/>
**Purpose:** <br/>
bcrypt is specifically designed for securely hashing passwords, prioritizing resistance to brute-force and rainbow table attacks.
**Speed:** <br/>
It is intentionally designed to be slow and computationally intensive, making it difficult for attackers to try many password combinations quickly. This "work factor" is adjustable, allowing the algorithm to be scaled with increasing computational power.
**Salting:** <br/>
bcrypt automatically incorporates a random salt into each password hash, meaning the same plaintext password will produce a different hash each time it's hashed. This thwarts rainbow table attacks.
**Security:** <br/>
bcrypt is considered a strong and secure algorithm for password hashing due to its adaptive nature, salting, and resistance to GPU optimization for cracking.

### Key Differences and Why bcrypt is Preferred for Passwords:
**Security:** <br/>
bcrypt's design directly addresses the vulnerabilities that make MD5 unsuitable for password hashing. Its slowness and salting mechanism significantly increase the cost and time required for attackers to compromise passwords.
**Purpose:** <br/>
MD5 is a general-purpose hashing algorithm, while bcrypt is a specialized password hashing function.
**Adaptability:** <br/>
bcrypt's adjustable work factor allows it to remain secure against increasing computational power over time, a feature MD5 lacks.
**Resistance to Attacks:** <br/>
bcrypt's design makes it resistant to brute-force attacks, rainbow table attacks, and is less susceptible to GPU acceleration compared to MD5.
In summary, while MD5 may still have non-security-critical applications, bcrypt is the recommended and industry-standard choice for securely hashing passwords due to its inherent design for security and resistance to modern attack techniques.
   </pre>
