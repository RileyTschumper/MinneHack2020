import cv2 
import matplotlib.pyplot as plt
import json
# Read images
image_path = 'images/mona1.jpeg'

data = {"artist_id":"0001", 'image_path':image_path}

img1 = cv2.imread(image_path)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Find key points for each image using sift
sift = cv2.xfeatures2d.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
index = ""
for point in keypoints_1:
    temp = (point.pt, point.size, point.angle, point.response, point.octave, point.class_id)
    index += str(temp) + '\n'

data['keypoints'] = index

y = json.dumps(data, index=4)
with open('JSON/data.json', 'w') as outfile:
    json.dump(data, indent=4, outfile)

