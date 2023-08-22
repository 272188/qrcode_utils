import qrcode
import numpy as np
import cv2

class Qr:
    def gerar_qr(palavra: str, nome_da_imagem:str = "meu_qr_code.png", exibir_mensagens: bool = True) -> bool:
        if(len(palavra) > 4296):
            print('Limite de caracteres utrapassado. A palavra deve ter no maximo 4296 caracteres incluindo pontuações')
            return False

        QRimage = qrcode.make(palavra)
        QRimage.save(nome_da_imagem)
        if(exibir_mensagens):
            print(f"Quantidade de caracteres: {len(palavra)}")
            print(f'Imagem salva: \"{nome_da_imagem}\"')

        return True
           
    def ler_imagem(caminho_da_imagem: str) -> str:
        imagem = cv2.imread(caminho_da_imagem)
        qr = cv2.QRCodeDetector()
        dados, vertices, binarios = qr.detectAndDecode(imagem)

        if vertices is not None:
            print(f"Palavra decodificada: \"{dados}\"")
            return dados
        else:
            print("Não foi possivel ler a imagem")
            return ""
