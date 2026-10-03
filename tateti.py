#ta te ti

juego = [
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]  ]
partidas = 0

def jugar():
	global jug
	global partidas
	jugador = partidas % 2
	partidas += 1
	print(f"jugador {jug[ jugador]} comiensa")
	ganado = 0
	while ganado == 0:
		tabla()
		poner_pieza(jugador)
		ganado = detecganador(juego)
		if ganado == 0:
			print(f"ahora va {jug[1 - jugador]}")
			jugador = 1 - jugador
		elif ganado == 1:
			print(f"{jug[jugador]} gano")
		else:
			print("empate")
	tabla()

def detecganador(juego):
	for col in juego: #comprobando columnas
		if col[0] == col[1] == col[2] != 0:
			return 1
	for fila in juego: #comprueba filas
		if fila[0] == fila[1] == fila[2] != 0:
			return 1
	if juego[0][0] == juego[1][2] == juego[2][2] != 0: #comprobando diagonal \
		return 1
	if juego[0][2] == juego[1][1] == juego[2][0] != 0: #comprobando diagonal /
		return 1
	con = 0
	for fila in juego:
		if not 0 in fila:
			con += 1
		if con >= 3:
			return 2
	return 0

def poner_pieza(jugador):
	try: # lugar en donde pueden susuder los errores
		posision = input("pon una posision: ")
		y = int(posision[0])
		x = int(posision[1])
		if juego[x][y] != 0:
			raise ValueError("La casilla ya está ocupada.")
		juego[x][y] = jugador + 1
	except (ValueError, IndexError) as error: # as esto si hay estos errores
		#dhace que tengas que poner otra piesa
		print("posision invalida")
		poner_pieza(jugador)

def tabla():
	for fila in juego: print(fila) #muesta cada fila en distintas lineas

print("estan en tateti.py")
print("pongan sus nombres de jugadores")
jug = [input("jugador 1:  "), input("jugador 2:  ")]
print('bueno ahora a jugar')
jugark = "y"
while  jugark[0] == "y":
	juego = [[0] * 3 for _ in range(3)]
	jugar()
	jugark = input("queres seguir jugando preciona y si, si ")