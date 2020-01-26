from flask import Flask, escape, request

flaskApp = None

def init():
    global flaskApp

    flaskApp = Flask(__name__)

    @flaskApp.route("/")
    def rootRoute():
        return "Nothing here..."

def start():
    global flaskApp
    
    flaskApp.run()