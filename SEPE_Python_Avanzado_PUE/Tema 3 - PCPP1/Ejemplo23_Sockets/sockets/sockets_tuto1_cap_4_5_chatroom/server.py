import socket  # Libreria para manejar sockets
import select  # Libreria para interactuar con los flujos de entrada y salida del sistema operativo

LONGITUD_CABECERA = 10
IP = "127.0.0.1"
PUERTO = 1234

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
setsockopt (o set socket option), es un metodo que nos permite introducir 
configuraciones a nuestro socket, tiene tres parametros

PRIMERO: El nivel de socket, en este caso el nivel de socket es SOL_SOCKET, con 
SOL_SOCKET lo que indicamos es que configuramos a nivel de socket

SEGUNDO: La opcion de configuracion, permite elegir una opcion de socket para 
posteriormente introducir su configuracion en el tercer parametro. SO_REUSEADDR
permite reutilizar de un socket del servidor despues de un reinicio, con esto 
evitamos un error de tipo "Address already in use"

TERCERO: La configuracion del socket, en este caso le asignamos 1 para decir True o 
verdadero o activado.

"""
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Declaramos el socket como un socket servidor
socket_servidor.bind((IP, PUERTO))

# Declaramos que el socket va a escuchar peticiones
socket_servidor.listen()

# Crearemos una lista de sockets, para crear una lista de clientes.
# Recuerda que en un inicio no tenedremos los sockets de los clientes
# solo tendremos sockets del lado del servidor.
lista_sockets = [socket_servidor] # Aqui podemos poner todos los sockets servidor que queramos.

clientes = {}

# https://youtu.be/CV7_stUWvBQ?list=PLQVvvaa0QuDdzLB_0JSTTcl8E8jsJLhR5&t=396

def recibir_mensaje(socket_cliente: socket):
    try:
        # Recibiremos el mensaje junto con su cabecera
        cabecera_mensaje = socket_cliente.recv(LONGITUD_CABECERA)

        if not len(cabecera_mensaje):
            return False

        # Lo decodificamos y le quitamos el relleno
        longitud_mensaje = int(cabecera_mensaje.decode("utf-8").strip())

        # Devolvemos un diccionario con la cabecera y con el mensaje
        return {"header": cabecera_mensaje, "data": socket_cliente.recv(longitud_mensaje)}

    except Exception as e:
        print(e)
        return False

while True:
    # El metodo select nos permite supervisar multiples flujos de entrada y salida,
    # hasta que alguno de ellos este listo para operar, hay tres parametros:
    # 1º lectura : si le pasas una lista de objetos, estos seran leidos.
    # 2º escritura : si le pasas una lista de objetos, estos se escribiran sobre ellos, sin riesgo a se bloqueado.
    # 3º excepciones : si le pasas una lista de objetos, se examinaran para ver si ocasionan excepciones.
    # Este metodo en concreto trabaja con objetos que tengan implementados el metodo fileno()
    #
    # El guion bajo es una variable a modo de papelera, para meter valores que no nos interesan
    lectura_sockets, _, excepcion_sockets = select.select(lista_sockets, [], lista_sockets)

    # Iteramos la lista sockets servidor (el listado de los clientes), para trabajar con varios sockets,
    # hay otras formas pero esta es la mas sencilla.
    for socket_notificado in lectura_sockets:

        # Averiguamos si el socket leido es el socket servidor que vamos a usar para realizar las peticiones
        # correspondientes. Esto es para que en caso de que tengamos mas de socket podamos realizar las operaciones
        # solamente en los sockets servidor con los que queramos trabajar
        if socket_notificado == socket_servidor:

            # Aceptamos solicitudes sobre el socket servidor con el que vamos a trabajar
            socket_cliente, direccion_cliente = socket_servidor.accept()

            usuario = recibir_mensaje(socket_cliente) # Recibimos el mensaje

            if usuario is False:
                continue

            lista_sockets.append(socket_cliente)

            clientes[socket_cliente] = usuario

            print(f"Conexion aceptada desde {direccion_cliente[0]}:{direccion_cliente[1]} " +
                  f"por: {usuario['data'].decode("utf-8")}")

        else:

            mensaje = recibir_mensaje(socket_notificado)

            if mensaje is False:
                print(f"Conexion cerrada por {clientes[socket_notificado]['data'].decode("utf-8")}")
                lista_sockets.remove(socket_notificado)
                del clientes[socket_notificado]
                continue

            usuario = clientes[socket_notificado]

            print(f"Mensaje recibido desde {usuario['data'].decode("utf-8")}: {mensaje['data'].decode("utf-8")}")

            for socket_cliente in clientes:
                if socket_cliente != socket_notificado:
                    socket_cliente.send(usuario['header'] + usuario['data'] + mensaje['header'] + mensaje['data'])

    for socket_notificado in excepcion_sockets:
        lista_sockets.remove(socket_notificado)
        del clientes[socket_notificado]
