###########################################
#
#   Software para Gerar dias dependendo do mes.
#   A formatação é feita conforme a necessidade
#   de um outro software que eu havia criado
#   previamente (pode ser mudado conforme
#   a necessidade)
#
###########################################








def gerdata():
  mes=int(input("Qual mes quer gerar os dias? "))
  global dia 
  global diager
  dia=0
  if mes%2 == 0:
    while dia <= 29 : 
      dia+=1
      diager=(str(dia)+"/"+str(mes))
      print(diager+str("  :  :"))
  else:
    while dia <= 30 : 
      dia+=1
      diager=(str(dia)+"/"+str(mes))
      print(diager+str("  :  :"))

def randnumb():
  import random
  tel=0
  while tel <= 8 :
    tel+=1
    for n in range(10):
      n=random.randint(0,9)
    print(str(n)+str(n))

gerdata()


