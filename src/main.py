from QrUtilitario.Qr import Qr
palavra = "+55(89)994545850"
#"Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis"
dado = Qr.gerar_qr(palavra)
Qr.ler_imagem("meu_qr_code.png")
