from flask import Flask, escape, request, send_from_directory, render_template
from BackendServer import BackendDatabase

flaskApp = None
database = None

def init():
    global flaskApp

    flaskApp = Flask(__name__)

    database = BackendDatabase.BackendDatabase()
    with open("JSON/artworks.json") as jsonFile:
        database.loadArtworkJSON(jsonFile)
    
    with open("JSON/artists.json") as jsonFile:
        database.loadArtistJSON(jsonFile)

    # Specifically handle root path:
    @flaskApp.route("/")
    def routeRoot():
        info1 = {"artworkName": "Testing", "artistName": "Riley T", "website": "www.rileyt.com", "numScans": 15}
        return render_template('index.html', info=info1)
        #return send_from_directory('web', "index.html")

    @flaskApp.route("/scan")
    def routeScan():
        return render_template('scan.html')

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
