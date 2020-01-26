import base64
import io

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
        return render_template('index.html', top_artworks=database.artworks)
        #return send_from_directory('web', "index.html")

    @flaskApp.route("/scan")
    def routeScan():
        return render_template('scan.html')
            
    @flaskApp.route('/postmethod', methods = ['POST'])
    def get_post_javascript_data():
        jsdata = request.form['javascript_data']
        print(jsdata)
        #jsdata = jsdata.split(",")
        response = database.findClosestMatch(jsdata)
        #image = io.BytesIO(base64.b64decode(jsdata[1]))
        #response = database.findClosestMatch(image)
        print(response)
        if response == None:
            return "Something"
        else:
            print(response)
            return response

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

    flaskApp.run(host="0.0.0.0", ssl_context='adhoc')
