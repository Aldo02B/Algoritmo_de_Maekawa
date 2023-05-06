#Examen Parcial
#Miembros del equipo:
#Bastida Vargas Karen Mariel
#Gomez Bolaños Luis Aldo
#Hernández Olvera Humberto Ignacio

from proceso import proceso

def main():
  #Conjuntos de votación
  print("\nExamen Parcial: Algoritmos de exlusión mutua\n")
  while(True):
    decision = int(input("\nElije una opción: \n1. Para 4 procesos \n2. Para 3 procesos \n3. Para mejora de Sanders \n4. Salir\nR = "))
    if decision == 1:
      cuatro_procesos()
    elif decision == 2:
      tres_procesos()
    elif decision == 3:
      sanders()
    elif decision == 4:
      return
    else:
      print("Decisión no válida\n")

###################################################################################################################################
###################################################################################################################################

def cuatro_procesos():
  print("\nAlgoritmo de Maekawa con 4 procesos\n")
  print("Se crean los procesos: P1, P2, P3 y P4\n")
  p1 = proceso("p1")
  p2 = proceso("p2")
  p3 = proceso("p3")
  p4 = proceso("p4")

  print("Se crean los grupos de votación\n")
  v1=[p1, p2, p3]
  print("El grupo 1 está constituido de los procesos: P1, P2 y P3")
  v2=[p2, p1, p4]
  print("El grupo 2 está constituido de los procesos: P2, P1 y P4")
  v3=[p3, p4, p1]
  print("El grupo 3 está constituido de los procesos: P3, P4 y P1")
  v4=[p4, p3, p2]
  print("El grupo 4 está constituido de los procesos: P4, P3 y P2\n")

  p1.agrega_grupo_votacion(v1)
  p2.agrega_grupo_votacion(v2)
  p3.agrega_grupo_votacion(v3)
  p4.agrega_grupo_votacion(v4)

  # 1 -> Proceso 2 quiere entrar a la seccion critica
  # 2 -> Proceso 3 quiere entrar a la seccion critica
  # 3 -> Proceso 2 libera
  # 4 -> Proceso 3 libera

  print("El paso 1 es: Proceso 2 quiere entrar a la sección crítica")
  print("El paso 2 es: Proceso 3 quiere entrar a la sección crítica")
  print("El paso 3 es: Proceso 2 libera la sección crítica")
  print("El paso 4 es: Proceso 3 libera la sección crítica\n")

  print("================================================== ESTADO INICIAL ======================================================")
  print("Todos los procesos están en estado Released, sus colas de mensajes están vacías y votación en False")
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n================================================== PASO 1 ==================================================")
  print("---------------------------------------- P2 QUIERE ENTRAR -------------------------------------")
  print("P2 manda mensaje a todos en su grupo de votación (P1, P4) de que quiere entrar, cambia su estado a Wanted y su votación a True")
  envia_mensaje_quiero_entrar(p2)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P2 RECIBE RESPUESTA -------------------------------------")
  print("Los procesos P1 y P4 contestan a P2 y cambian su votación a True")
  envian_respuesta(p2)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- ¿¿ P2 PUEDE ENTRAR ?? -------------------------------------")
  print("Si P2 recibió mensaje de todos los de su grupo de votación, entonces cambia su estado a Held")
  p2.puede_entrar()
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n========================================================= PASO 2 =========================================================")
  print("\n---------------------------------------- P3 QUIERE ENTRAR -------------------------------------")
  print("P3 manda mensaje a todos en su grupo de votación (P1, P4) de que quiere entrar, cambia su estado a Wanted y su votación a True")
  envia_mensaje_quiero_entrar(p3)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P3 RECIBE RESPUESTA  ----------------------------------------")
  print("P3 espera por mensajes de su grupo de votación, pero su grupo de votación tiene votación en True, por lo tanto encolan el mensaje de P3 hasta que se libere la sección crítica de P2")
  envian_respuesta(p3)
  p3.puede_entrar()
  print(p1)
  print(p2)
  print(p3)
  print(p4)
  print("P3 no tiene permiso para entrar")

  print("\n=============================================== PASO 3 =============================================================")
  print("\n---------------------------------------- P2 SALIÓ -------------------------------------")
  print("P2 salió de la sección crítica, cambia su estado a Released y votación a False")
  p2.salio_SC()
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P2 ENVIA MENSAJE YA SALÍ -------------------------------------")
  print("P2 manda mensaje a todos en su grupo de votación (P1, P4) de que ya salió, cambian su votación a False")
  envia_mensaje_sali(p2)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P3 RECIBE RESPUESTA  ----------------------------------------")
  print("P1 y P4 mandan respuesta a P3, cambiando su votación a True y vaciando su cola de mensajes")
  envian_respuesta(p3)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- ¿¿ P3 PUEDE ENTRAR ?? ----------------------------------------")
  print("Si P3 recibió mensaje de todos los de su grupo de votación, entonces cambia su estado a Held")
  p3.puede_entrar()
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n======================================================= PASO 4 ======================================================")
  print("\n----------------------------------- P3 ENVÍA MENSAJE DE SALIDA -------------------------------------")
  print("P3 salió de la sección crítica, cambia su estado a Released y votación a False")
  p3.salio_SC()
  print("P3 manda mensaje a todos en su grupo de votación (P1, P4) de que ya salió, cambian su votación a False")
  envia_mensaje_sali(p3)
  print(p1)
  print(p2)
  print(p3)
  print(p4)
  return

