from flask import Flask
import spotifyalg

app = Flask(__name__)

@app.route('/')
def show_spotify():
    return spotifyalg.main()
# def hello_world():
#     return 'Hello, World!'