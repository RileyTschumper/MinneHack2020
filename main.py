import cv2 
import matplotlib.pyplot as plt

# read images
img1 = cv2.imread('images/mona1.jpeg')  
img2 = cv2.imread('images/randomart1.jpeg') 

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#sift
sift = cv2.xfeatures2d.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

#feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)


index_params = dict(algorithm = 0, trees = 5)
search_params = dict()

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(descriptors_1,descriptors_2, k=2)
#matches = sorted(matches, key = lambda x:x.distance)


good_points = []
for m,n in matches:
    if m.distance < 0.6 *n.distance:
        good_points.append(m)

print("keypoints_1: ", len(keypoints_1))
print("keypoints_2: ", len(keypoints_2))


print("matches: ", len(matches))
print("good matches: ", len(good_points))
img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, good_points, None)
plt.imshow(img3),plt.show()
