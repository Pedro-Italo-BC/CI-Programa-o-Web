width = input('Coloque a largura do seu comodo em metros: ')

lenth = input('Coloque o comprimento do seu comodo em metros: ')

size = float(width) * float(lenth)

totalProduct = size / 2

formatedText = 'Será nescessario ' + str(totalProduct) + ' litros ' + ' de ' + ' produto para a realização da limpeza.'

print(formatedText)