import qrcode
'''
qrcode é uma biblioteca que permite criar códigos QR (Quick Response) que são tipos de códigos de barras bidimensionais que podem ser escaneados por dispositivos móveis, câmeras e outros dispositivos para rapidamente acessar informações, URLs, mensagens, entre outros tipos de dados.
'''
import numpy as np
'''
numpy é uma biblioteca amplamente usada para trabalhar com arrays multidimensionais e realizar cálculos numéricos eficientes.
'''
import cv2
"""
Open Source Computer Vision Library (OpenCV) ou cv2 é uma biblioteca amplamente utilizada para processamento de imagens e visão computacional. Ele oferece uma ampla gama de funções e ferramentas para manipulação, análise e processamento de imagens e vídeos em tempo real.
"""

class Qr:
    """
    Classe para gerar e ler códigos QR.
    """
     

    def gerar_qr(palavra: str, nome_da_imagem:str = "meu_qr_code.png", exibir_mensagens: bool = True) -> bool:
        """
        Gera um código QR a partir de uma palavra fornecida e salva-o como uma imagem.

        Parâmetros:
            palavra (str): Texto que será codificado no QR Code.
            nome_da_imagem (str, opcional): Nome do arquivo de imagem para salvar o QR Code. Padrão é "meu_qr_code.png".
            exibir_mensagens (bool, opcional): Se True, exibe mensagens de informação. Padrão é True.

        Retorna:
            bool: True se o QR Code foi gerado e salvo com sucesso, False se houver um erro.
        """

        if(len(palavra) > 4296):  #permite ler uma palavra de até 4296 caracteres.
            print('Limite de caracteres utrapassado. A palavra deve ter no maximo 4296 caracteres incluindo pontuações')
            return False

        QRimage = qrcode.make(palavra)
        QRimage.save(nome_da_imagem)
        if(exibir_mensagens):
            print(f"Quantidade de caracteres: {len(palavra)}")
            print(f'Imagem salva: \"{nome_da_imagem}\"')

        return True
           
    def ler_imagem(caminho_da_imagem: str) -> str:
        """
        Lê um código QR de uma imagem e retorna os dados decodificados.

        Parâmetros:
            caminho_da_imagem (str): Caminho para o arquivo de imagem contendo o código QR.

        Retorna:
            str: Dados decodificados do código QR. Retorna uma string vazia se a leitura não for bem-sucedida.
        """

        # Carregar uma imagem a partir do caminho especificado
        imagem = cv2.imread(caminho_da_imagem)

        # Criar um objeto QRCodeDetector do OpenCV para detecção e decodificação de QR Code
        qr = cv2.QRCodeDetector()

        # Detectar e decodificar o QR Code na imagem
        # A função detectAndDecode() retorna os dados decodificados, os vértices dos quadrados do QR Code e os binários
        dados, vertices, binarios = qr.detectAndDecode(imagem)

        # Verificar se a detecção e decodificação foram bem-sucedidas (se há vértices)
        if vertices is not None:
            # Imprimir os dados decodificados (a palavra contida no QR Code)
            print(f"Palavra decodificada: \"{dados}\"")
            # Retornar os dados decodificados
            return dados
        else:
            # Se não houver vértices, a detecção e decodificação falharam
            print("Não foi possivel ler a imagem")
            # Retornar uma string vazia para indicar a falha na leitura
            return ""
