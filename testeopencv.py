import cv2

print(cv2.__version__)
print(cv2.__file__)

imagem = cv2.imread('opencv-python.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original',imagem)
cv2.imshow('Cinza0', imagemCinza)
cv2.waitKey()