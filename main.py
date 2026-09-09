import cv2
import face_recognition
import numpy as np

image_shiva = face_recognition.load_image_file("Shiva.jpeg")
known_locations = face_recognition.face_locations(image_Shiva)
known_encodings = face_recognition.face_encodings(image_Shiva, known_locations)

known_names = ["Shiva"]

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, face_locations)

    for encoding in encodings:
        distances = face_recognition.face_distance(known_encodings, encoding)
        name = "Unknown"

        if np.min(distances) < 0.6:
            name = known_names[np.argmin(distances)]

        cv2.putText(
            frame, name, (30, 50),cv2.FONT_HERSHEY_SIMPLEX,  1.2, (255, 0, 0),3
        )

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()