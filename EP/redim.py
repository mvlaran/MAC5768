from PIL import Image
import os

# Script auxiliar para redimensionar as imagens originais 4000x3000 para 800x600

# Diretório onde as imagens originais estão localizadas (pasta corrente)
diretorio_original = './'

# Diretório onde as imagens originais serão movidas após o processo (subdiretório da pasta corrente)
diretorio_originais = 'originais'

# Dimensões desejadas para as imagens redimensionadas
nova_largura = 800
nova_altura = 600

# Função para redimensionar e rotacionar a imagem conforme necessário
def redimensionar_e_rotacionar(imagem, largura, altura, rotacao):
    # Rotaciona a imagem
    imagem_redimensionada = imagem.rotate(rotacao, expand = True)
    # Redimensiona a imagem
    imagem_redimensionada = imagem_redimensionada.resize((largura, altura), Image.Resampling.LANCZOS)

    return imagem_redimensionada

# Cria o diretório "originais" se ainda não existir
if not os.path.exists(diretorio_originais):
    os.makedirs(diretorio_originais)

arquivos = os.listdir(diretorio_original)

for arquivo in arquivos:
    # Apenas para imagens JPG
    if arquivo.endswith('.jpg'):
        imagem_original = Image.open(arquivo)
        
        imagem_original.save(os.path.join(diretorio_originais, arquivo))
        
        
        imagem_redimensionada = redimensionar_e_rotacionar(imagem_original, nova_largura, nova_altura, 0)
        novo_nome = os.path.splitext(arquivo)[0] + '.png'  # Altera a extensão para PNG
        imagem_redimensionada.save(novo_nome, format='PNG')
        
        os.remove(arquivo)