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
MD5 was designed as a fast and efficient algorithm for generating fixed-size hash values for data integrity checks and message authentication.<br/>
**Speed:** <br/>
It is computationally fast, making it suitable for applications where quick hashing is required, such as verifying file integrity or creating checksums.<br/>
**Security:** <br/>
MD5 is considered cryptographically broken for security-sensitive applications like password storage due to its vulnerability to collision attacks (where two different inputs produce the same hash) and pre-image attacks (recovering the original input from the hash).

<br/><br/>
**bcrypt:** <br/>
**Purpose:** <br/>
bcrypt is specifically designed for securely hashing passwords, prioritizing resistance to brute-force and rainbow table attacks.<br/>
**Speed:** <br/>
It is intentionally designed to be slow and computationally intensive, making it difficult for attackers to try many password combinations quickly. This "work factor" is adjustable, allowing the algorithm to be scaled with increasing computational power.<br/>
**Salting:** <br/>
bcrypt automatically incorporates a random salt into each password hash, meaning the same plaintext password will produce a different hash each time it's hashed. This thwarts rainbow table attacks.<br/>
**Security:** <br/>
bcrypt is considered a strong and secure algorithm for password hashing due to its adaptive nature, salting, and resistance to GPU optimization for cracking.<br/>

### Key Differences and Why bcrypt is Preferred for Passwords:
**Security:** <br/>
bcrypt's design directly addresses the vulnerabilities that make MD5 unsuitable for password hashing. Its slowness and salting mechanism significantly increase the cost and time required for attackers to compromise passwords.<br/>
**Purpose:** <br/>
MD5 is a general-purpose hashing algorithm, while bcrypt is a specialized password hashing function.<br/>
**Adaptability:** <br/>
bcrypt's adjustable work factor allows it to remain secure against increasing computational power over time, a feature MD5 lacks.<br/>
**Resistance to Attacks:** <br/>
bcrypt's design makes it resistant to brute-force attacks, rainbow table attacks, and is less susceptible to GPU acceleration compared to MD5.<br/>
In summary, while MD5 may still have non-security-critical applications, bcrypt is the recommended and industry-standard choice for securely hashing passwords due to its inherent design for security and resistance to modern attack techniques.
   </pre>

### Werkzeug webpag : https://werkzeug.palletsprojects.com/en/stable/utils/#module-werkzeug.security
### Flask Login Document : https://flask-login.readthedocs.io/en/latest/
### Flask Messages : https://flask.palletsprojects.com/en/stable/patterns/flashing/



## Salt Round
- Adding salt to a password and Hashing it is Round One <br/>
- Adding Salt to the Password and Hasing, and then adding another salt to the Hashed code and then Hashing it again is Rout Two. It will go more round

## Github push an existing project

1. Install Gitbash
2. Within working directory -. git init
3. git status  ->  gives pending commit files
4. git add . --> Ready to commit
5. git commit -m "message"   --> it will locally commit the changes
6. git log  -> give details about the last commit
7. Git add adds the files to staging and then git commit adds it to local git
8. git checkout . will rollback any pending commit (after git add )
9. git diff filename   --> give the different between add/ committed file

10. git remote add origin <GitHub .git path>
11. //git branch -M main  -> This step no need
12. git push -u origin main


### To remove file from staging but not rollback the local copy  -> <b>git rm --cached -r . </b>


## Great collection of projects
https://github.com/awesome-selfhosted/awesome-selfhosted

## What is Fork in github  -> We can make copy of someone's repository under our github account. whole repository will be copied into our githuib.


## Hosting Python Application:

WSGI stands for **Web Server Gateway Interface** and it's described here: https://www.python.org/dev/peps/pep-3333/

In summary: normal web servers can't run Python applications, so a special type of server was created (WSGI) to run our Flask app.  Essentially, a WSGI server standardises the language and protocols between our Python Flask application and the host server.

There are many WSGIs to choose from, but we'll use the most popular -** gunicorn**. That way our hosting provider will call gunicorn to run our code.

Next, we need to tell our hosting provider about our gunicorn server, what our app is called, and how to run our Flask app. We do that using a config file called a Procfile.

### Creating a Procfile
<p>

    3. Create a new file in the project top-level folder called Procfile. When you create the new file, PyCharm will prompt you to track the new file under git version control. Agree by clicking add.

NOTE: make sure you spell the name of the file exactly as you see above, with a capital P and no file extension.

Type the following into the Procfile:



