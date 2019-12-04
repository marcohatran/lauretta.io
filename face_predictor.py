import sys
import requests
import cv2

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def open_image(get_url):
	try:
		res = requests.get(get_url)
		msg = res.json()
		url = requests.get(msg['image_url'])
		url.raise_for_status()
	except Exception:
		print('Error occurred')

	img_name = 'test.jpg'
	with open(img_name, 'wb') as f:
		for chunk in url.iter_content(chunk_size=512):
			f.write(chunk)
	return img_name


def img_tiles(img_name):
    img = cv2.imread(img_name)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (row, col) = img_gray.shape
    square_size = row // 8
    for i in range(row // square_size):
        for j in range(col // square_size):            
            tile = img_gray[i*square_size:i*square_size+square_size,j*square_size:j*square_size+square_size]
            yield(i, j, tile)

def face_or_not(tile):
    res = face_classifier.detectMultiScale(tile, scaleFactor=1.3, minNeighbors=5)
    return len(res) > 0

def result(res, post_url):
    res = requests.post(post_url+'&playground=1', json={'face_tiles': res})
    return res.text

def face_predict(get_url, post_url):
	img_name = open_image(get_url)
	res = []
	for i, j, tile in img_tiles(img_name):
		if face_or_not(tile):
			res.append([i,j])
	msg = result(res, post_url)
	return msg

if __name__ == '__main__':
	token = 'a43e487fb3a5b7be'
	get_url = 'https://hackattic.com/challenges/basic_face_detection/problem?access_token='+token
	post_url = 'https://hackattic.com/challenges/basic_face_detection/solve?access_token='+token
	post_msg = face_predict(get_url, post_url)

	print(post_msg)


    