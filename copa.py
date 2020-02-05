#Copa
#https://olimpiada.ic.unicamp.br/pratique/pj/2018/f2/copa/

#Posição nas oitavas
K = int(input()) #Kung
L = int(input()) #Lu

#Definindo dois "grupos" de oitavas
primeiroGrupoOitavas = [1, 2, 3, 4, 5, 6, 7, 8]
segundoGrupoOitavas = [9, 10 , 11, 12, 13, 14, 15, 16]

#Se estiverem em "grupos" (de oito) diferentes, só se encontraram nas finais
if (K in primeiroGrupoOitavas and L in segundoGrupoOitavas) or (L in primeiroGrupoOitavas and K in segundoGrupoOitavas):
  resultado = 'final'

#Se estiverem em "grupos" (de oito) iguais:
#Grupo 1:
elif (K in primeiroGrupoOitavas and L in primeiroGrupoOitavas):
	primeiroGrupoQuartas = [1, 2, 3, 4]
	segundoGrupoQuartas = [5, 6, 7, 8]
	if (K in primeiroGrupoQuartas and L in segundoGrupoQuartas) or (L in primeiroGrupoQuartas and K in segundoGrupoQuartas):
		resultado = "semifinal"
#Grupo 2:
elif(K in segundoGrupoOitavas and L in segundoGrupoOitavas):
	primeiroGrupoQuartas = [9, 10, 11, 12]
	segundoGrupoQuartas = [13, 14, 15, 16]
	if (K in primeiroGrupoQuartas and L in segundoGrupoQuartas):
		resultado = "semifinal"

#Exibir o resultado:
print(resultado)