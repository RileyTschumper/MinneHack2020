from BackendServer import BackendDataFormat

class BackendDatabase:
    artists  = []
    artworks = []

    def __init__(self):
        pass
    
    def loadJSONDB(self, jsonFile):
        pass
        # TODO: Load JSON file and populate self.artists and self.artworks

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