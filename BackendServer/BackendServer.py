from flask import Flask, escape, request, send_from_directory
#import BackendDatabase

flaskApp = None

def init():
    global flaskApp

    flaskApp = Flask(__name__)

    @flaskApp.route("/")
    def routeRoot():
        return send_from_directory('web', "index.html")

    @flaskApp.route('/<path:path>')
    def sendStatic(path):
        return send_from_directory('web', path)
    
    @flaskApp.route('/image/<path:path>')
    def sendStaticImage(path):
        return send_from_directory('../images', path)

    @flaskApp.route("/api/artist/<string:artistID>", methods=["GET"])
    def routeArtist(artistID):
        if request.method == "GET":
            return "Requested artist ID: %s"%(escape(artistID))
        else:
            return "NO"

def start():
    global flaskApp

    flaskApp.run()