###################################################################################################################################
###################################################################################################################################

def tres_procesos():
  print("Algoritmo de Maekawa con 3 procesos, bloqueo indefinido")
  p1 = proceso("p1")
  p2 = proceso("p2")
  p3 = proceso("p3")

  print("Se crean los grupos de votación\n")
  v1=[p1, p2]
  print("El grupo 1 está constituido de los procesos: P1 y P2")
  v2=[p2, p3]
  print("El grupo 2 está constituido de los procesos: P2 y P3")
  v3=[p3, p1]
  print("El grupo 3 está constituido de los procesos: P3 y P1")

  p1.agrega_grupo_votacion(v1)
  p2.agrega_grupo_votacion(v2)
  p3.agrega_grupo_votacion(v3)

  # 1 -> Proceso 1 quiere entrar a la seccion critica
  # 2 -> Proceso 2 quiere entrar a la seccion critica
  # 3 -> Proceso 3 quiere entrar a la seccion critica

  print("El paso 1 es: Proceso 1 quiere entrar a la sección crítica")
  print("El paso 2 es: Proceso 2 quiere entrar a la sección crítica")
  print("El paso 3 es: Proceso 3 quiere entrar a la sección crítica")

  print("================================================== ESTADO INICIAL ======================================================")
  print("Todos los procesos están en estado Released, sus colas de mensajes están vacías y votación en False")
  print(p1)
  print(p2)
  print(p3)

  print("\n================================================== PASO 1 ==================================================")
  print("---------------------------------------- P1 QUIERE ENTRAR -------------------------------------")
  print("P1 manda mensaje a todos en su grupo de votación (P2) de que quiere entrar, cambia su estado a Wanted y su votación a True")
  envia_mensaje_quiero_entrar(p1)
  envia_mensaje_quiero_entrar(p2)
  envia_mensaje_quiero_entrar(p3)
  print(p1)
  print(p2)
  print(p3)

  print("\n---------------------------------------- P1 RECIBE RESPUESTA -------------------------------------")
  print("P2 contesta a P1 y cambia su votación a True")
  envian_respuesta(p1)
  envian_respuesta(p2)
  envian_respuesta(p3)
  print(p1)
  print(p2)
  print(p3)

  print("\n---------------------------------------- ¿¿ P1 PUEDE ENTRAR ?? -------------------------------------")
  print("Si P1 recibió mensaje de todos los de su grupo de votación, entonces cambia su estado a Held")
  p1.puede_entrar()
  p2.puede_entrar()
  p3.puede_entrar()
  print(p1)
  print(p2)
  print(p3)
  return
 

###################################################################################################################################
###################################################################################################################################

