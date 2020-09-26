import cv2

video = cv2.VideoCapture(0)
classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

while True:
    conectado, frame = video.read()

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()