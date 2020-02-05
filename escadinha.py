#Escadinha
#https://olimpiada.ic.unicamp.br/pratique/p1/2018/f1/escadinha/

tamanhaDaSequencia = int(input()) #Define tamanho da sequencia

sequencia = input().split()
for i in range(0, tamanhaDaSequencia):
  sequencia[i] = int(sequencia[i])
#^ Define uma lista com os numeros da sequencia ^

final = 1 
if tamanhaDaSequencia == 1 or 2:
  print(final)
else:
  dif_atual = sequencia[0] - sequencia[1]
  for i in range(1, tamanhaDaSequencia - 1):
    dif_nova = sequencia[i] - sequencia[i+1]
    if dif_atual != dif_nova:
      dif_atual = dif_nova
      final += 1


print("TS: ", tamanhaDaSequencia)
print("SE: ", sequencia)
print("FI: ", final)