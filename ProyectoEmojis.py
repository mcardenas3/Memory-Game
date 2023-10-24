# Marcelo Cárdenas Leal
# A00836049
# ITC
# Proyecto - Memorama - Tematica: Animales de frances con Emoji y Palabras

import random, os

#  shuffle(x, random=None) method of Random instance
        #Shuffle list x in place, and return None.
# randint(a, b) method of Random instance
#         Return random integer in range [a, b], including both end points.
# report random, os

def pares( ):
    pars =    """\U0001F413
Poulet
\U0001F9A5
Paresseux
\U0001F9A6
Loutre
\U0001F998
Kangourou
\U0001F430
Lapin
\U0001F418
Éléphant
\U0001F992
Girafe
\U0001F42A
Chameau
\U0001F99B
Hippopotame
\U0001F98F
Rhinocéros
\U0001F416
Porc
\U0001F404
Vache
\U0001F98C
Cerf
\U0001F993
Zèbre
\U0001F405
Tigre
\U0001F408
Chat
\U0001F436
Chien
\U0001F412
Singe"""

    lista = pars.split("\n")
    print("Longitud = ", len(lista))
    for elemento in lista:
        print(elemento)
    
    return lista


from colorama import init, Fore, Back, Style

#variable globales
colores = [Fore.BLACK, Fore.BLUE , Fore.CYAN , Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.LIGHTBLACK_EX ,
           Fore.LIGHTBLUE_EX,Fore.LIGHTCYAN_EX,Fore. LIGHTGREEN_EX,Fore.LIGHTMAGENTA_EX ,Fore.LIGHTRED_EX ,
           Fore.LIGHTWHITE_EX,Fore.LIGHTYELLOW_EX ,Fore.MAGENTA,Fore.RED,Fore.RESET,Fore.WHITE ,Fore.YELLOW ]
 
fondo = [  Back.BLUE, Back.CYAN, Back.GREEN,Back.LIGHTBLACK_EX, Back.LIGHTBLUE_EX, Back.LIGHTCYAN_EX,
 Back.LIGHTGREEN_EX, Back.LIGHTMAGENTA_EX, Back.LIGHTRED_EX, Back.LIGHTWHITE_EX, Back.LIGHTYELLOW_EX,
 Back.MAGENTA, Back.RED, Back.RESET, Back.WHITE , Back.YELLOW ]

init()
  
   
def limpia():
    '''Función que limpia a pantalla sin importar el sistema operativo
      de la máquina donde esté corriendo'''
    if os.name == 'nt': #Windows
        os.system('cls') 
    else:  #'posix'
        os.system('clear') #Mac/linux

def llena_tablero():
  '''Llena el matriz con las "cartas volteadas"'''
  tablero=[]
  for r in range(6):
      renglon=[]
      for c in range(6):
          renglon.append('\U0001F3DD')
      tablero.append(renglon)
  return tablero


def despliega_matriz(matriz, r1 = None, c1 = None, r2 = None, c2 = None):
    renglones = len(matriz)
    columnas = len(matriz[0])
    print("-----------" * renglones)
    r = 1
    for r in range(renglones):
        print(r + 1,"|", end="")
        
        for c in range(columnas):
            if r1 != None and r1 == r and c1 == c:
                print(Back.GREEN+ f'{matriz[r][c]}'.center(10) + Back.RESET , end="")
            elif r2 != None and r2 == r and c2 == c:
                print(Back.GREEN+ f'{matriz[r][c]}'.center(10) + Back.RESET , end="")
            else:
                print(f'{matriz[r][c]}'.center(10) + Back.RESET , end="")
                
            print("|" + Back.RESET, end="")
            
        print('\n'+"-----------"* renglones)
        
