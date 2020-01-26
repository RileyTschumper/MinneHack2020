class ArtistData:
    # Full name of artist:
    artistName = ""
    # URL of artist's web site
    artistSite = ""
    # UUID of artist
    artistID   = ""

    def __init__(self, artistName, artistID):
        self.artistName = artistName
        self.artistID   = artistID

class ArtworkData:
    # UUID of artwork:
    artworkID       = ""
    # Name of artwork:
    artworkName     = ""
    # UUID of artist:
    artistID        = ""
    # Date of creation:
    artworkDate     = ""
    # Location of artwork:
    artworkLocation = "" # Should this be string?
    # Features of artwork:
    artworkFeatures = None
    # Relative location (within `images`) of image file:
    artworkImage    = ""
    
    def __init__(self, artworkName, artistID):
        self.artworkName = artworkName
        self.artistID    = artistID
