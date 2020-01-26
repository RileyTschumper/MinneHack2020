import json
import random
import numpy as np
import base64
import cv2
import matplotlib.pyplot as plt

from BackendServer import BackendDataFormat

class BackendDatabase:
    artists  = []
    artworks = []

    def __init__(self):
        random.seed()
    
    def findClosestMatch(self, imageURI):
        encoded_data = imageURI.split(',')[1]
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        #img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #plt.imshow(image),plt.show()
        sift = cv2.xfeatures2d.SIFT_create()

        keyPoints, descriptors = sift.detectAndCompute(image, None)

        maxSoFar = 0
        #print(self.artworks)
        for artwork in self.artworks:
            curr = artwork.compareKeyPoints(descriptors)
            print(curr)
            if curr > maxSoFar:
                maxSoFar = curr
                bestArtwork = artwork
        if maxSoFar < 10:
            return None
        else:
            return bestArtwork.generateJSON()
        

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
            artwork.artistName      = rawArtwork["artistName"]
            artwork.artistWebsite   = rawArtwork["artistWebsite"]
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
