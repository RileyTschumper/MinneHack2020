<<<<<<< HEAD
from flask import Flask, escape, request, send_from_directory, render_template
#import BackendDatabase
=======
from flask import Flask, escape, request, send_from_directory
from BackendServer import BackendDatabase
>>>>>>> f7c66a6a942873ab974dac80c2c74bd1e69c0b30

flaskApp = None

def init():
    global flaskApp

    flaskApp = Flask(__name__)

    # Specifically handle root path:
    @flaskApp.route("/")
    def routeRoot():
        return render_template('index.html', name="Riley")
        #return send_from_directory('web', "index.html")

    # Serve all static web content:
    @flaskApp.route('/<path:path>')
    def sendStatic(path):
        return send_from_directory('web', path)
    
    # Serve all static images:
    @flaskApp.route('/image/<path:path>')
    def sendStaticImage(path):
        return send_from_directory('../images', path)

    # GET artist info:
    @flaskApp.route("/api/artist/<string:artistID>", methods=["GET"])
    def routeArtist(artistID):
        if request.method == "GET":
            return "Requested artist ID: %s"%(escape(artistID))
        else:
            return "NO"

def start():
    global flaskApp

    flaskApp.run()
