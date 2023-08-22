# Importa a classe Qr do módulo QrUtilitario.Qr
from QrUtilitario.Qr import Qr

# Define uma palavra que será transformada em QR Code
palavra = "Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis"
#"+55(89)994545850"

# Gera um QR Code a partir da palavra usando o método estático gerar_qr da classe Qr
# O resultado é armazenado na variável 'dado'
dado = Qr.gerar_qr(palavra)
# Ler uma imagem contendo um QR Code usando o método estático ler_imagem da classe Qr
Qr.ler_imagem("meu_qr_code.png")
