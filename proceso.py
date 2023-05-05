class proceso:
  def __init__(self, nombre):
    self._nombre = nombre
    self.estado = "Released"
    self.msg = []
    self.votacion = "False"
    self.grupo_votacion = []

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
    for process in self.grupo_votacion:
      if process.estado == "Released":
        continue
      else:
        return False
    self.estado = "Held"
    self.msg.clear()
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
    return f'Nombre = {self._nombre}, Estado = {self.estado}, Cola de mensajes = {self.msg}, Votacion = {self.votacion}'

'''
Otra implementacion es que para no llamar a tantas funciones para cambiar el estado del proceso
podemos definir como atributo una lista de los estados: RELEASED, WANTED Y HELL, para saber 
en que estado se encuentra el proceso podemos ver el primer elemento de la lista donde nos dice que
estado se encuentra, en caso de que se quiera cambiar de estado se busca el que se quiere cambiar en la lista
y se cambia a la primera posicion de la lista y asi sucesivamente para evitar tantas llamadas
a una funcion.
'''

'''
groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elected_processes = {0: 1, 1: 4, 2: 7}

def request_resource(process_id, resource_id):
    group_id = resource_id % len(groups)
    elected_process_id = elected_processes[group_id]
    # send a request message to the elected process
    message = f"REQUEST {process_id} {resource_id}"
    send_message(elected_process_id, message)

def release_resource(process_id, resource_id):
    group_id = resource_id % len(groups)
    elected_process_id = elected_processes[group_id]
    # send a release message to the elected process
    message = f"RELEASE {process_id} {resource_id}"
    send_message(elected_process_id, message)

# initialize the queue of pending requests for each group
pending_requests = [[] for _ in range(len(groups))]

def handle_message(message):
    command, process_id, resource_id = message.split()
    group_id = resource_id % len(groups)
    if command == "REQUEST":
        # add the request to the pending requests queue
        pending_requests[group_id].append((process_id, resource_id))
        # check if this process is next in line to access the resource
        if pending_requests[group_id][0][0] == process_id:
            # grant access to the resource
            grant_resource_access(process_id, resource_id)
    elif command == "RELEASE":
        # remove the request from the pending requests queue
        pending_requests[group_id].pop(0)
        # check if there are any other pending requests
        if len(pending_requests[group_id]) > 0:
            # grant access to the next process in line
            next_process_id, next_resource_id = pending_requests[group_id][0]
            grant_resource_access(next_process_id, next_resource_id)

def grant_resource_access(process_id, resource_id):
    # grant access to the resource
    print(f"Process {process_id} granted access to resource {resource_id}")
'''