#!/Users/peter/.virtualenvs/cv/bin/python3
#coding=utf-8
import face_recognition
import cv2
import time
import os
import pyautogui

def numberof(photopath):
	image = face_recognition.load_image_file(photopath)
	face_locations = face_recognition.face_locations(image,model = "cnn")
	return len(face_locations)

def cutface(photopath):
	image = face_recognition.load_image_file(photopath)
	face_locations = face_recognition.face_locations(image)
	if(len(face_locations)!=1):
		return -1
	else:
		top, right, bottom, left = face_locations[0]
		face_image = image[top:bottom,left:right]
		cv2.imwrite(photopath,face_image)

	return 0


def TakePhoto(cap,filename): #
    """使用opencv拍照"""
    # cap = cv2.VideoCapture(0)  # 默认的摄像头
    time.sleep(1)#camera启动需要一定时间
    while True:
        ret, frame = cap.read()
        if ret:
            # 等待1s
            if cv2.waitKey(1):
	            cv2.imwrite(filename, frame)
	            break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def TakePhoto(filename): #
    """使用opencv拍照"""
    cap = cv2.VideoCapture(0)  # 默认的摄像头
    time.sleep(1)#camera启动需要一定时间
    while True:
        ret, frame = cap.read()
        if ret:
            # 等待1s
            if cv2.waitKey(1):
	            cv2.imwrite(filename, frame)
	            break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def COMPARE(owner,unknown):
	known_image = face_recognition.load_image_file(owner)#读入图片文件
	print(known_image)
	unknown_image = face_recognition.load_image_file(unknown)
	# try:
	# 	owner_encoding = face_recognition.face_encodings(known_image)[0] #encode
	# 	unknown_encoding = face_recognition.face_encodings(unknown_image)
	# except:
	# 	print("There is no face in the image")
	# 	return -1
	# try:
	owner_encoding = face_recognition.face_encodings(known_image)[0] #encode
	# except IndexError:
		# print(owner_encoding)
	unknown_encoding = face_recognition.face_encodings(unknown_image)
	for x in range(len(unknown_encoding)):
		results = face_recognition.compare_faces([owner_encoding], unknown_encoding[x], 0.4)
		if(True in results):
			print("success")
			return 0
	print("fail")
	return -1
# TakePhoto("/home/foenix/LockApp/owner.jpg")
# cutface("owner.jpg")