"""  
def despliega_matriz(matriz, r1 = None, cl = None, r2 = None, c2 = None):
  '''Despliega a pantalla la matriz que recibe en forma de tabla
  desplegando una cuadricula'''
  print("----------"*len(matriz))
  r = 1
  for renglon in matriz:
    print(r, "|", end="")
    r += 1
    for elemento in renglon:
        # Centra el elemento en un espacio de 5
        print(fondo[r]+ f'{elemento}'.center(10) + Back.RESET , end="")
        print("|", end=""+Back.RESET)
    print('\n'+"----------"*len(matriz))


def despliega_matriz(matriz, r1 = None, c1 = None, r2 = None, c2 = None):
    
    renglones = len(matriz)
    columnas = len(matriz[0])
    
    print("----------"*renglones)
    
    
    for r in range(renglones):
        print(r + 1, "|", end="")
        for c in range(columnas):
        # Centra el elemento en un espacio de 5
            if r1 != None and r1 == r and c1 == elemento:
                print(Back.RED + f'{matriz[r][c]}'.center(10) + Back.RESET , end="")
            elif r2 != None and r2 == r and c2 == elemento:
                print(Back.RED + f'{matriz[r][c]}'.center(10) + Back.RESET , end="")
            else:
                print(fondo[r]+ f'{matriz[r][c]}'.center(10) + Back.RESET , end="")
        
        print("|", end=""+Back.RESET)
    
    print('\n'+"----------"*len(matriz))
"""


def llena_escondida( lista ):
  '''Llena una matriz de emojis y palabras'''
  tablero = []
  
  random.shuffle(lista)
  
  for r in range(6):
      renglon = []
      for c in range(6):
          # agrega cada elemento de la lista
          renglon.append( lista.pop(0) )
      tablero.append(renglon)
  despliega_matriz(tablero)
  
  return tablero


def validar_carta(tablero, r1,c1, r2 = None, c2 = None):
  # verifico si r y c son valores válidos entre 1 y 6
  if r2 is None and c2 is None:
      # validar la carta1 - volver a leer r1 y c1 si no cumple
      while r1 < 1 or r1 > 6 or c1 < 1 or c1 > 6 or tablero[r1 -1][c1 -1] != "\U0001F3DD":
          r1 = int(input('Error, Ingresa de nuevo la posición de la carta 1\nRenglón: '))
          c1 = int(input('Columna: '))
          
      # retornar el valor como debe si ingrso 1,1 regresa 0,0
      return r1 - 1, c1 - 1
    
  else:
      return r2 - 1, c2 - 1


def validar_carta_computadora(tablero, r1,c1, r2 = None, c2 = None):
  # verificar que carta voy a validar
  
  if r2 is None and c2 is None:
      # validar la carta1 - genera un valor random r1 y c1
      while tablero[r1 -1][c1 -1] != "\U0001F3DD":
          r1 = random.randint(1, 6)
          c1 = random.randint(1, 6)
          
      # retornar el valor definitivo de la carta1 de la computadora
      return r1 - 1, c1 - 1
    
  else:
      while tablero[r2 -1][c2 -1] != "\U0001F3DD":
          r2 = random.randint(1, 6)
          c2 = random.randint(1, 6)
      return r2 - 1, c2 - 1


def son_pares(tablero, escondidas, lista_pares, lista_impares, r1, c1, r2, c2):
    
    # Poner la carta1 y la carta2
    tablero[r1][c1] = escondidas[r1][c1]
    tablero[r2][c2] = escondidas[r2][c2]
    
    # Desplegar el tablero
    limpia()
    despliega_matriz(escondidas)
    despliega_matriz(tablero, r1, c1, r2, c2)
    
    gano = 0
    # Verificar si son pares
    # Buscar donde esta la carta
    if escondidas[r1][c1] in lista_pares:
        posicion = lista_pares.index( escondidas[r1][c1] )
        # Verificar si lo que esta en la lista de impares es igual a la carta 2
        if escondidas[r2][c2] == lista_impares[posicion]:
            print(f"Felicidades, es un par")
            gano = 1
        else:
            print(f"No es par!!")
            
            # voltea de nuevo las cartas que no fueron par
            tablero[r1][c1] = "\U0001F3DD"
            tablero[r2][c2] = "\U0001F3DD"
        
    elif escondidas[r1][c1] in lista_impares:
        posicion = lista_impares.index( escondidas[r1][c1] )
        # verificar si lo que esta en la lista pares es igual a la carta2
        if escondidas[r2][c2] == lista_pares[posicion]:
            print(f"Felicidades, es un par")
            gano = 1
        else:
            print(f"No es par!!")
            # voltea las cartas que no fueron par
            tablero[r1][c1] = "\U0001F3DD"
            tablero[r2][c2] = "\U0001F3DD"
            
    return gano


