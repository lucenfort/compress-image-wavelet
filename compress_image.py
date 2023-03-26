import matplotlib.pyplot as plt
import numpy as np
import pywt
import cv2

def compress_image(image_path, compression_ratio=0.8, level=2, wavelet='haar'):
    # Carrega a imagem usando opencv
    img = cv2.imread(image_path)
    
    # Converte a imagem para escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplica wavelet 2D na imagem
    coeffs = pywt.dwt2(img_gray, wavelet)
    cA, (cH, cV, cD) = coeffs
    
    # Verifica o número de níveis de decomposição suportados pelos coeficientes
    max_level = pywt.dwtn_max_level(img_gray.shape, wavelet)
    level = min(level, max_level)
    
    # Define o nível de decomposição
    coeffs = cA, (cH * 0, cV * 0, cD * 0)
    for i in range(level-1):
        coeffs = pywt.idwt2(coeffs, wavelet)
        cA, (cH, cV, cD) = pywt.dwt2(coeffs, wavelet)
        coeffs = cA, (cH * 0, cV * 0, cD * 0)
    
    # Calcula a energia total dos coeficientes de detalhe
    energy = (cH ** 2 + cV ** 2 + cD ** 2).sum()
    
    # Calcula a energia necessária para atingir o grau de compressão especificado
    target_energy = energy * compression_ratio
    
    # Percorre os coeficientes de detalhe do nível de decomposição mais alto para o mais baixo
    # e define os coeficientes como zero até atingir o target_energy
    coeffs_list = [cH, cV, cD]
    for coeffs in coeffs_list:
        for i in range(level):
            coeffs_shape = coeffs.shape[0] // (2 ** i), coeffs.shape[1] // (2 ** i)
            flat_coeffs = coeffs[:coeffs_shape[0], :coeffs_shape[1]].ravel()
            sorted_coeffs = np.sort(np.abs(flat_coeffs))
            cum_energy = np.cumsum(sorted_coeffs ** 2)
            idx = np.where(cum_energy >= target_energy)[0][0]
            threshold = sorted_coeffs[idx]
            flat_coeffs[np.abs(flat_coeffs) <= threshold] = 0
            coeffs[:coeffs_shape[0], :coeffs_shape[1]] = flat_coeffs.reshape((coeffs_shape[0], coeffs_shape[1]))
    
    # Reconstrói a imagem a partir dos coeficientes
    coeffs = cA, (cH, cV, cD)
    for i in range(level-1):
        coeffs = pywt.idwt2(coeffs, wavelet)
    compressed_image = np.uint8(coeffs)
    
    # Mostra a imagem comprimida
    plt.imshow(compressed_image, cmap='gray')
    plt.axis('off')
    plt.title('Imagem Comprimida')
    plt.show()

# Define o caminho para a imagem
image_path = 'images/owl.jpg'

# Define a taxa de compressão
compression_ratio = 0.5

# Define o nível de decomposição
level = 2

# Define a familia wavelet
wavelet='db4'

# Comprime a imagem
compress_image(image_path, compression_ratio, level)
