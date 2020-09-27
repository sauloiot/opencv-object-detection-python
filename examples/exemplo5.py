import cv2
#captura de imagem

classificador = cv2.CascadeClassifier('../cascades/haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
amostra = 1
numeroAmostras = 5
id = input('Digite seu identificador: ')
largura, altura = 220, 220
print("capturando as faces .....")

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,0,255), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))

            cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
            print("[foto "+ str(amostra) + " capturada com Sucesso]")
            amostra += 1


    cv2.imshow("Face", imagem)
    cv2.waitKey(1)
    if (amostra >= numeroAmostras +1):
        break

print ("Faces Capturadas com Sucesso!")
camera.release()
cv2.destroyAllWindows()