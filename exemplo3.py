import cv2

video = cv2.VideoCapture(0)
classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
classificadorOlhos = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

while True:
    conectado, frame = video.read()
    #print(conectado)
    #print(frame)

    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesDetectada = classificadorFace.detectMultiScale(frameCinza)
    for (x,y,l,a) in facesDetectada:
        cv2.rectangle(frame, (x,y), (x + l, y + a), (0,255,00,2),5)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()