def sanders():
  print("Algoritmo de Maekawa con la mejora de Sanders")
  count = 1
  # Se agregan las marcas de tiempo.
  p1 = proceso("p1")
  p2 = proceso("p2")
  p3 = proceso("p3")
  lista_procesos=[p1, p2, p3]
  print("Se crean los grupos de votación\n")
  v1=[p1, p2]
  print("El grupo 1 está constituido de los procesos: P1 y P2")
  v2=[p2, p3]
  print("El grupo 2 está constituido de los procesos: P2 y P3")
  v3=[p3, p1]
  print("El grupo 3 está constituido de los procesos: P3 y P1")

  p1.agrega_grupo_votacion(v1)
  p2.agrega_grupo_votacion(v2)
  p3.agrega_grupo_votacion(v3)

  # 1 -> Proceso 1 quiere entrar a la seccion critica
  # 2 -> Proceso 2 quiere entrar a la seccion critica
  # 3 -> Proceso 3 quiere entrar a la seccion critica

  print("El paso 1 es: Proceso 1 quiere entrar a la sección crítica")
  print("El paso 2 es: Proceso 2 quiere entrar a la sección crítica")
  print("El paso 3 es: Proceso 3 quiere entrar a la sección crítica")

  print("================================================== ESTADO INICIAL ======================================================")
  print("Todos los procesos están en estado Released, sus colas de mensajes están vacías y votación en False")
  imprimir(p1)
  imprimir(p2)
  imprimir(p3)

  print("\n================================================== PASO 1 ==================================================")
  print("---------------------------------------- P1 QUIERE ENTRAR -------------------------------------")
  print("P1 manda mensaje a todos en su grupo de votación (P2) de que quiere entrar, cambia su estado a Wanted y su votación a True")
     # Si ambos procesos piden entrar a la zona crítica después de esas dos funciones mandamos a llamar a otra donde escoge quien
     # entrará a la SC, aquí se realizara la asignación de marcas de tiempo.
  envia_mensaje_quiero_entrar(p2)
  count = asigna_marca_tiempo(p2, count)
  envia_mensaje_quiero_entrar(p3)
  count = asigna_marca_tiempo(p3, count)
  envia_mensaje_quiero_entrar(p1)
  count = asigna_marca_tiempo(p1, count)

  compara_marca_tiempo(p2, p3)
  compara_marca_tiempo(p3,p1)
  
  imprimir(p1)
  imprimir(p2)
  imprimir(p3)

  return

###################################################################################################################################
###################################################################################################################################

# Proceso que quiere entrar, envia mensaje a todos los de 
# su grupo, cambia su estado a Wanted. Es el paso 1.1, 2.1
def envia_mensaje_quiero_entrar(proceso):
  proceso.quiere_entrar_SC()
  if proceso.estado == "Wanted":
    # Manda a su grupo de votacion un mensaje
    for process in proceso.grupo_votacion:
      process.recibe_mensaje(proceso.nombre)
    proceso.saca_primer_mensaje()

# Los que no son pivote, sólo si votación es False 
# limpian el mensaje que recibieron,
# envían respuesta al pivote, cambian su votacion a True
def envian_respuesta(proceso):
  pivote = proceso.grupo_votacion.pop(0)
  for process in proceso.grupo_votacion:
    if process.votacion == "False":
      process.saca_primer_mensaje()
      pivote.recibe_mensaje(process.nombre)
      process.cambia_votacion_true()
    else:
      # No envia respuesta, mantiene el mensaje en la cola
      print("Hay un proceso en el recurso compartido")
      proceso.regresa_pivote(pivote)
      return
  proceso.regresa_pivote(pivote)
  return

def envia_mensaje_sali(proceso):
  for process in proceso.grupo_votacion:
    process.recibe_mensaje(proceso.nombre)
  for process in proceso.grupo_votacion:
    process.msg.pop()
    process.cambia_votacion_false()
  return


def asigna_marca_tiempo(proceso, count):
  proceso.marca_tiempo = count
  count = count + 1
  return count

#Esta función compara la marca de tiempo de los procesos que se pasan como parámetro, para colocar cuál de ellos es el primero
#en entrar en la sección crítica, entonces se llamaría a la función envían respuesta, que envía la respuesta con la votación
#y se deja entrar con la función puede entrar, que cambia su estado a Held
def compara_marca_tiempo(proceso1, proceso2):
  if(proceso1.marca_tiempo < proceso2.marca_tiempo):
    envian_respuesta(proceso1)
    proceso1.puede_entrar()
  else:
    envian_respuesta(proceso2)
    proceso2.puede_entrar()


def imprimir(proceso):
  print("| Nombre = ", proceso.nombre , "| Estado " , proceso.estado , "| Cola de mensajes ", proceso.msg , "| Votacion " , proceso.votacion , " | Marca de Tiempo " , proceso.marca_tiempo, "\n")

if __name__ == '__main__':
  main()