def main():
  # Llamamos a las funciones que llenan las matrices
  lista = pares()
  lista_pares = lista[0: :2]
  lista_impares = lista[1: :2]
  
  tablero = llena_tablero()
  escondidas = llena_escondida( lista )
  
  #contadores de pares de los jugadores antes del ciclo
  pares1 = 0
  pares2 = 0
  
  #funciona mientras un jugador no gane
  while pares1 + pares2 < 18:
    limpia()
    despliega_matriz(escondidas)
    despliega_matriz(tablero)
                            # +++++++++ TURNO DEL USUARIO +++++++++
    print('Escribe la posición del que quieres voltear')
    # Selecciona la primer carta
    r1 =int(input('Ingresa la posición de la carta 1\nRenglón:'))
    c1 =int(input('Columna: '))
    
    r1, c1 = validar_carta(tablero, r1, c1)
    
    # Selecciona la 2a carta
    r2 =int(input('Ingresa la posición de la carta 2\nRenglón: '))
    c2 =int(input('Columna: '))
    
    r2, c2 = validar_carta(tablero, r1, c1, r2, c2)
    
    # actualizar el contador del jugador1
    pares1 += son_pares(tablero, escondidas, lista_pares, lista_impares, r1, c1, r2, c2)
    
    print("Pares del Jugador =", pares1)
    print("Pares de la Computadora =", pares2)
    
                                # +++++++++ TURNO DE LA COMPUTADORA +++++++++
    # generar carta1 de la computadora
    r1 = random.randint(1, 6)
    c1 = random.randint(1, 6)
    
    r1, c1 = validar_carta_computadora(tablero, r1, c1)
    
    # generar carta2 de la computadora
    r2 = random.randint(1, 6)
    c2 = random.randint(1, 6)
    
    r2, c2 = validar_carta_computadora(tablero, r2, c2)
    
    # desplegar al jugador el tiro de la computadora
    print("La computadora eligio la carta1: [", r1 + 1,"]","[", c1 + 1,"]")
    print("La computadora eligio la carta12: [", r2 + 1,"]","[", c2 + 1,"]")
    
    # crear una pausa
    input('Enter para continuar')
    
    # actualizar el contador de la computadora
    pares2 += son_pares(tablero, escondidas, lista_pares, lista_impares, r1, c1, r2, c2)
    
    print("Pares del Jugador = ", pares1)
    print("Pares de la Computadora = ", pares2)
    
    # crear una pausa
    input('Enter para continuar')
    
  # Se acaba el ciclo verifico el resultado
  limpia()
  despliega_matriz(tablero)
  if pares1 > pares2:
      salida = Back.MAGENTA + Fore.WHITE + "GANASTE FELICIDADES!!" + Fore.RESET + Back.RESET
      print(salida.center(80,"*"))
  elif pares1 < pares2:
      salida = Back.LIGHTRED_EX + Fore.WHITE + 'HAZ PERDIDO' + Fore.RESET + Back.RESET
      print(salida.center(80,"*"))
  elif pares1 == pares2:
      salida = Back.LIGHTMAGENTA_EX + "EMPATE!" + Back.RESET
      print(salida.center(80,"*"))
  despliega_matriz(matriz)

main()