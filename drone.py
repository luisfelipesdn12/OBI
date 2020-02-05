#Drone de Entrega
#https://olimpiada.ic.unicamp.br/pratique/pj/2017/f1/drone/

#Dimensoes da caixa:
xBox = int(input())
yBox = int(input())
zBox = int(input())
dimensoesDaCaixa = [xBox, yBox, zBox]
dimensoesDaCaixa.sort()

#Dimensoes da janela:
hWindow = int(input())
lWindow = int(input())
dimensoesDaJanela = [hWindow, lWindow]
dimensoesDaJanela.sort()

#Resultado:
if dimensoesDaCaixa[0] <= dimensoesDaJanela[0] and dimensoesDaCaixa[1] <= dimensoesDaJanela[1]: print("S")
else: print("N")
