from proceso import *

def main():
  # LOL
  #Conjuntos de votación
  print("Se crean los procesos: P1, P2, P3 y P4")
  p1 = proceso("p1")
  p2 = proceso("p2")
  p3 = proceso("p3")
  p4 = proceso("p4")
  
  print("Se crean los grupos de votación")
  v1=[p1, p2, p3]
  print("El grupo 1 está constituido de los procesos: P1, P2 y P3")
  v2=[p2, p1, p4]
  print("El grupo 2 está constituido de los procesos: P2, P1 y P4")
  v3=[p3, p4, p1]
  print("El grupo 3 está constituido de los procesos: P3, P4 y P1")
  v4=[p4, p3, p2]
  print("El grupo 4 está constituido de los procesos: P4, P3 y P2")

  p1.agrega_grupo_votacion(v1)
  p2.agrega_grupo_votacion(v2)
  p3.agrega_grupo_votacion(v3)
  p4.agrega_grupo_votacion(v4)

  # 1 -> Proceso 2 quiere entrar a la seccion critica
  # 2 -> Proceso 3 quiere entrar a la seccion critica
  # 3 -> Proceso 2 libera
  # 4 -> Proceso 3 libera

  print("\n------------------------------------- Estado 0----------------------------------------------")
  print(p1)
  print(p2)
  print(p3)
  print(p4)
  print("\n\n######################################## PASO 1 ###############################################")
  print("---------------------------------------- P2 QUIERE ENTRAR -------------------------------------")

  envia_mensaje_quiero_entrar(p2)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  
  print("\n---------------------------------------- P2 RECIBE RESPUESTA -------------------------------------")
  envian_respuesta(p2)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P2 PUEDE ENTRAR ?? -------------------------------------")
  p2.puede_entrar()
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n\n######################################## PASO 2 ###############################################")
  print("---------------------------------------- P3 QUIERE ENTRAR -------------------------------------")
  envia_mensaje_quiero_entrar(p3)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P3 RECIBE RESPUESTA  ----------------------------------------")
  envian_respuesta(p3)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P3 PUEDE ENTRAR ?? -------------------------------------")
  p3.puede_entrar()
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n\n######################################## PASO 3 ###############################################")
  print("---------------------------------------- P2 SALIÓ -------------------------------------")
  p2.salio_SC()
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P2 ENVIA MENSAJE YA SALÍ -------------------------------------")
  envia_mensaje_sali(p2)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  
  print("\n---------------------------------------- P3 RECIBE RESPUESTA  ----------------------------------------")
  envian_respuesta(p3)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n---------------------------------------- P3 PUEDE ENTRAR ?? ----------------------------------------")
  p3.puede_entrar()
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  print("\n######################################## PASO 4 ###############################################")
  print("----------------------------------- P3 ENVÍA MENSAJE DE SALIDA -------------------------------------")
  envia_mensaje_sali(p3)
  print(p1)
  print(p2)
  print(p3)
  print(p4)

  return

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
      pass
  proceso.regresa_pivote(pivote)
  return

def envia_mensaje_sali(proceso):
  for process in proceso.grupo_votacion:
    process.recibe_mensaje(proceso.nombre)
  proceso.saca_primer_mensaje()
  pivote = proceso.grupo_votacion.pop(0)
  for process in proceso.grupo_votacion:
    process.msg.pop()
    process.cambia_votacion_false()
  return

if __name__ == '__main__':
  main()

# TODO: Revisar desde Paso 2
# TODO: P2 no esta cambiando a HELD, revisar funcion puede_entrar()
# TODO: P3 no debe cambiar a HELD en el primer P3 PUEDE ENTRAR ?? -- LINEA 77
# TODO: Desde paso 3, P2 y P3 no están limpiando su cola de mensajes