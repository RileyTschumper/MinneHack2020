import json
import random
import numpy as np
import base64
import cv2

from BackendServer import BackendDataFormat

class BackendDatabase:
    artists  = []
    artworks = []

    def __init__(self):
        random.seed()
    
    def findClosestMatch(self, image):
        encoded_data = image.split(',')[1]
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        #img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        maxSoFar = 0
        for artwork in self.artworks:
            curr = artwork.compareKeyPoints(nparr)
            if curr > maxSoFar:
                maxSoFar = curr
                bestArtwork = artwork
        if maxSoFar < 10:
            return None
        else:
            return artwork.generateJSON()
        

    def loadArtistJSON(self, jsonFile):
        data = json.load(jsonFile)
        for rawArtist in data:
            if not "artistName" in rawArtist:
                rawArtist["artistName"] = "Unnamed artist"
            if not "artistSite" in rawArtist:
                rawArtist["artistSite"] = ""
            if not "artistID" in rawArtist:
                print(" -- artistID must be defined! --")
                continue
            
            artist = BackendDataFormat.ArtistData(rawArtist["artistName"], rawArtist["artistID"])
            artist.artistSite = rawArtist["artistSite"]

            self.artists.append(artist)

    def loadArtworkJSON(self, jsonFile):
        data = json.load(jsonFile)
        for rawArtwork in data:
            if not "artworkName" in rawArtwork:
                rawArtwork["artworkName"] = "(unnamed)"
            if not "artworkID" in rawArtwork:
                rawArtwork["artworkID"] = random.randint(1, 99999999)
            if not "artistID" in rawArtwork:
                print(" -- Artist ID must be defined!!! -- ")
                continue
            if not "artworkDate" in rawArtwork:
                rawArtwork["artworkDate"] = "Undated"
            if not "artworkLocation" in rawArtwork:
                rawArtwork["artworkLocation"] = "No location"
            if not "imagePath" in rawArtwork:
                print(" -- Artwork image file path must be defined!")
                continue

            if not "scansToday" in rawArtwork:
                rawArtwork["scansToday"] = 0
            if not "scansThisWeek" in rawArtwork:
                rawArtwork["scansThisWeek"] = 0
            if not "scansThisMonth" in rawArtwork:
                rawArtwork["scansThisMonth"] = 0

            artwork = BackendDataFormat.ArtworkData(rawArtwork["artworkName"], rawArtwork["artistID"])
            artwork.artworkID       = rawArtwork["artworkID"]
            artwork.artworkDate     = rawArtwork["artworkDate"]
            artwork.artworkLocation = rawArtwork["artworkLocation"]
            artwork.artworkImage    = rawArtwork["imagePath"]
            artwork.scanHistory     = [
                rawArtwork["scansToday"],
                rawArtwork["scansThisWeek"],
                rawArtwork["scansThisMonth"]
            ]
            artwork.generateKeyPoints()

            self.artworks.append(artwork)
        pass

    def getArtistByID(self, artistID):
        for artist in self.artists:
            if(artist.artistID == artistID):
                return artist
        
        return None
    
    def getArtworkByID(self, artworkID):
        for artwork in self.artworks:
            if(artwork.artworkID == artworkID):
                return artwork
        
        return None
