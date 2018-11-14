import face_recognition
import cv2
import time
import os
import pyautogui

def FaceInPhoto(photopath):
	image = face_recognition.load_image_file(photopath)
	#打开图像
	face_locations = face_recognition.face_locations(image)
	if(len(face_locations)!=1):
		print("Error!There is more than one face in the picture")
		return -1
	else:
		top, right, bottom, left = face_locations[0]
		face_image = image[top:bottom,left:right]
		cv2.imwrite(photopath,face_image)


def TakePhoto(filename): #para 0 表示拍的时owner的照片，1表示是是当前使用者的照片
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
	unknown_image = face_recognition.load_image_file(unknown)

	owner_encoding = face_recognition.face_encodings(known_image)[0] #encode
	unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

	results = face_recognition.compare_faces([owner_encoding], unknown_encoding)
	if(results[0] == True):
		print("Compare success!")
		return 0
	else:
		print("Compare fail!")
		return -1

lock = 0
while(1):
	if(lock == 1):
		TakePhoto("unknown.jpg")
		if(FaceInPhoto("unknown.jpg")):
			continue
		if(COMPARE("owner.jpg","unknown.jpg")==0):
			pyautogui.hotkey("esc")
			time.sleep(1.5)
			pyautogui.typewrite("maoyi1003")
			pyautogui.hotkey("enter")
			lock = 0
		continue
	TakePhoto("unknown.jpg")
	number = FaceInPhoto("unknown.jpg")
	if(number == -1):
		pyautogui.keyDown('ctrl')
		pyautogui.keyDown('command')
		pyautogui.keyDown('q')
		pyautogui.keyUp('ctrl')
		pyautogui.keyUp('command')
		pyautogui.keyUp('q')
		lock = 1
		continue
	if(COMPARE("owner.jpg","unknown.jpg")==-1):
		pyautogui.keyDown('ctrl')
		pyautogui.keyDown('command')
		pyautogui.keyDown('q')
		pyautogui.keyUp('ctrl')
		pyautogui.keyUp('command')
		pyautogui.keyUp('q')
		lock = 1
		continue