import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

data_path = r'D:\Data Science\Face Recognition Project\Dataset'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

Training_Data, Labels = [], []

for i, files in enumerate(onlyfiles):
    image_path = join(data_path, onlyfiles[i])
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if images is not None:
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    else:
        print(f"Image {image_path} not loaded properly. Skipping.")

Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Dataset Model Training Complete!!!!!")

face_classifier = cv2.CascadeClassifier(
    r'D:\pythonProject\Basics\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')


def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return img, np.array([])

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi = gray[y:y + h, x:x + w]  # Fix here: use gray image instead of the entire frame
        roi = cv2.resize(roi, (200, 200))

    return img, roi


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        if face.size != 0:  # Check if face is not empty
            result = model.predict(face)  # Pass the face directly to the recognizer

            if result[1] < 500:
                confidence = int(100 * (1 - result[1] / 300))
                cv2.putText(image, f"Confidence: {confidence}%", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                if confidence > 75:
                    image = cv2.putText(image, "Ali Hadi", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            else:
                cv2.putText(image, "Unknown", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow('Face Cropper', image)

        cv2.waitKey(1)  # Added waitKey here

    except Exception as e:
        print(str(e))

    if cv2.waitKey(1) & 0xFF == 13:
        break

cap.release()
cv2.destroyAllWindows()
