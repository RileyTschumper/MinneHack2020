import cv2

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
    artworkID        = ""
    # Name of artwork:
    artworkName      = ""
    # UUID of artist:
    artistID         = ""
    # Date of creation:
    artworkDate      = ""
    # Location of artwork:
    artworkLocation  = "" # Should this be string?
    # Key points:
    artworkKeyPoints = None
    # Key point descriptors:
    artworkDescriptors = None
    # Relative location (within `images`) of image file:
    artworkImage     = ""
    
    def __init__(self, artworkName, artistID):
        self.artworkName = artworkName
        self.artistID    = artistID
    
    def generateKeyPoints(self):
        image = cv2.imread('../images/%s'%(self.artworkImage))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        sift = cv2.xfeatures2d.SIFT_create()

        self.artworkKeyPoints, artworkDescriptors = sift.detectAndCompute(image, None)

    def compareKeyPoints(self, otherImage):
        image = cv2.imread(otherImage)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        sift = cv2.xfeatures2d.SIFT_create()

        keyPoints, descriptors = sift.detectAndCompute(image, None)

        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

        index_params = dict(algorithm = 0, trees = 5)
        search_params = dict()

        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(self.artworkDescriptors, descriptors, k=2)
