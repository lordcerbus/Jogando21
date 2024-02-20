# Iniciar um jogo de 21 
import random

valordascartas = {
'Ás' : 1,'2' : 2,'3' : 3, '4' : 4,'5' : 5,'6' : 6,'7' : 7,'8' : 8,'9' : 9, '10' :10,
'J' : 10, 'Q' : 10, 'K' : 10}
carta = ['Ás','2','3','4','5','6','7','8','9','10','J','Q','K']
naipes = [' de Ouros',' de Paus',' de Copas',' de Espadas']
valordaminhamao = 0
valordamaomaquina = 0
minhamao = []
maomaquina = []
maousu = []
maocomp = []
# Função para gerar cartas do usuario 
while len(minhamao) < 2 and len(maomaquina) < 2:
	minhamao.append(random.choice(carta))
	maomaquina.append(random.choice(carta))

for cartas in minhamao:
	valordaminhamao += valordascartas[cartas]
	cartas+= random.choice(naipes)	
	maousu.append(cartas)
print('Mão do Jogador: ',maousu)
print('Pontos Jogador: ',valordaminhamao)

for cartas in maomaquina:
	valordamaomaquina += valordascartas[cartas]
	cartas+= random.choice(naipes)	
	maocomp.append(cartas)
print('Mão do computador: ',maocomp)
print('Pontos Computador: ',valordamaomaquina)

#Decisão do usuario
decisaousuario = input('Deseja: 1-Manter 2-Desistir 3-Comprar ')
if decisaousuario == '3':
	novacarta = random.choice(carta)
	valordaminhamao += valordascartas[novacarta]
	novacarta += random.choice(naipes)
	maousu.append(novacarta)
	print(maousu)
	print(valordaminhamao)
elif decisaousuario == '1':
	print(maousu)
	print(valordaminhamao)
else:
	print('Voce desistiu')

decisaomaquina = int(random.randint(1,3))
if decisaomaquina == '3':
	print('A maquina decidiu comprar...')
	novacartamaquina = random.choice(carta)
	valordamaomaquina += valordascartas[novacartamaquina]
	novacartamaquina += random.choice(naipes)
	maocomp.append(novacartamaquina)
	print(maomaquina)
	print(valordamaomaquina)
elif decisaomaquina == '1':
	print('A maquina manteve a mão...')
	print(maocomp)
	print(valordamaomaquina)
else:
	print(' A maquina desistiu!')

if valordamaomaquina > valordaminhamao:
	print('A maquina venceu!')
elif valordamaomaquina > 21 or decisaomaquina == '2':
	print('Voce venceu!')
elif valordaminhamao > 21 or decisaousuario == '2':
	print('A maquina venceu!')
elif valordamaomaquina == '21':
	print('A maquina venceu!')
else:
	print('Voce venceu!')