web: gunicorn main:app


This will tell our hosting provider to create a web worker that is able to receive HTTP requests. The Procfile also says to use gunicorn to serve your web app. And finally it specifies the Flask app object is the main.py file. That way the hosting provider knows about the entry point for the app and what our app is called.


</p>
<p>
    Create an account with a hosting provider
There are many different hosting providers to choose from when it comes to making your app go live on the internet. Features and pricing vary between them and their pricing plans can change. It's up to you who you want to choose. For this tutorial, I will show you how to host on render.com <br/>
<pre>
Provider                   ~Cost / Month           Name of Plan

Heroku                                $5                      Eco & Basic

render                                  $0                      Individual

Cyclic                                   $0                      Free Forever

Glitch                                   $0                      Starter

Vercel                                  $0                       Hobby

PythonAnywhere              $0                       Beginner 
</pre>
</p>

<p>
    The nice thing about most of these providers is that they can easily deploy your app straight from a GitHub repo. We've done most of the difficult bits already. There are just a few steps left:

1. Create an account with the hosting provider

2. Link our GitHub repo with the host

3. Set up a PostgreSQL database with the host

4. Store the key-value pairs for our environment variables with our host



Create an account e.g., on render.com


Heroku discontinued their free plan, but other providers are still offering one. You can create an account on render.com simply by signing up via Github.

<img width="3044" height="978" alt="image" src="https://github.com/user-attachments/assets/46904683-c319-4230-9f22-2fefda163a21" />

Click "authorize" and confirm your email address. Job done.
<img width="1344" height="1758" alt="image" src="https://github.com/user-attachments/assets/b7400bdd-1331-4485-bcb0-e17b056950fb" />

**Create a new Web Service**
<img width="1358" height="880" alt="image" src="https://github.com/user-attachments/assets/bb085dbc-3e67-4a71-8c3e-9324dce108c6" />
Choose your blog app that you've uploaded to GitHub and connect your repo

<img width="1718" height="684" alt="image" src="https://github.com/user-attachments/assets/7ffc3307-429d-438c-8045-53a7003b3e24" />

**Edit the Start Command**
Most of render.com's defaults are fine. All you need to do is pick a name for your project and then change the Start Command to:

_gunicorn main:app_

<img width="1318" height="576" alt="image" src="https://github.com/user-attachments/assets/e0d6dca9-e201-496d-83b4-5847dbb1aa1d" />

**Add your first environment variable**
Before you create your web service, click "Advanced" and add your environment variable your Flask app.

<img width="3406" height="616" alt="image" src="https://github.com/user-attachments/assets/ca5ee445-3dc7-4383-8cb8-db76a56b5441" />
Scroll to the bottom and create your web service.

<img width="546" height="172" alt="image" src="https://github.com/user-attachments/assets/107f0a4d-1eae-4609-a0bc-48017092d8c6" />

Your web app won't work yet, however. We first need to set up our database and set the environment variable for SQLAlchemy.
</p>


**Create a new Postgres Database**

1. Create a new Postgres database from the website menu.

<img width="934" height="1028" alt="image" src="https://github.com/user-attachments/assets/b165fd0e-f77f-4bb3-87b9-625661e2468e" />

Next, you will see a form. All you need to do is pick a name for the database and create it. <br/>

<img width="2558" height="1288" alt="image" src="https://github.com/user-attachments/assets/a0c2fcb0-ca58-4f79-96f5-d5bef509f70b" />

**Copy the internal database URL**
Once you've created your database, go and find the Internal Database URL in the Info section. You might have to wait a little while until your database is created.


<img width="2518" height="1165" alt="image" src="https://github.com/user-attachments/assets/60a5c98e-7255-4abf-904c-b3253645d866" />

Afterwards, simply copy this URL. You will shortly use this as an environment variable.

<img width="1278" height="544" alt="image" src="https://github.com/user-attachments/assets/dd8e3cbf-0ea7-4418-8e4e-80ce5992d0f6" />

**Set your SQLALCHEMY_DATABASE_URI environment variable**
Go back to your web service settings called "environment".  Create an environment variable that matches the name of the key you're using in the main.py.


<img width="3792" height="740" alt="image" src="https://github.com/user-attachments/assets/6b0d05ae-9b25-4841-8eb4-be89069d0fcf" />

**Paste your internal database URL as the key value. It should look something like this:**

**postgres://example_ig2c_user:u0E_lots_of_Symbols_here@dpg-c_more_symbols3bj85d0-a/example_ig2c**

