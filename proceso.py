class proceso:
  def __init__(self, nombre):
    self.nombre = nombre
    self.estado = "Released"
    self.msg = []
    self.votacion = "False"
    self.grupo_votacion = []

  def quiere_entrar_SC(self):
    self.estado = "Wanted"
    self.votacion = "True"
    self.msg.append(self.nombre)

  def esta_adentro_SC(self):
    self.estado = "Held"
    self.votacion = "True"

  def salio_SC(self):
    self.estado = "Released"
    self.votacion = "True"

  def agrega_grupo_votacion(self, proceso):
    self.grupo_votacion.append(proceso.nombre)

  def saca_primer_mensaje(self):
    self.msg.pop(0)

  def __str__(self):
    return f'Estado = {self.estado}, Cola de mensajes = {self.msg}, Votacion = {self.votacion}'

'''
Otra implementacion es que para no llamar a tantas funciones para cambiar el estado del proceso
podemos definir como atributo una lista de los estados: RELEASED, WANTED Y HELL, para saber 
en que estado se encuentra el proceso podemos ver el primer elemento de la lista donde nos dice que
estado se encuentra, en caso de que se quiera cambiar de estado se busca el que se quiere cambiar en la lista
y se cambia a la primera posicion de la lista y asi sucesivamente para evitar tantas llamadas
a una funcion.
'''