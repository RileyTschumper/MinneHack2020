# MinneHack2020
MinneHack 2020 3rd place winner

## Demo Video
[![Watch the Video](https://img.youtube.com/vi/MC2t7IUA2lI/0.jpg)](https://www.youtube.com/watch?v=MC2t7IUA2lI&feature=emb_title)


## Inspiration
Hackathon prompt: "Develop a solution for local communities to help them foster social good"

Artists represent a local communities that provides tremendous amounts of social good, while historically having a lack of support. Art doesn't just take place in museums where plaques tell about the artist and the artwork, it is all around us. We wanted a way for people to connect with artists when they find murals, paintings and sculptures all around their community.

## What it does
After an artist finishes an art installation around the community, they can upload it SnapArt with info about themselves, the artwork, and where people can find them online. Community members can then snap a picture of the artwork and learn more about it.

## How we built it
When an artist uploads an image, it is added to our database and analyzed for key points using a scale-invariant feature transform (SIFT) algorithm. When a user scans a piece of art, the image is also analyzed for key points and referenced against the already uploaded artwork regardless of translation, rotation, and illumination that the image was taken at.

## Challenges we ran into
Ensuring that functionality is preserved across multiple devices (mobile, desktop) and browsers (Chrome, Firefox, Safari).

## Built With
* css3
* cv2
* flask
* html5
* javascript
* opencv
* python
* sift


## Devpost
https://devpost.com/software/snapart
