import sys

# Obtener una lista de todos los módulos incorporados en Python
builtin_modules = sys.builtin_module_names

# Iterar sobre cada módulo y listar sus recursos
for module_name in builtin_modules:
    try:
        module = __import__(module_name)
        print(f"Recursos de la librería nativa: {module_name}")
        print(dir(module))
        print("=" * 50)  # Separador visual entre los recursos de cada módulo
    except Exception as e:
        print(f"No se pudo cargar el módulo {module_name}: {e}")
