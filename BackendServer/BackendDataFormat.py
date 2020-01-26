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