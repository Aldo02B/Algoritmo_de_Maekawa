# Primer Examen Parcial
# Miembros del equipo:
#   Bastida Vargas Karen Mariel
#   Gomez Bolaños Luis Aldo
#   Hernández Olvera Humberto Ignacio

class proceso:
  def __init__(self, nombre):
    self._nombre = nombre
    self.estado = "Released"
    self.msg = []
    self.votacion = "False"
    self.grupo_votacion = []
    self.marca_tiempo = 0

  # Getter para el nombre del proceso
  @property
  def nombre(self):
    return self._nombre

  def quiere_entrar_SC(self):
    self.estado = "Wanted"
    self.votacion = "True"

  def esta_adentro_SC(self):
    self.estado = "Held"

  def cambia_votacion_true(self):
    self.votacion = "True"

  def cambia_votacion_false(self):
    self.votacion = "False"

  def salio_SC(self):
    self.estado = "Released"
    self.votacion = "False"

  def agrega_grupo_votacion(self, proceso):
    for process in proceso:
      self.grupo_votacion.append(process)

  # Función que permite hacer el 1.3 del ejercicio donde cambiamos el valor del proceso
  # a Held.
  def puede_entrar(self):
    pivote = self.grupo_votacion.pop(0)
    for process in self.grupo_votacion:
      if process.votacion == "True" and len(process.msg) == 0:
        continue
      else:
        self.regresa_pivote(pivote)
        return False
    self.estado = "Held"
    self.msg.clear()
    self.regresa_pivote(pivote)
    return True

  def recibe_mensaje(self, mensaje):
    self.msg.append(mensaje)

  def saca_primer_mensaje(self):
    self.msg.pop(0)

  def regresa_pivote(self, proceso):
    self.grupo_votacion.insert(0, proceso)

  def nombres_grupo_votacion(self):
    nombres = []
    for process in self.grupo_votacion:
      nombres.append(process.nombre)
    return nombres

  def __str__(self):
    return f'| Nombre = {self._nombre} | Estado = {self.estado} | Cola de mensajes = {self.msg} | Votacion = {self.votacion} |'