You just need to make one small modification. Change the first part from ** postgres to postgresql**. The URI has to start with "postgresql" because this is required by SQLAlchemy:


<img width="2552" height="1142" alt="image" src="https://github.com/user-attachments/assets/f3aa5028-3433-4549-a192-5967d4298662" />




Reder will automatically deploy the changes. If we get any error like 
<pre>
    AssertionError: Class <class 'sqlalchemy.sql.elements.SQLCoreOperations'> directly inherits TypingOnly but has additional attributes
</pre>

run 
<pre>
    pip install --upgrade Flask-SQLAlchemy SQLAlchemy
</pre>
 and noted the latest version of SqlAlchemy and updated the version in the requirements.txt and push the changes to github.

## Pandas Data managing and reporting

Today's Learning Points



* Use **.head(), .tail(), .shape and .columns** to explore your DataFrame and find out the number of rows and columns as well as the column names.

* Look for NaN (not a number) values with **.findna()** and consider using **.dropna()** to clean up your DataFrame.

* You can access entire columns of a DataFrame using the square bracket notation: **df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]**

* You can access individual cells in a DataFrame by chaining square brackets **df['column name'][index] or using df['column name'].loc[index]**

* The largest and smallest values, as well as their positions, can be found with methods like **.max(), .min(), .idxmax() and .idxmin()**

* You can sort the DataFrame with** .sort_values() and add new columns with .insert()**

* To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the **.groupby() **method, **mean()**

<pre>
    import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
# df
# df.head() #display first page
#df.shape   #number of rows and columns
#df.columns  #listdown all columns
#df.isna()   # check if there is NAN value in any column
# df.tail()  # display last page records

clean_df = df.dropna()
# clean_df.tail()
# clean_df["Starting Median Salary"]
# clean_df["Starting Median Salary"].max()  #Gives Maximum Starting Median Salary column value from entrire DataFrame
# clean_df["Starting Median Salary"].idxmax()  #Gives the index of the max column name
# clean_df["Undergraduate Major"].loc[clean_df["Starting Median Salary"].idxmax()]  # Give a particular column that blong to a max Starting Medium Salary
# clean_df.loc[43] # Display Entire rows

# clean_df.loc[clean_df["Mid-Career Median Salary"].idxmax()]  #["Undergraduate Major"]

spread_col = clean_df["Mid-Career 90th Percentile Salary"].subtract(clean_df["Mid-Career 10th Percentile Salary"])
clean_df.insert(1,"Spread",spread_col)
clean_df.tail()

#low_risk = clean_df.sort_values("Spread", ascending=True)
# low_risk["Undergraduate Major"]
#low_risk[["Undergraduate Major","Spread"]].head()

#We have three categories in the 'Group' column: STEM, HASS and Business. Let's count how many majors we have in each category:
# clean_df.groupby('Group').count()

#for Mean
# clean_df.groupby('Group').mean()  #not working because there is npon nunberic fields Undergraduate Major is there.

pd.options.display.float_format = '{:,.2f}'.format
for_mean = clean_df[["Starting Median Salary","Spread","Mid-Career Median Salary","Group"]]
for_mean.groupby('Group').mean()

</pre>


* Change engtire column to Date:
<pre>
    df.DATE =pd.to_datetime(df.DATE)
    
    df.head()
</pre>


## Matplotlib
<p>
    To create our first charts we're going to use a library called Matplotlib. There are many different libraries in Python to help us create charts and graphs. Matplotlib is an incredibly popular one and it works beautifully in combination with Pandas
</p>

<pre>
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv('QueryResults.csv', names=['DATE','TAG','POSTS'], header=0)
    df.groupby("TAG").count()
    df.groupby("TAG").sum()
    df["DATE"][0]
    pd.to_datetime(df["DATE"][0])
    type(pd.to_datetime(df["DATE"][1]))
    df.DATE =pd.to_datetime(df.DATE)

    reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df
# reshaped_df.columns
# reshaped_df.count()
reshaped_df.fillna(0, inplace=True)
# reshaped_df.isna().values.any()
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df['java'])
</pre>

<p>
    Styling the Chart

Let's look at a couple of methods that will help us style our chart:

.figure() - allows us to resize our chart

.xticks() - configures our x-axis

.yticks() - configures our y-axis

.xlabel() - add text to the x-axis

.ylabel() - add text to the y-axis

.ylim() - allows us to set a lower and upper bound
</p>
