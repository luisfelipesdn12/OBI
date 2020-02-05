#Arquivos
#https://olimpiada.ic.unicamp.br/pratique/p1/2015/f1/arquivos/

numeroDeArquivos = int(input())
limite = int(input())

tamanhoDosArquivos = input().split()

#transforma o input de (str) para (int)
for i in range(0, len(tamanhoDosArquivos)):
  tamanhoDosArquivos[i] = int(tamanhoDosArquivos[i])

tamanhoDosArquivos.sort()

resultado = 1 #quantas pastas serão usadas
soma = 0 #variavel de controle para o laço for

for i in range(0, numeroDeArquivos):
  tamanhoDosArquivos.remove(tamanhoDosArquivos[i])