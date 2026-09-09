from email.mime import image

import cv2
import numpy as np
import face_recognition_models
import face_recognition

from main import known_locations, known_encodings, rgb, face_locations, distances

image_shiva=face_recognition.load_image_file('shiva.jpeg')
known_locations=face_recognition.face_locations(image_shiva)
known_encodings=face_recognition.face_encodings(image_shiva,known_locations)

known_names=["shiva"]

video=cv2.videocapture(0)

while True:
    ret,frame=video.read()
    if not ret:
        break
    small=cv2.resize(frame,(0,0),fx=0.025,fy=0.025)
    rgb=cv2.cvtColor(small,cv2.COLOR_BGR2RGB)

    face_locations=face_recognition.face_locations(rgb)
    encodings=face_recognition.face_encodings(rgb,face_locations)

    for encoding in encodings:
        distances=face_recognition.face_distance(known_encodings)
        name="unknown"

        if np.min(distances)<0.6:
            name=known_names[np.argmin(distances)]
        cv2.putText(
            frame,name,(30,50)
        )