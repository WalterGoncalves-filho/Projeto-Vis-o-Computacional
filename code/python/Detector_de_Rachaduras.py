import cv2
import numpy as np
# Carregar imagem
imagem = cv2.imread('D:\IFAM\Projeto_Integrador_1\images\image1.png')# , cv2.IMREAD_GRAYSCALE
imagem = cv2.resize(imagem, (562, 426))
cv2.imshow('Imagem', imagem)
print(imagem.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)# imagem preto e branco
cv2.imshow('Imagem preto e branco', imagem_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Aplicar filtro para remoção de ruído
imagem_filtrada = cv2.GaussianBlur(imagem_gray, (5, 5), 0)
# Detectar bordas usando Canny
bordas = cv2.Canny(imagem_filtrada, 50, 150)
# Mostrar resultado
cv2.imshow('Rachaduras Detectadas', bordas)
cv2.waitKey(0)
cv2.destroyAllWindows()