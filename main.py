from flask import Flask
from flask import render_template

import spotifyalg

app = Flask(__name__)  #making a new flask app

@app.route('/')   #when you go to the home page (the spotifyalg.py page) it will run the show_spotify func
def show_spotify():
    song_url = spotifyalg.main()  #runs the algorithm and gets the output of that algorithm and passes it to main.html
    return render_template('main.html', songurl=song_url)  #flask makes main.html as a webpage
# def hello_world():
#     return 'Hello, World!'