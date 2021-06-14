#!/usr/bin/env python

import cv2
import rospy

def main():
	cap = cv2.VideoCapture(2)

	if not cap.isOpened():
		raise IOError("Cannot Open webcam")


	while True:
		ret, frame = cap.read()
		cv2.imshow('INput',frame)
		if cv2.waitKey(1) == 27:
			break
	cv2.destroyAllWindows()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass

