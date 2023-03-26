# Compressão de Imagem usando Transformada Wavelet
Este é um script em Python para comprimir imagens usando a Transformada Wavelet Discreta 2D (DWT) e limiarização dos coeficientes wavelet. O script carrega uma imagem, aplica a DWT usando uma família wavelet especificada e, em seguida, limiariza os coeficientes de detalhe para atingir uma taxa de compressão desejada. A imagem comprimida é exibida usando o matplotlib. 

## Pré-requisitos

Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

- `matplotlib`
- `numpy`
- `pywt`
- `opencv-python`

## Como usar

1. Escolha a imagem que deseja comprimir e salve-a no diretório `images`.
2. Execute o script `compress_image.py`.
3. Defina os parâmetros de compressão, nível de decomposição e família wavelet.
4. A imagem comprimida será exibida.

## Parâmetros

- `image_path`: caminho para a imagem que deseja comprimir.
- `compression_ratio`: taxa de compressão desejada. O valor padrão é 0.8.
- `level`: nível de decomposição da wavelet. O valor padrão é 2.
- `wavelet`: família wavelet a ser usada na compressão. O valor padrão é "haar".

## Exemplo de uso

```python
# Define o caminho para a imagem
image_path = 'images/owl.jpg'

# Define a taxa de compressão
compression_ratio = 0.5

# Define o nível de decomposição
level = 2

# Define a família wavelet
wavelet='db4'

# Comprime a imagem
compress_image(image_path, compression_ratio, level, wavelet)
