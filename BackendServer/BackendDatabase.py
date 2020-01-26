import json
import random

from BackendServer import BackendDataFormat

class BackendDatabase:
    artists  = []
    artworks = []

    def __init__(self):
        random.seed()
    
    def loadArtistJSON(self, jsonFile):
        data = json.load(jsonFile)
        # TODO: Load JSON file and populate self.artists and self.artworks

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

            artwork = BackendDataFormat.ArtworkData(rawArtwork["artworkName"], rawArtwork["artistID"])
            artwork.artworkID       = rawArtwork["artworkID"]
            artwork.artworkDate     = rawArtwork["artworkDate"]
            artwork.artworkLocation = rawArtwork["artworkLocation"]
            artwork.artworkImage    = rawArtwork["imagePath"]
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