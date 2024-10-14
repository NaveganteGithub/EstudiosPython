import platform

# funcion platform
print(platform.platform())
print(platform.platform(aliased=True))
print(platform.platform(aliased=True, terse=True))
print(platform.platform(0, 0))

# funcion machine: nombre generico del procesador
print(platform.machine()) # Nombre largo

# funcion processor: nombre real del procesador
print(platform.processor()) # Nombre acortado

# funcion system: nombre del Sistema Operativo
print(platform.system())

# funcion version: version del Sistema Operativo
print(platform.version())

# funcion python_implementation: implementacion de Python
print(platform.python_implementation())

# funcion version: Retorna la version de python
print(platform.python_version())  # 3.10.0
print(platform.python_version_tuple()) # ('3', '10', '0')

