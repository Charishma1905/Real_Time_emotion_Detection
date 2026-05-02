import cv2
from fer import FER

detector = FER(mtcnn=True)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    emotions = detector.detect_emotions(frame)
    
    for face in emotions:
        (x, y, w, h) = face["box"]
        emotion, score = max(face["emotions"].items(), key=lambda item: item[1])

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, emotion, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

